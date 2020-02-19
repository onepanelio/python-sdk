# core.api.WorkflowServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_workflow_template**](WorkflowServiceApi.md#archive_workflow_template) | **PUT** /apis/v1beta1/{namespace}/workflow_templates/{uid}/archive | 
[**create_workflow**](WorkflowServiceApi.md#create_workflow) | **POST** /apis/v1beta1/{namespace}/workflows | 
[**create_workflow_template**](WorkflowServiceApi.md#create_workflow_template) | **POST** /apis/v1beta1/{namespace}/workflow_templates | 
[**create_workflow_template_version**](WorkflowServiceApi.md#create_workflow_template_version) | **POST** /apis/v1beta1/{namespace}/workflow_templates/{workflowTemplate.uid}/versions | 
[**get_workflow**](WorkflowServiceApi.md#get_workflow) | **GET** /apis/v1beta1/{namespace}/workflows/{name} | 
[**get_workflow_logs**](WorkflowServiceApi.md#get_workflow_logs) | **GET** /apis/v1beta1/{namespace}/workflows/{name}/pods/{podName}/containers/{containerName}/logs | 
[**get_workflow_metrics**](WorkflowServiceApi.md#get_workflow_metrics) | **GET** /apis/v1beta1/{namespace}/workflows/{name}/pods/{podName}/metrics | 
[**get_workflow_template**](WorkflowServiceApi.md#get_workflow_template) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid} | 
[**get_workflow_template2**](WorkflowServiceApi.md#get_workflow_template2) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions/{version} | 
[**list_workflow_template_versions**](WorkflowServiceApi.md#list_workflow_template_versions) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions | 
[**list_workflow_templates**](WorkflowServiceApi.md#list_workflow_templates) | **GET** /apis/v1beta1/{namespace}/workflow_templates | 
[**list_workflows**](WorkflowServiceApi.md#list_workflows) | **GET** /apis/v1beta1/{namespace}/workflows | 
[**resubmit_workflow**](WorkflowServiceApi.md#resubmit_workflow) | **PUT** /apis/v1beta1/{namespace}/workflows/{name}/resubmit | 
[**terminate_workflow**](WorkflowServiceApi.md#terminate_workflow) | **PUT** /apis/v1beta1/{namespace}/workflows/{name}/terminate | 
[**update_workflow_template_version**](WorkflowServiceApi.md#update_workflow_template_version) | **PUT** /apis/v1beta1/{namespace}/workflow_templates/{workflowTemplate.uid}/versions/{workflowTemplate.version} | 
[**watch_workflow**](WorkflowServiceApi.md#watch_workflow) | **GET** /apis/v1beta1/{namespace}/workflows/{name}/watch | 


# **archive_workflow_template**
> ArchiveWorkflowTemplateResponse archive_workflow_template(namespace, uid)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.archive_workflow_template(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->archive_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**ArchiveWorkflowTemplateResponse**](ArchiveWorkflowTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow**
> Workflow create_workflow(namespace, body)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = core.api.Workflow() # Workflow | 

    try:
        api_response = api_instance.create_workflow(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**Workflow**](Workflow.md)|  | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow_template**
> WorkflowTemplate create_workflow_template(namespace, body)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = core.api.WorkflowTemplate() # WorkflowTemplate | 

    try:
        api_response = api_instance.create_workflow_template(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**WorkflowTemplate**](WorkflowTemplate.md)|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow_template_version**
> WorkflowTemplate create_workflow_template_version(namespace, workflow_template_uid, body)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_uid = 'workflow_template_uid_example' # str | 
body = core.api.WorkflowTemplate() # WorkflowTemplate | 

    try:
        api_response = api_instance.create_workflow_template_version(namespace, workflow_template_uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow_template_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **workflow_template_uid** | **str**|  | 
 **body** | [**WorkflowTemplate**](WorkflowTemplate.md)|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow**
> Workflow get_workflow(namespace, name)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.get_workflow(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_logs**
> StreamResultOfLogEntry get_workflow_logs(namespace, name, pod_name, container_name)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
pod_name = 'pod_name_example' # str | 
container_name = 'container_name_example' # str | 

    try:
        api_response = api_instance.get_workflow_logs(namespace, name, pod_name, container_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **pod_name** | **str**|  | 
 **container_name** | **str**|  | 

### Return type

[**StreamResultOfLogEntry**](StreamResultOfLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_metrics**
> GetWorkflowMetricsResponse get_workflow_metrics(namespace, name, pod_name)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
pod_name = 'pod_name_example' # str | 

    try:
        api_response = api_instance.get_workflow_metrics(namespace, name, pod_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **pod_name** | **str**|  | 

### Return type

[**GetWorkflowMetricsResponse**](GetWorkflowMetricsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_template**
> WorkflowTemplate get_workflow_template(namespace, uid, version=version)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
version = 56 # int |  (optional)

    try:
        api_response = api_instance.get_workflow_template(namespace, uid, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **version** | **int**|  | [optional] 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_template2**
> WorkflowTemplate get_workflow_template2(namespace, uid, version)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
version = 56 # int | 

    try:
        api_response = api_instance.get_workflow_template2(namespace, uid, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_template2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_template_versions**
> ListWorkflowTemplateVersionsResponse list_workflow_template_versions(namespace, uid)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.list_workflow_template_versions(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflow_template_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**ListWorkflowTemplateVersionsResponse**](ListWorkflowTemplateVersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_templates**
> ListWorkflowTemplatesResponse list_workflow_templates(namespace)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 

    try:
        api_response = api_instance.list_workflow_templates(namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflow_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 

### Return type

[**ListWorkflowTemplatesResponse**](ListWorkflowTemplatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflows**
> ListWorkflowsResponse list_workflows(namespace, workflow_template_uid=workflow_template_uid, workflow_template_version=workflow_template_version, page_size=page_size, page=page)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_uid = 'workflow_template_uid_example' # str |  (optional)
workflow_template_version = 'workflow_template_version_example' # str |  (optional)
page_size = 56 # int |  (optional)
page = 56 # int |  (optional)

    try:
        api_response = api_instance.list_workflows(namespace, workflow_template_uid=workflow_template_uid, workflow_template_version=workflow_template_version, page_size=page_size, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **workflow_template_uid** | **str**|  | [optional] 
 **workflow_template_version** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**ListWorkflowsResponse**](ListWorkflowsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resubmit_workflow**
> Workflow resubmit_workflow(namespace, name)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.resubmit_workflow(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->resubmit_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_workflow**
> object terminate_workflow(namespace, name)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.terminate_workflow(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->terminate_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow_template_version**
> WorkflowTemplate update_workflow_template_version(namespace, workflow_template_uid, workflow_template_version, body)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_uid = 'workflow_template_uid_example' # str | 
workflow_template_version = 56 # int | 
body = core.api.WorkflowTemplate() # WorkflowTemplate | 

    try:
        api_response = api_instance.update_workflow_template_version(namespace, workflow_template_uid, workflow_template_version, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->update_workflow_template_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **workflow_template_uid** | **str**|  | 
 **workflow_template_version** | **int**|  | 
 **body** | [**WorkflowTemplate**](WorkflowTemplate.md)|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_workflow**
> StreamResultOfWorkflow watch_workflow(namespace, name)



### Example

```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.watch_workflow(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->watch_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**StreamResultOfWorkflow**](StreamResultOfWorkflow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

