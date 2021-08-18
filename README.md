# onepanel-sdk
Onepanel Python SDK

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/onepanelio/core](https://github.com/onepanelio/core)

## Requirements.

Python 3.6+

## Installation & Usage
### pip install

To install from PyPI:

```sh
pip install onepanel-sdk
```
(you may need to run `pip` with root permission: `sudo pip install onepanel-sdk`)

Then import the package:
```python
import onepanel.core.api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import onepanel.core.api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import onepanel.core.auth
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8888
# See configuration.py for a list of all supported configuration parameters.
configuration = onepanel.core.api.Configuration(
    host = "http://localhost:8888"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# If inside Onepanel you do not need to pass any parameters to `get_access_token`
access_token = onepanel.core.auth.get_access_token(username='<username>', token='<token>', host='<host>')

# Configure API key authorization: Bearer
configuration = onepanel.core.api.Configuration(
    host = "http://localhost:8888",
    api_key = {
        'authorization': access_token
    }
)
configuration.api_key_prefix['authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.InferenceServiceApi(api_client)

    try:
        api_response = api_instance.get_inference_service(namespace='<namespace>')
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InferenceServiceApi->get_inference_service: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8888*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthServiceApi* | [**get_access_token**](docs/AuthServiceApi.md#get_access_token) | **POST** /apis/v1beta1/auth/get_access_token | 
*AuthServiceApi* | [**is_authorized**](docs/AuthServiceApi.md#is_authorized) | **POST** /apis/v1beta1/auth | 
*AuthServiceApi* | [**is_valid_token**](docs/AuthServiceApi.md#is_valid_token) | **POST** /apis/v1beta1/auth/token | 
*ConfigServiceApi* | [**get_config**](docs/ConfigServiceApi.md#get_config) | **GET** /apis/v1beta1/config | 
*ConfigServiceApi* | [**get_namespace_config**](docs/ConfigServiceApi.md#get_namespace_config) | **GET** /apis/v1beta1/{namespace}/config | 
*CronWorkflowServiceApi* | [**create_cron_workflow**](docs/CronWorkflowServiceApi.md#create_cron_workflow) | **POST** /apis/v1beta1/{namespace}/cron_workflow | 
*CronWorkflowServiceApi* | [**delete_cron_workflow**](docs/CronWorkflowServiceApi.md#delete_cron_workflow) | **DELETE** /apis/v1beta1/{namespace}/cron_workflows/{uid} | 
*CronWorkflowServiceApi* | [**get_cron_workflow**](docs/CronWorkflowServiceApi.md#get_cron_workflow) | **GET** /apis/v1beta1/{namespace}/cron_workflow/{uid} | 
*CronWorkflowServiceApi* | [**list_cron_workflows**](docs/CronWorkflowServiceApi.md#list_cron_workflows) | **GET** /apis/v1beta1/{namespace}/cron_workflows | 
*CronWorkflowServiceApi* | [**list_cron_workflows2**](docs/CronWorkflowServiceApi.md#list_cron_workflows2) | **GET** /apis/v1beta1/{namespace}/cron_workflows/{workflowTemplateName} | 
*CronWorkflowServiceApi* | [**update_cron_workflow**](docs/CronWorkflowServiceApi.md#update_cron_workflow) | **PUT** /apis/v1beta1/{namespace}/cron_workflow/{uid} | 
*FileServiceApi* | [**get_object_download_presigned_url**](docs/FileServiceApi.md#get_object_download_presigned_url) | **GET** /apis/v1beta1/{namespace}/files/presigned-url/{key} | 
*FileServiceApi* | [**list_files**](docs/FileServiceApi.md#list_files) | **GET** /apis/v1beta1/{namespace}/files/list/{path} | 
*InferenceServiceApi* | [**create_inference_service**](docs/InferenceServiceApi.md#create_inference_service) | **POST** /apis/v1beta1/{namespace}/inferenceservice | 
*InferenceServiceApi* | [**delete_inference_service**](docs/InferenceServiceApi.md#delete_inference_service) | **DELETE** /apis/v1beta1/{namespace}/inferenceservice/{name} | 
*InferenceServiceApi* | [**get_inference_service**](docs/InferenceServiceApi.md#get_inference_service) | **GET** /apis/v1beta1/{namespace}/inferenceservice/{name} | 
*LabelServiceApi* | [**add_labels**](docs/LabelServiceApi.md#add_labels) | **POST** /apis/v1beta1/{namespace}/{resource}/{uid}/labels | 
*LabelServiceApi* | [**delete_label**](docs/LabelServiceApi.md#delete_label) | **DELETE** /apis/v1beta1/{namespace}/{resource}/{uid}/labels/{key} | 
*LabelServiceApi* | [**get_available_labels**](docs/LabelServiceApi.md#get_available_labels) | **GET** /apis/v1beta1/{namespace}/{resource}/labels | 
*LabelServiceApi* | [**get_labels**](docs/LabelServiceApi.md#get_labels) | **GET** /apis/v1beta1/{namespace}/{resource}/{uid}/labels | 
*LabelServiceApi* | [**replace_labels**](docs/LabelServiceApi.md#replace_labels) | **PUT** /apis/v1beta1/{namespace}/{resource}/{uid}/labels | 
*NamespaceServiceApi* | [**create_namespace**](docs/NamespaceServiceApi.md#create_namespace) | **POST** /apis/v1beta1/namespaces | 
*NamespaceServiceApi* | [**list_namespaces**](docs/NamespaceServiceApi.md#list_namespaces) | **GET** /apis/v1beta1/namespaces | 
*SecretServiceApi* | [**add_secret_key_value**](docs/SecretServiceApi.md#add_secret_key_value) | **POST** /apis/v1beta1/{namespace}/secrets/{secret.name} | 
*SecretServiceApi* | [**create_secret**](docs/SecretServiceApi.md#create_secret) | **POST** /apis/v1beta1/{namespace}/secrets | 
*SecretServiceApi* | [**delete_secret**](docs/SecretServiceApi.md#delete_secret) | **DELETE** /apis/v1beta1/{namespace}/secrets/{name} | 
*SecretServiceApi* | [**delete_secret_key**](docs/SecretServiceApi.md#delete_secret_key) | **DELETE** /apis/v1beta1/{namespace}/secrets/{secretName}/keys/{key} | 
*SecretServiceApi* | [**get_secret**](docs/SecretServiceApi.md#get_secret) | **GET** /apis/v1beta1/{namespace}/secrets/{name} | 
*SecretServiceApi* | [**list_secrets**](docs/SecretServiceApi.md#list_secrets) | **GET** /apis/v1beta1/{namespace}/secrets | 
*SecretServiceApi* | [**secret_exists**](docs/SecretServiceApi.md#secret_exists) | **GET** /apis/v1beta1/{namespace}/secrets/{name}/exists | 
*SecretServiceApi* | [**update_secret_key_value**](docs/SecretServiceApi.md#update_secret_key_value) | **PATCH** /apis/v1beta1/{namespace}/secrets/{secret.name} | 
*ServiceServiceApi* | [**get_service**](docs/ServiceServiceApi.md#get_service) | **GET** /apis/v1beta1/{namespace}/service/{name} | 
*ServiceServiceApi* | [**has_service**](docs/ServiceServiceApi.md#has_service) | **GET** /apis/v1beta/service/{name} | 
*ServiceServiceApi* | [**list_services**](docs/ServiceServiceApi.md#list_services) | **GET** /apis/v1beta1/{namespace}/service | 
*WorkflowServiceApi* | [**add_workflow_execution_metrics**](docs/WorkflowServiceApi.md#add_workflow_execution_metrics) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid}/metric | 
*WorkflowServiceApi* | [**add_workflow_execution_statistics**](docs/WorkflowServiceApi.md#add_workflow_execution_statistics) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid}/statistics | 
*WorkflowServiceApi* | [**clone_workflow_execution**](docs/WorkflowServiceApi.md#clone_workflow_execution) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid} | Clone a Workflow. This is the same as running it again.
*WorkflowServiceApi* | [**create_workflow_execution**](docs/WorkflowServiceApi.md#create_workflow_execution) | **POST** /apis/v1beta1/{namespace}/workflow_executions | Creates a Workflow
*WorkflowServiceApi* | [**cron_start_workflow_execution_statistic**](docs/WorkflowServiceApi.md#cron_start_workflow_execution_statistic) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid}/cron_start_statistics | 
*WorkflowServiceApi* | [**get_workflow_execution**](docs/WorkflowServiceApi.md#get_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid} | 
*WorkflowServiceApi* | [**get_workflow_execution_logs**](docs/WorkflowServiceApi.md#get_workflow_execution_logs) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/pods/{podName}/containers/{containerName}/logs | 
*WorkflowServiceApi* | [**get_workflow_execution_metrics**](docs/WorkflowServiceApi.md#get_workflow_execution_metrics) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/pods/{podName}/metrics | 
*WorkflowServiceApi* | [**get_workflow_execution_statistics_for_namespace**](docs/WorkflowServiceApi.md#get_workflow_execution_statistics_for_namespace) | **GET** /apis/v1beta1/{namespace}/workflow_execution/statistics | 
*WorkflowServiceApi* | [**list_workflow_executions**](docs/WorkflowServiceApi.md#list_workflow_executions) | **GET** /apis/v1beta1/{namespace}/workflow_executions | 
*WorkflowServiceApi* | [**list_workflow_executions_field**](docs/WorkflowServiceApi.md#list_workflow_executions_field) | **GET** /apis/v1beta/{namespace}/field/workflow_executions/{fieldName} | 
*WorkflowServiceApi* | [**resubmit_workflow_execution**](docs/WorkflowServiceApi.md#resubmit_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/resubmit | 
*WorkflowServiceApi* | [**terminate_workflow_execution**](docs/WorkflowServiceApi.md#terminate_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/terminate | 
*WorkflowServiceApi* | [**update_workflow_execution_metrics**](docs/WorkflowServiceApi.md#update_workflow_execution_metrics) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/metric | 
*WorkflowServiceApi* | [**update_workflow_execution_status**](docs/WorkflowServiceApi.md#update_workflow_execution_status) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/status | 
*WorkflowServiceApi* | [**watch_workflow_execution**](docs/WorkflowServiceApi.md#watch_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/watch | 
*WorkflowTemplateServiceApi* | [**archive_workflow_template**](docs/WorkflowTemplateServiceApi.md#archive_workflow_template) | **PUT** /apis/v1beta1/{namespace}/workflow_templates/{uid}/archive | 
*WorkflowTemplateServiceApi* | [**clone_workflow_template**](docs/WorkflowTemplateServiceApi.md#clone_workflow_template) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/clone/{name} | 
*WorkflowTemplateServiceApi* | [**clone_workflow_template2**](docs/WorkflowTemplateServiceApi.md#clone_workflow_template2) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/clone/{name}/{version} | 
*WorkflowTemplateServiceApi* | [**create_workflow_template**](docs/WorkflowTemplateServiceApi.md#create_workflow_template) | **POST** /apis/v1beta1/{namespace}/workflow_templates | 
*WorkflowTemplateServiceApi* | [**create_workflow_template_version**](docs/WorkflowTemplateServiceApi.md#create_workflow_template_version) | **POST** /apis/v1beta1/{namespace}/workflow_templates/{workflowTemplate.uid}/versions | 
*WorkflowTemplateServiceApi* | [**generate_workflow_template**](docs/WorkflowTemplateServiceApi.md#generate_workflow_template) | **POST** /apis/v1beta1/{namespace}/workflow_templates/{uid}/generate | Get the generated WorkflowTemplate, applying any modifications based on the content
*WorkflowTemplateServiceApi* | [**get_workflow_template**](docs/WorkflowTemplateServiceApi.md#get_workflow_template) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid} | 
*WorkflowTemplateServiceApi* | [**get_workflow_template2**](docs/WorkflowTemplateServiceApi.md#get_workflow_template2) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions/{version} | 
*WorkflowTemplateServiceApi* | [**list_workflow_template_versions**](docs/WorkflowTemplateServiceApi.md#list_workflow_template_versions) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions | 
*WorkflowTemplateServiceApi* | [**list_workflow_templates**](docs/WorkflowTemplateServiceApi.md#list_workflow_templates) | **GET** /apis/v1beta1/{namespace}/workflow_templates | 
*WorkflowTemplateServiceApi* | [**list_workflow_templates_field**](docs/WorkflowTemplateServiceApi.md#list_workflow_templates_field) | **GET** /apis/v1beta/{namespace}/field/workflow_templates/{fieldName} | 
*WorkspaceServiceApi* | [**create_workspace**](docs/WorkspaceServiceApi.md#create_workspace) | **POST** /apis/v1beta1/{namespace}/workspaces | 
*WorkspaceServiceApi* | [**delete_workspace**](docs/WorkspaceServiceApi.md#delete_workspace) | **DELETE** /apis/v1beta1/{namespace}/workspaces/{uid} | 
*WorkspaceServiceApi* | [**get_workspace**](docs/WorkspaceServiceApi.md#get_workspace) | **GET** /apis/v1beta1/{namespace}/workspaces/{uid} | 
*WorkspaceServiceApi* | [**get_workspace_container_logs**](docs/WorkspaceServiceApi.md#get_workspace_container_logs) | **GET** /apis/v1beta1/{namespace}/workspaces/{uid}/containers/{containerName}/logs | 
*WorkspaceServiceApi* | [**get_workspace_statistics_for_namespace**](docs/WorkspaceServiceApi.md#get_workspace_statistics_for_namespace) | **GET** /apis/v1beta1/{namespace}/workspace/statistics | 
*WorkspaceServiceApi* | [**list_workspaces**](docs/WorkspaceServiceApi.md#list_workspaces) | **GET** /apis/v1beta1/{namespace}/workspaces | 
*WorkspaceServiceApi* | [**list_workspaces_field**](docs/WorkspaceServiceApi.md#list_workspaces_field) | **GET** /apis/v1beta/{namespace}/field/workspaces/{fieldName} | 
*WorkspaceServiceApi* | [**pause_workspace**](docs/WorkspaceServiceApi.md#pause_workspace) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid}/pause | 
*WorkspaceServiceApi* | [**resume_workspace**](docs/WorkspaceServiceApi.md#resume_workspace) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid}/resume | 
*WorkspaceServiceApi* | [**retry_last_workspace_action**](docs/WorkspaceServiceApi.md#retry_last_workspace_action) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid}/retry | 
*WorkspaceServiceApi* | [**update_workspace**](docs/WorkspaceServiceApi.md#update_workspace) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid} | 
*WorkspaceServiceApi* | [**update_workspace_status**](docs/WorkspaceServiceApi.md#update_workspace_status) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid}/status | 
*WorkspaceTemplateServiceApi* | [**archive_workspace_template**](docs/WorkspaceTemplateServiceApi.md#archive_workspace_template) | **PUT** /apis/v1beta1/{namespace}/workspace_templates/{uid}/archive | Archives a WorkspaceTemplate
*WorkspaceTemplateServiceApi* | [**create_workspace_template**](docs/WorkspaceTemplateServiceApi.md#create_workspace_template) | **POST** /apis/v1beta1/{namespace}/workspace_templates | Creates a WorkspaceTemplate
*WorkspaceTemplateServiceApi* | [**generate_workspace_template_workflow_template**](docs/WorkspaceTemplateServiceApi.md#generate_workspace_template_workflow_template) | **POST** /apis/v1beta1/{namespace}/workspace_templates/{uid}/workflow_template | Get the generated WorkflowTemplate for a WorkspaceTemplate
*WorkspaceTemplateServiceApi* | [**get_workspace_template**](docs/WorkspaceTemplateServiceApi.md#get_workspace_template) | **GET** /apis/v1beta1/{namespace}/workspace_templates/{uid} | Get a WorkspaceTemplate
*WorkspaceTemplateServiceApi* | [**list_workspace_template_versions**](docs/WorkspaceTemplateServiceApi.md#list_workspace_template_versions) | **GET** /apis/v1beta1/{namespace}/workspace_templates/{uid}/versions | 
*WorkspaceTemplateServiceApi* | [**list_workspace_templates**](docs/WorkspaceTemplateServiceApi.md#list_workspace_templates) | **GET** /apis/v1beta1/{namespace}/workspace_templates | 
*WorkspaceTemplateServiceApi* | [**list_workspace_templates_field**](docs/WorkspaceTemplateServiceApi.md#list_workspace_templates_field) | **GET** /apis/v1beta/{namespace}/field/workspace_templates/{fieldName} | 
*WorkspaceTemplateServiceApi* | [**update_workspace_template**](docs/WorkspaceTemplateServiceApi.md#update_workspace_template) | **PUT** /apis/v1beta1/{namespace}/workspace_templates/{uid} | Updates a WorkspaceTemplate


## Documentation For Models

 - [AddSecretKeyValueResponse](docs/AddSecretKeyValueResponse.md)
 - [AddWorkflowExecutionsMetricsRequest](docs/AddWorkflowExecutionsMetricsRequest.md)
 - [ArchiveWorkflowTemplateResponse](docs/ArchiveWorkflowTemplateResponse.md)
 - [Container](docs/Container.md)
 - [CreateInferenceServiceRequest](docs/CreateInferenceServiceRequest.md)
 - [CreateWorkflowExecutionBody](docs/CreateWorkflowExecutionBody.md)
 - [CreateWorkspaceBody](docs/CreateWorkspaceBody.md)
 - [CronWorkflow](docs/CronWorkflow.md)
 - [CronWorkflowStatisticsReport](docs/CronWorkflowStatisticsReport.md)
 - [DeleteSecretKeyResponse](docs/DeleteSecretKeyResponse.md)
 - [DeleteSecretResponse](docs/DeleteSecretResponse.md)
 - [Env](docs/Env.md)
 - [File](docs/File.md)
 - [GetAccessTokenRequest](docs/GetAccessTokenRequest.md)
 - [GetAccessTokenResponse](docs/GetAccessTokenResponse.md)
 - [GetConfigResponse](docs/GetConfigResponse.md)
 - [GetInferenceServiceResponse](docs/GetInferenceServiceResponse.md)
 - [GetLabelsResponse](docs/GetLabelsResponse.md)
 - [GetNamespaceConfigResponse](docs/GetNamespaceConfigResponse.md)
 - [GetPresignedUrlResponse](docs/GetPresignedUrlResponse.md)
 - [GetWorkflowExecutionMetricsResponse](docs/GetWorkflowExecutionMetricsResponse.md)
 - [GetWorkflowExecutionStatisticsForNamespaceResponse](docs/GetWorkflowExecutionStatisticsForNamespaceResponse.md)
 - [GetWorkspaceStatisticsForNamespaceResponse](docs/GetWorkspaceStatisticsForNamespaceResponse.md)
 - [GoogleProtobufAny](docs/GoogleProtobufAny.md)
 - [GoogleRpcStatus](docs/GoogleRpcStatus.md)
 - [HasServiceResponse](docs/HasServiceResponse.md)
 - [InferenceServiceCondition](docs/InferenceServiceCondition.md)
 - [InferenceServicePredictor](docs/InferenceServicePredictor.md)
 - [InferenceServiceTransformer](docs/InferenceServiceTransformer.md)
 - [IsAuthorized](docs/IsAuthorized.md)
 - [IsAuthorizedResponse](docs/IsAuthorizedResponse.md)
 - [IsValidTokenRequest](docs/IsValidTokenRequest.md)
 - [IsValidTokenResponse](docs/IsValidTokenResponse.md)
 - [KeyValue](docs/KeyValue.md)
 - [Labels](docs/Labels.md)
 - [ListCronWorkflowsResponse](docs/ListCronWorkflowsResponse.md)
 - [ListFilesResponse](docs/ListFilesResponse.md)
 - [ListNamespacesResponse](docs/ListNamespacesResponse.md)
 - [ListSecretsResponse](docs/ListSecretsResponse.md)
 - [ListServicesResponse](docs/ListServicesResponse.md)
 - [ListWorkflowExecutionsFieldResponse](docs/ListWorkflowExecutionsFieldResponse.md)
 - [ListWorkflowExecutionsResponse](docs/ListWorkflowExecutionsResponse.md)
 - [ListWorkflowTemplateVersionsResponse](docs/ListWorkflowTemplateVersionsResponse.md)
 - [ListWorkflowTemplatesFieldResponse](docs/ListWorkflowTemplatesFieldResponse.md)
 - [ListWorkflowTemplatesResponse](docs/ListWorkflowTemplatesResponse.md)
 - [ListWorkspaceResponse](docs/ListWorkspaceResponse.md)
 - [ListWorkspaceTemplateVersionsResponse](docs/ListWorkspaceTemplateVersionsResponse.md)
 - [ListWorkspaceTemplatesFieldResponse](docs/ListWorkspaceTemplatesFieldResponse.md)
 - [ListWorkspaceTemplatesResponse](docs/ListWorkspaceTemplatesResponse.md)
 - [ListWorkspacesFieldResponse](docs/ListWorkspacesFieldResponse.md)
 - [LogEntry](docs/LogEntry.md)
 - [LogStreamResponse](docs/LogStreamResponse.md)
 - [MachineType](docs/MachineType.md)
 - [Metric](docs/Metric.md)
 - [Namespace](docs/Namespace.md)
 - [NodePool](docs/NodePool.md)
 - [NodePoolOption](docs/NodePoolOption.md)
 - [Parameter](docs/Parameter.md)
 - [ParameterOption](docs/ParameterOption.md)
 - [Secret](docs/Secret.md)
 - [SecretExistsResponse](docs/SecretExistsResponse.md)
 - [Service](docs/Service.md)
 - [Statistics](docs/Statistics.md)
 - [StreamResultOfLogStreamResponse](docs/StreamResultOfLogStreamResponse.md)
 - [StreamResultOfWorkflowExecution](docs/StreamResultOfWorkflowExecution.md)
 - [UpdateSecretKeyValueResponse](docs/UpdateSecretKeyValueResponse.md)
 - [UpdateWorkflowExecutionsMetricsRequest](docs/UpdateWorkflowExecutionsMetricsRequest.md)
 - [UpdateWorkspaceBody](docs/UpdateWorkspaceBody.md)
 - [WorkflowExecution](docs/WorkflowExecution.md)
 - [WorkflowExecutionMetadata](docs/WorkflowExecutionMetadata.md)
 - [WorkflowExecutionStatisticReport](docs/WorkflowExecutionStatisticReport.md)
 - [WorkflowExecutionStatus](docs/WorkflowExecutionStatus.md)
 - [WorkflowExecutionsMetricsResponse](docs/WorkflowExecutionsMetricsResponse.md)
 - [WorkflowTemplate](docs/WorkflowTemplate.md)
 - [Workspace](docs/Workspace.md)
 - [WorkspaceComponent](docs/WorkspaceComponent.md)
 - [WorkspaceStatisticReport](docs/WorkspaceStatisticReport.md)
 - [WorkspaceStatus](docs/WorkspaceStatus.md)
 - [WorkspaceTemplate](docs/WorkspaceTemplate.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: authorization
- **Location**: HTTP header


## Author



