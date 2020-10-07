# onepanel-sdk
Onepanel API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.13.0
- Package version: v0.13.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/onepanelio/core](https://github.com/onepanelio/core)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

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

# Configure API key authorization: Bearer
configuration = onepanel.core.api.Configuration(
    host = "http://localhost:8888",
    api_key = {
        'authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.AuthServiceApi(api_client)
    body = onepanel.core.api.IsAuthorized() # IsAuthorized | 

    try:
        api_response = api_instance.is_authorized(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthServiceApi->is_authorized: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8888*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthServiceApi* | [**is_authorized**](docs/AuthServiceApi.md#is_authorized) | **POST** /apis/v1beta1/auth | 
*AuthServiceApi* | [**is_valid_token**](docs/AuthServiceApi.md#is_valid_token) | **POST** /apis/v1beta1/auth/token | 
*ConfigServiceApi* | [**get_config**](docs/ConfigServiceApi.md#get_config) | **GET** /apis/v1beta1/config | 
*CronWorkflowServiceApi* | [**create_cron_workflow**](docs/CronWorkflowServiceApi.md#create_cron_workflow) | **POST** /apis/v1beta1/{namespace}/cron_workflow | 
*CronWorkflowServiceApi* | [**delete_cron_workflow**](docs/CronWorkflowServiceApi.md#delete_cron_workflow) | **DELETE** /apis/v1beta1/{namespace}/cron_workflows/{uid} | 
*CronWorkflowServiceApi* | [**get_cron_workflow**](docs/CronWorkflowServiceApi.md#get_cron_workflow) | **GET** /apis/v1beta1/{namespace}/cron_workflow/{uid} | 
*CronWorkflowServiceApi* | [**list_cron_workflows**](docs/CronWorkflowServiceApi.md#list_cron_workflows) | **GET** /apis/v1beta1/{namespace}/cron_workflows | 
*CronWorkflowServiceApi* | [**list_cron_workflows2**](docs/CronWorkflowServiceApi.md#list_cron_workflows2) | **GET** /apis/v1beta1/{namespace}/cron_workflows/{workflow_template_name} | 
*CronWorkflowServiceApi* | [**update_cron_workflow**](docs/CronWorkflowServiceApi.md#update_cron_workflow) | **PUT** /apis/v1beta1/{namespace}/cron_workflow/{uid} | 
*LabelServiceApi* | [**add_labels**](docs/LabelServiceApi.md#add_labels) | **POST** /apis/v1beta1/{namespace}/{resource}/{uid}/labels | 
*LabelServiceApi* | [**delete_label**](docs/LabelServiceApi.md#delete_label) | **DELETE** /apis/v1beta1/{namespace}/{resource}/{uid}/labels/{key} | 
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
*ServiceServiceApi* | [**list_services**](docs/ServiceServiceApi.md#list_services) | **GET** /apis/v1beta1/{namespace}/service | 
*WorkflowServiceApi* | [**add_workflow_execution_statistics**](docs/WorkflowServiceApi.md#add_workflow_execution_statistics) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid}/statistics | 
*WorkflowServiceApi* | [**clone_workflow_execution**](docs/WorkflowServiceApi.md#clone_workflow_execution) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid} | 
*WorkflowServiceApi* | [**create_workflow_execution**](docs/WorkflowServiceApi.md#create_workflow_execution) | **POST** /apis/v1beta1/{namespace}/workflow_executions | 
*WorkflowServiceApi* | [**cron_start_workflow_execution_statistic**](docs/WorkflowServiceApi.md#cron_start_workflow_execution_statistic) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid}/cron_start_statistics | 
*WorkflowServiceApi* | [**get_artifact**](docs/WorkflowServiceApi.md#get_artifact) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/artifacts/{key} | 
*WorkflowServiceApi* | [**get_workflow_execution**](docs/WorkflowServiceApi.md#get_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid} | 
*WorkflowServiceApi* | [**get_workflow_execution_logs**](docs/WorkflowServiceApi.md#get_workflow_execution_logs) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/pods/{podName}/containers/{containerName}/logs | 
*WorkflowServiceApi* | [**get_workflow_execution_metrics**](docs/WorkflowServiceApi.md#get_workflow_execution_metrics) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/pods/{podName}/metrics | 
*WorkflowServiceApi* | [**get_workflow_execution_statistics_for_namespace**](docs/WorkflowServiceApi.md#get_workflow_execution_statistics_for_namespace) | **GET** /apis/v1beta1/{namespace}/workflow_executions/statistics | 
*WorkflowServiceApi* | [**list_files**](docs/WorkflowServiceApi.md#list_files) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/files/{path} | 
*WorkflowServiceApi* | [**list_workflow_executions**](docs/WorkflowServiceApi.md#list_workflow_executions) | **GET** /apis/v1beta1/{namespace}/workflow_executions | 
*WorkflowServiceApi* | [**resubmit_workflow_execution**](docs/WorkflowServiceApi.md#resubmit_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/resubmit | 
*WorkflowServiceApi* | [**terminate_workflow_execution**](docs/WorkflowServiceApi.md#terminate_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/terminate | 
*WorkflowServiceApi* | [**update_workflow_execution_status**](docs/WorkflowServiceApi.md#update_workflow_execution_status) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/status | 
*WorkflowServiceApi* | [**watch_workflow_execution**](docs/WorkflowServiceApi.md#watch_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/watch | 
*WorkflowTemplateServiceApi* | [**archive_workflow_template**](docs/WorkflowTemplateServiceApi.md#archive_workflow_template) | **PUT** /apis/v1beta1/{namespace}/workflow_templates/{uid}/archive | 
*WorkflowTemplateServiceApi* | [**clone_workflow_template**](docs/WorkflowTemplateServiceApi.md#clone_workflow_template) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/clone/{name} | 
*WorkflowTemplateServiceApi* | [**clone_workflow_template2**](docs/WorkflowTemplateServiceApi.md#clone_workflow_template2) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/clone/{name}/{version} | 
*WorkflowTemplateServiceApi* | [**create_workflow_template**](docs/WorkflowTemplateServiceApi.md#create_workflow_template) | **POST** /apis/v1beta1/{namespace}/workflow_templates | 
*WorkflowTemplateServiceApi* | [**create_workflow_template_version**](docs/WorkflowTemplateServiceApi.md#create_workflow_template_version) | **POST** /apis/v1beta1/{namespace}/workflow_templates/{workflowTemplate.uid}/versions | 
*WorkflowTemplateServiceApi* | [**get_workflow_template**](docs/WorkflowTemplateServiceApi.md#get_workflow_template) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid} | 
*WorkflowTemplateServiceApi* | [**get_workflow_template2**](docs/WorkflowTemplateServiceApi.md#get_workflow_template2) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions/{version} | 
*WorkflowTemplateServiceApi* | [**list_workflow_template_versions**](docs/WorkflowTemplateServiceApi.md#list_workflow_template_versions) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions | 
*WorkflowTemplateServiceApi* | [**list_workflow_templates**](docs/WorkflowTemplateServiceApi.md#list_workflow_templates) | **GET** /apis/v1beta1/{namespace}/workflow_templates | 
*WorkspaceServiceApi* | [**create_workspace**](docs/WorkspaceServiceApi.md#create_workspace) | **POST** /apis/v1beta1/{namespace}/workspaces | 
*WorkspaceServiceApi* | [**delete_workspace**](docs/WorkspaceServiceApi.md#delete_workspace) | **DELETE** /apis/v1beta1/{namespace}/workspaces/{uid} | 
*WorkspaceServiceApi* | [**get_workspace**](docs/WorkspaceServiceApi.md#get_workspace) | **GET** /apis/v1beta1/{namespace}/workspaces/{uid} | 
*WorkspaceServiceApi* | [**get_workspace_statistics_for_namespace**](docs/WorkspaceServiceApi.md#get_workspace_statistics_for_namespace) | **GET** /apis/v1beta1/{namespace}/workspace/statistics | 
*WorkspaceServiceApi* | [**list_workspaces**](docs/WorkspaceServiceApi.md#list_workspaces) | **GET** /apis/v1beta1/{namespace}/workspaces | 
*WorkspaceServiceApi* | [**pause_workspace**](docs/WorkspaceServiceApi.md#pause_workspace) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid}/pause | 
*WorkspaceServiceApi* | [**resume_workspace**](docs/WorkspaceServiceApi.md#resume_workspace) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid}/resume | 
*WorkspaceServiceApi* | [**retry_last_workspace_action**](docs/WorkspaceServiceApi.md#retry_last_workspace_action) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid}/retry | 
*WorkspaceServiceApi* | [**update_workspace**](docs/WorkspaceServiceApi.md#update_workspace) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid} | 
*WorkspaceServiceApi* | [**update_workspace_status**](docs/WorkspaceServiceApi.md#update_workspace_status) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid}/status | 
*WorkspaceTemplateServiceApi* | [**archive_workspace_template**](docs/WorkspaceTemplateServiceApi.md#archive_workspace_template) | **PUT** /apis/v1beta1/{namespace}/workspace_templates/{uid}/archive | 
*WorkspaceTemplateServiceApi* | [**create_workspace_template**](docs/WorkspaceTemplateServiceApi.md#create_workspace_template) | **POST** /apis/v1beta1/{namespace}/workspace_templates | 
*WorkspaceTemplateServiceApi* | [**generate_workspace_template_workflow_template**](docs/WorkspaceTemplateServiceApi.md#generate_workspace_template_workflow_template) | **POST** /apis/v1beta1/{namespace}/workspace_templates/{uid}/workflow_template | 
*WorkspaceTemplateServiceApi* | [**get_workspace_template**](docs/WorkspaceTemplateServiceApi.md#get_workspace_template) | **GET** /apis/v1beta1/{namespace}/workspace_templates/{uid} | 
*WorkspaceTemplateServiceApi* | [**list_workspace_template_versions**](docs/WorkspaceTemplateServiceApi.md#list_workspace_template_versions) | **GET** /apis/v1beta1/{namespace}/workspace_templates/{uid}/versions | 
*WorkspaceTemplateServiceApi* | [**list_workspace_templates**](docs/WorkspaceTemplateServiceApi.md#list_workspace_templates) | **GET** /apis/v1beta1/{namespace}/workspace_templates | 
*WorkspaceTemplateServiceApi* | [**update_workspace_template**](docs/WorkspaceTemplateServiceApi.md#update_workspace_template) | **PUT** /apis/v1beta1/{namespace}/workspace_templates/{uid} | 


## Documentation For Models

 - [AddSecretKeyValueResponse](docs/AddSecretKeyValueResponse.md)
 - [ArchiveWorkflowTemplateResponse](docs/ArchiveWorkflowTemplateResponse.md)
 - [ArtifactResponse](docs/ArtifactResponse.md)
 - [CreateWorkflowExecutionBody](docs/CreateWorkflowExecutionBody.md)
 - [CreateWorkspaceBody](docs/CreateWorkspaceBody.md)
 - [CronWorkflow](docs/CronWorkflow.md)
 - [CronWorkflowStatisticsReport](docs/CronWorkflowStatisticsReport.md)
 - [DeleteSecretKeyResponse](docs/DeleteSecretKeyResponse.md)
 - [DeleteSecretResponse](docs/DeleteSecretResponse.md)
 - [File](docs/File.md)
 - [GetConfigResponse](docs/GetConfigResponse.md)
 - [GetLabelsResponse](docs/GetLabelsResponse.md)
 - [GetWorkflowExecutionMetricsResponse](docs/GetWorkflowExecutionMetricsResponse.md)
 - [GetWorkflowExecutionStatisticsForNamespaceResponse](docs/GetWorkflowExecutionStatisticsForNamespaceResponse.md)
 - [GetWorkspaceStatisticsForNamespaceResponse](docs/GetWorkspaceStatisticsForNamespaceResponse.md)
 - [GoogleProtobufAny](docs/GoogleProtobufAny.md)
 - [GrpcGatewayRuntimeError](docs/GrpcGatewayRuntimeError.md)
 - [GrpcGatewayRuntimeStreamError](docs/GrpcGatewayRuntimeStreamError.md)
 - [IsAuthorized](docs/IsAuthorized.md)
 - [IsAuthorizedResponse](docs/IsAuthorizedResponse.md)
 - [IsValidTokenResponse](docs/IsValidTokenResponse.md)
 - [KeyValue](docs/KeyValue.md)
 - [Labels](docs/Labels.md)
 - [ListCronWorkflowsResponse](docs/ListCronWorkflowsResponse.md)
 - [ListFilesResponse](docs/ListFilesResponse.md)
 - [ListNamespacesResponse](docs/ListNamespacesResponse.md)
 - [ListSecretsResponse](docs/ListSecretsResponse.md)
 - [ListServicesResponse](docs/ListServicesResponse.md)
 - [ListWorkflowExecutionsResponse](docs/ListWorkflowExecutionsResponse.md)
 - [ListWorkflowTemplateVersionsResponse](docs/ListWorkflowTemplateVersionsResponse.md)
 - [ListWorkflowTemplatesResponse](docs/ListWorkflowTemplatesResponse.md)
 - [ListWorkspaceResponse](docs/ListWorkspaceResponse.md)
 - [ListWorkspaceTemplateVersionsResponse](docs/ListWorkspaceTemplateVersionsResponse.md)
 - [ListWorkspaceTemplatesResponse](docs/ListWorkspaceTemplatesResponse.md)
 - [LogEntry](docs/LogEntry.md)
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
 - [StreamResultOfLogEntry](docs/StreamResultOfLogEntry.md)
 - [StreamResultOfWorkflowExecution](docs/StreamResultOfWorkflowExecution.md)
 - [TokenWrapper](docs/TokenWrapper.md)
 - [UpdateSecretKeyValueResponse](docs/UpdateSecretKeyValueResponse.md)
 - [UpdateWorkspaceBody](docs/UpdateWorkspaceBody.md)
 - [WorkflowExecution](docs/WorkflowExecution.md)
 - [WorkflowExecutionMetadata](docs/WorkflowExecutionMetadata.md)
 - [WorkflowExecutionStatisticReport](docs/WorkflowExecutionStatisticReport.md)
 - [WorkflowExecutionStatus](docs/WorkflowExecutionStatus.md)
 - [WorkflowTemplate](docs/WorkflowTemplate.md)
 - [Workspace](docs/Workspace.md)
 - [WorkspaceStatisticReport](docs/WorkspaceStatisticReport.md)
 - [WorkspaceStatus](docs/WorkspaceStatus.md)
 - [WorkspaceTemplate](docs/WorkspaceTemplate.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: authorization
- **Location**: HTTP header


## Author




