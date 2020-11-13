import logging
import pyaml
import os
import json
import zlib
from couler.argo_submitter import ArgoSubmitter
import onepanel.core.api
from onepanel.core.api.rest import ApiException


class OnepanelException(Exception):
    """Base-class for all exceptions raised by the OnepanelSubmitter"""


class MissingTokenException(OnepanelException):
    """
    Happens when there is no provided token and one can't be found on the system.
    """


class MissingHostException(OnepanelException):
    """
    Happens when there is no provided host and can't be found on the system
    """


class InvalidCredentialsException(OnepanelException):
    """
    Happens when the credentials to get the authentication token are incorrect.
    """


class LongWorkflowNameException(OnepanelException):
    """
    Happens when the workflow name is too long - which is >= 20 characters.
    """


class Submitter(ArgoSubmitter):
    """A submitter which submits a workflow to Onepanel"""
    def __init__(self, workflow_name, username=None, token=None, host=None):
        if len(workflow_name) >= 20:
            raise LongWorkflowNameException('workflow_name must be 20 characters or less.')
        # If token and api_url are not passed in, use the values from token file and environment variable
        # If those don't exist, throw an exception
        self.namespace = os.getenv('ONEPANEL_RESOURCE_NAMESPACE')
        self.workflow_name = workflow_name

        if host is None:
            host = os.getenv('ONEPANEL_API_URL')
            if host is None:
                raise MissingHostException()

        self.configuration = onepanel.core.api.Configuration(host)
        logging.basicConfig(level=logging.INFO)

        if token is None:
            try:
                with open('/var/run/secrets/kubernetes.io/serviceaccount/token') as f:
                    self.token = f.read()
            except FileNotFoundError:
                raise MissingTokenException('Token not set and no token found on system')
            logging.info('Onepanel configuration detected')
        else:
            try:
                self.token = self._get_token(host, username, token)
            except ApiException as e:
                if e.status == 400:
                    raise InvalidCredentialsException('The provided credentials are invalid')

        self.configuration.api_key['authorization'] = self.token
        self.configuration.api_key_prefix['authorization'] = 'Bearer'
        logging.info('Initialized')

    def _get_workflow_template(self, namespace, name):
        """
        Attempts to get the workflow template from the API.
        If the template exists, it is returned.
        If it does not, None is returned.
        """
        try:
            with onepanel.core.api.ApiClient(self.configuration) as api_client:
                api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
                api_response = api_instance.get_workflow_template(namespace, name)
                return api_response
        except ApiException as e:
            if e.status == 404:
                return None
        return None

    def _are_workflow_template_manifests_equal(self, workflow_template, manifest):
        """
        Compare the crc32 hash of the workflow_template manifest and the input manifest
        If they are the same (same contents) return true, false otherwise.
        If workflow_template is None, false is automatically returned.
        """
        if workflow_template is None:
            return False
        yaml_str = workflow_template.to_dict()['manifest']
        hash1 = str(zlib.crc32(manifest.encode()))
        hash2 = str(zlib.crc32(yaml_str.encode()))
        return hash1 == hash2

    def _create_workflow_template(self, namespace, body):
        with onepanel.core.api.ApiClient(self.configuration) as api_client:
            api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
            workflow_template = api_instance.create_workflow_template(
                namespace,
                body
            )
            return workflow_template

    def _create_template_version(self, namespace, workflow_template_uid, body):
        with onepanel.core.api.ApiClient(self.configuration) as api_client:
            api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
            api_instance.create_workflow_template_version(namespace, workflow_template_uid, body)

    def _execute_workflow(self, namespace, workflow_template_uid):
        with onepanel.core.api.ApiClient(self.configuration) as api_client:
            api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
            body = onepanel.core.api.CreateWorkflowExecutionBody(
                parameters=[],
                workflow_template_uid=workflow_template_uid,
                labels=[{'key': 'created-by', 'value': 'couler'}])
            return api_instance.create_workflow_execution(namespace, body)

    def _get_token(self, host, username, token):
        with onepanel.core.api.ApiClient(self.configuration) as api_client:
            api_instance = onepanel.core.api.AuthServiceApi(api_client)
            body = onepanel.core.api.GetAccessTokenRequest(username, token)
            return api_instance.get_access_token(body).to_dict()['access_token']

    def template_to_argo(self, workflow_yaml):
        output_dict = json.loads(json.dumps(workflow_yaml))
        yaml = output_dict['spec']
        manifest = pyaml.dump(yaml)
        return manifest

    def submit(self, workflow_yaml, secrets=None):
        if secrets is None:
            secrets = []

        for secret in secrets:
            self._create_secret(secret.to_yaml())
        manifest = self.template_to_argo(workflow_yaml)
        body = onepanel.core.api.WorkflowTemplate(
            manifest=manifest,
            name=self.workflow_name,
            labels=[{'key': 'created-by', 'value': 'couler'}]
        )
        workflow_template = self._get_workflow_template(self.namespace, self.workflow_name)
        # If we don't have a template, create one
        if workflow_template is None:
            workflow_template = self._create_workflow_template(self.namespace, body)
            logging.info('Workflow Template Created')
        elif not self._are_workflow_template_manifests_equal(workflow_template, manifest):
            # The contents are different, so create a new version.
            # If the contents are the same, no need for a new version.
            self._create_template_version(self.namespace, self.workflow_name, body)
            logging.info('Workflow Template updated')
        self._execute_workflow(self.namespace, workflow_template.uid)
        logging.info('Workflow Executed')
