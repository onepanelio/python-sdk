import logging
import pyaml
import os
import json
import zlib

from couler.argo_submitter import ArgoSubmitter

import onepanel.core.api
from onepanel.core.api.rest import ApiException


class OnepanelSubmitter(ArgoSubmitter):
    """A submitter which submits a workflow to Onepanel"""

    namespace = os.getenv('ONEPANEL_RESOURCE_NAMESPACE')
    # username = 'admin'
    # host = os.getenv('ONEPANEL_API_URL')

    def __init__(self, username, workflow_name, host, token):
        # NOTE: Need to take username, api_url here as well
        # If token and api_url are not passed in, use the values from token file and environment variable
        # If those don't exist, throw an exception
        self.token = token
        self.workflow_name = workflow_name
        self.host = host
        self.username = username
        self.configuration = onepanel.core.api.Configuration(self.host)

        logging.basicConfig(level=logging.INFO)
        try:
            with open('/var/run/secrets/kubernetes.io/serviceaccount/token') as f:
                api_token = f.read()
            self.configuration.api_key['authorization'] = api_token
            self.configuration.api_key_prefix['authorization'] = 'Bearer'
            logging.info('Onepanel configuration detected')

        except Exception:
            api_token = self._get_token(host, username, token)
            self.configuration.api_key['authorization'] = api_token
            self.configuration.api_key_prefix['authorization'] = 'Bearer'
        except Exception as e:
            print(e)
        with onepanel.core.api.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            self.api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
        logging.info('Initialized')

    # If template exist, compare the crc32 hash of workflow_yaml and the YAML returned from get_workflow_template()
    def _get_workflow_template(self, namespace, name, workflow_template):
        with onepanel.core.api.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
            api_response = api_instance.get_workflow_template(namespace, name)
            yaml_str = api_response.to_dict()['manifest']
            hash1 = str(zlib.crc32(workflow_template.encode()))
            hash2 = str(zlib.crc32(yaml_str.encode()))
        return bool(hash1 != hash2)

    def _create_workflow_template(self, namespace, body):
        try:
            workflow_template = self.api_instance.create_workflow_template(
                namespace,
                body
            )
            self._execute_workflow(namespace, workflow_template.uid)
        except ApiException as e:
            print("Exception when calling WorkflowTemplateServiceApi->create_workflow_template: %s\n" % e)

    def _create_template_version(self, namespace, workflow_template_uid, body):
        with onepanel.core.api.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance=onepanel.core.api.WorkflowTemplateServiceApi(api_client)
            try:
                api_response = api_instance.create_workflow_template_version(namespace, workflow_template_uid, body)
                logging.info("New template version added to %s" % workflow_template_uid)
                print(api_response)
            except ApiException as e:
                print("Exception when calling WorkflowTemplateServiceApi->create_workflow_template_version: %s\n" % e)

    def _execute_workflow(self, namespace, workflow_template_uid):
        params = []
        # Enter a context with an instance of the API client
        with onepanel.core.api.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
            # NOTE: `label` was added here
            body = onepanel.core.api.CreateWorkflowExecutionBody(
                parameters=params,
                workflow_template_uid=workflow_template_uid,
                labels=[{'key': 'created-by', 'value': 'couler'}])
            try:
                workflow = api_instance.create_workflow_execution(namespace, body)
                if workflow:
                    logging.info('Executing Workflow %s in namespace: %s' % (workflow.name, self.namespace))
            except ApiException as e:
                print('There was an error executing the Workflow: %s\n' % e)

    def _get_token(self, host, username, token):
        with onepanel.core.api.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance=onepanel.core.api.AuthServiceApi(api_client)
            body=onepanel.core.api.GetAccessTokenRequest(username, token) # LogInRequest

            try:
                # NOTE: This should use the new login command
                return api_instance.get_access_token(body).to_dict()['access_token']

            except ApiException as e:
                print('There was an error with your credentials: %s\n' % e)

    def template_to_argo(self, workflow_yaml):
        output_dict = json.loads(json.dumps(workflow_yaml))
        yaml = output_dict['spec']
        manifest = pyaml.dump(yaml)
        return manifest

    def submit(self, workflow_yaml, secrets=None):
        if secrets:
            for secret in secrets:
                self._create_secret(secret.to_yaml())
        if len(self.workflow_name) >= 20:
            logging.info('Name must be 20 characters or less.')
            return
        manifest = self.template_to_argo(workflow_yaml)
        # NOTE: `label` was added here
        body = onepanel.core.api.WorkflowTemplate(
            manifest=manifest,
            name=self.workflow_name,
            labels=[{'key': 'created-by', 'value': 'couler'}])
        # The method calls should all be here as follows:
        # _get_workflow_template
        # If workflow_template exists, call _create_worfklow_template_version
        # If it does not exist, call create_workflow_template
        workflow_template = self._get_workflow_template(self.namespace, self.workflow_name, manifest)
        if workflow_template:
            self._create_template_version(self.namespace, self.workflow_name, body)
        else:
            self._create_workflow_template(self.namespace, body)
