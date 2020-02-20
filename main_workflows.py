from __future__ import print_function
import uuid
import core.api
from core.api.rest import ApiException
from pprint import pprint


def get_example_manifest():
    return """
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: pytorch-
spec:
  entrypoint: main
  onExit: exitHandler
  arguments:
    parameters:
    - name: source
      value: https://github.com/onepanelio/pytorch-examples.git
    - name: command
      value: "python mnist/main.py --epochs=1"
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 2Gi
  - metadata:
      name: output
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 2Gi
  templates:
  - name: main
    dag:
      tasks:
      - name: train-model
        template: pytorch
      - name: notify-in-slack
        dependencies: [train-model]
        template: slack-notify-success
        arguments:
          parameters:
          - name: status
            value: "{{tasks.train-model.status}}"
          artifacts:
          - name: metrics
            from: "{{tasks.train-model.outputs.artifacts.sys-metrics}}"
  - name: exitHandler
    dag:
      tasks:
      - name: notify-error-in-slack
        template: slack-notify-failed
        when: "{{workflow.status}} == Failed || {{workflow.status}} == Error"
  - name: pytorch
    inputs:
      artifacts:
      - name: src
        path: /mnt/src
        git:
          repo: "{{workflow.parameters.source}}"
    outputs:
      artifacts:
      - name: model
        path: /mnt/output
        optional: true
        archive:
          none: {}
    container:
      image: pytorch/pytorch:latest
      command: [sh,-c]
      args: ["{{workflow.parameters.command}}"]
      workingDir: /mnt/src
      volumeMounts:
      - name: data
        mountPath: /mnt/data
      - name: output
        mountPath: /mnt/output
  - name: slack-notify-success
    container:
      image: technosophos/slack-notify
      command: [sh,-c]
      args: ['SLACK_USERNAME=Worker SLACK_TITLE="{{workflow.name}} {{inputs.parameters.status}}" SLACK_ICON=https://www.gravatar.com/avatar/5c4478592fe00878f62f0027be59c1bd SLACK_MESSAGE=$(cat /tmp/metrics.json)} ./slack-notify']
    inputs:
      parameters:
      - name: status
      artifacts:
      - name: metrics
        path: /tmp/metrics.json
        optional: true
  - name: slack-notify-failed
    container:
      image: technosophos/slack-notify
      command: [sh,-c]
      args: ['SLACK_USERNAME=Worker SLACK_TITLE="{{workflow.name}} {{workflow.status}}" SLACK_ICON=https://www.gravatar.com/avatar/5c4478592fe00878f62f0027be59c1bd SLACK_MESSAGE="Worfklow failed" ./slack-notify']        
    """

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    api_client.configuration.host = "http://localhost:8888"

    name_create_and_use_template = uuid.uuid4().hex.upper()[0:6]
    name_template_to_archive = uuid.uuid4().hex.upper()[0:6]

    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'aleksandr'  # str |

    archive_template_uid = ""
    try:
        print("WorkflowServiceApi->create_workflow_template")
        archive_body = core.api.WorkflowTemplate()
        archive_body.name = name_template_to_archive
        archive_body.manifest = get_example_manifest()
        api_response = api_instance.create_workflow_template(namespace, archive_body)
        archive_template_uid = api_response.uid
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow_template: %s\n" % e)

    body = core.api.WorkflowTemplate()  # WorkflowTemplate |
    body.name = name_create_and_use_template
    body.manifest = get_example_manifest()
    try:
        print("WorkflowServiceApi->create_workflow_template")
        api_response = api_instance.create_workflow_template(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow_template: %s\n" % e)

    workflow_template_uid = ""
    workflow_template_version = 0
    try:
        print("WorkflowServiceApi->list_workflow_templates")
        api_response = api_instance.list_workflow_templates(namespace)
        if api_response.count > 0:
            last_elem = api_response.count - 1
            workflow_template_uid = api_response.workflow_templates[0].uid
            workflow_template_version = api_response.workflow_templates[0].version
            workflow_template_manifest = api_response.workflow_templates[0].manifest
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflow_templates: %s\n" % e)

    try:
        print("WorkflowServiceApi->create_workflow_template_version")
        api_response = api_instance.create_workflow_template_version(namespace, workflow_template_uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow_template_version: %s\n" % e)

    # Need some workflows for the next piece

    try:
        print("WorkflowServiceApi->create_workflow")
        workflow_body = core.api.Workflow()  # Workflow |
        workflow_body.parameters = [{"name":"SLACK_WEBHOOK", "value":"https://hooks.slack.com/services/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"}, {"name":"PARAM2", "value":"VALUE2"}]
        workflow_template = core.api.WorkflowTemplate()
        workflow_template.uid = workflow_template_uid
        workflow_template.name = body.name
        workflow_template.manifest = workflow_template_manifest
        workflow_template.version = workflow_template_version
        workflow_body.workflow_template = workflow_template
        api_response = api_instance.create_workflow(namespace, workflow_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow: %s\n" % e)


    page_size = 15
    page = 1
    try:
        print("WorkflowServiceApi->list_workflows")
        workflows = api_response = api_instance.list_workflows(namespace, workflow_template_uid=workflow_template_uid, workflow_template_version=workflow_template_version, page_size=page_size, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflows: %s\n" % e)

    specific_workflow_to_use = None
    try:
        print("WorkflowServiceApi->get_workflow")
        if workflows.count is not None and workflows.count > 0:
            specific_workflow_name = workflows.workflows[0].name
            specific_workflow_to_use = api_response = api_instance.get_workflow(namespace, specific_workflow_name)
            pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow: %s\n" % e)


    # try:
    #     api_response = api_instance.watch_workflow(namespace, specific_workflow_to_use.name)
    #     pprint(api_response)
    # except ApiException as e:
    #     print("Exception when calling WorkflowServiceApi->watch_workflow: %s\n" % e)

    try:
        if specific_workflow_to_use is not None:
            print("WorkflowServiceApi->get_workflow_logs")
            name = 'name_example'  # str |
            pod_name = 'pod_name_example'  # str |
            container_name = 'container_name_example'  # str |
            api_response = api_instance.get_workflow_logs(namespace, specific_workflow_to_use.name, pod_name, container_name)
            pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_logs: %s\n" % e)

    try:
        api_response = api_instance.archive_workflow_template(namespace, archive_template_uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->archive_workflow_template: %s\n" % e)

