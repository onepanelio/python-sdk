# onepanel.core.api.WorkflowServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_workflow_execution_statistics**](WorkflowServiceApi.md#add_workflow_execution_statistics) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{name}/statistics | 
[**clone_workflow_execution**](WorkflowServiceApi.md#clone_workflow_execution) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{name} | 
[**create_workflow_execution**](WorkflowServiceApi.md#create_workflow_execution) | **POST** /apis/v1beta1/{namespace}/workflow_executions | 
[**cron_start_workflow_execution_statistic**](WorkflowServiceApi.md#cron_start_workflow_execution_statistic) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{name}/cron_start_statistics | 
[**get_artifact**](WorkflowServiceApi.md#get_artifact) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/artifacts/{key} | 
[**get_workflow_execution**](WorkflowServiceApi.md#get_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name} | 
[**get_workflow_execution_logs**](WorkflowServiceApi.md#get_workflow_execution_logs) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/pods/{podName}/containers/{containerName}/logs | 
[**get_workflow_execution_metrics**](WorkflowServiceApi.md#get_workflow_execution_metrics) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/pods/{podName}/metrics | 
[**list_files**](WorkflowServiceApi.md#list_files) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/files/{path} | 
[**list_workflow_executions**](WorkflowServiceApi.md#list_workflow_executions) | **GET** /apis/v1beta1/{namespace}/workflow_executions | 
[**resubmit_workflow_execution**](WorkflowServiceApi.md#resubmit_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{name}/resubmit | 
[**terminate_workflow_execution**](WorkflowServiceApi.md#terminate_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{name}/terminate | 
[**watch_workflow_execution**](WorkflowServiceApi.md#watch_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/watch | 


# **add_workflow_execution_statistics**
> object add_workflow_execution_statistics(namespace, name, body)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
body = onepanel.core.api.Statistics() # Statistics | 

    try:
        api_response = api_instance.add_workflow_execution_statistics(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->add_workflow_execution_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **body** | [**Statistics**](Statistics.md)|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_workflow_execution**
> WorkflowExecution clone_workflow_execution(namespace, name)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.clone_workflow_execution(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->clone_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow_execution**
> WorkflowExecution create_workflow_execution(namespace, body)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = onepanel.core.api.CreateWorkflowExecutionBody() # CreateWorkflowExecutionBody | 

    try:
        api_response = api_instance.create_workflow_execution(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**CreateWorkflowExecutionBody**](CreateWorkflowExecutionBody.md)|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cron_start_workflow_execution_statistic**
> object cron_start_workflow_execution_statistic(namespace, name, body)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
body = onepanel.core.api.Statistics() # Statistics | 

    try:
        api_response = api_instance.cron_start_workflow_execution_statistic(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->cron_start_workflow_execution_statistic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **body** | [**Statistics**](Statistics.md)|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact**
> ArtifactResponse get_artifact(namespace, name, key)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
key = 'key_example' # str | 

    try:
        api_response = api_instance.get_artifact(namespace, name, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **key** | **str**|  | 

### Return type

[**ArtifactResponse**](ArtifactResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_execution**
> WorkflowExecution get_workflow_execution(namespace, name)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.get_workflow_execution(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_execution_logs**
> StreamResultOfLogEntry get_workflow_execution_logs(namespace, name, pod_name, container_name)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
pod_name = 'pod_name_example' # str | 
container_name = 'container_name_example' # str | 

    try:
        api_response = api_instance.get_workflow_execution_logs(namespace, name, pod_name, container_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution_logs: %s\n" % e)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_execution_metrics**
> GetWorkflowExecutionMetricsResponse get_workflow_execution_metrics(namespace, name, pod_name)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
pod_name = 'pod_name_example' # str | 

    try:
        api_response = api_instance.get_workflow_execution_metrics(namespace, name, pod_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **pod_name** | **str**|  | 

### Return type

[**GetWorkflowExecutionMetricsResponse**](GetWorkflowExecutionMetricsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> ListFilesResponse list_files(namespace, name, path)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
path = 'path_example' # str | 

    try:
        api_response = api_instance.list_files(namespace, name, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **path** | **str**|  | 

### Return type

[**ListFilesResponse**](ListFilesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_executions**
> ListWorkflowExecutionsResponse list_workflow_executions(namespace, workflow_template_uid=workflow_template_uid, workflow_template_version=workflow_template_version, page_size=page_size, page=page)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_uid = 'workflow_template_uid_example' # str |  (optional)
workflow_template_version = 'workflow_template_version_example' # str |  (optional)
page_size = 56 # int |  (optional)
page = 56 # int |  (optional)

    try:
        api_response = api_instance.list_workflow_executions(namespace, workflow_template_uid=workflow_template_uid, workflow_template_version=workflow_template_version, page_size=page_size, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflow_executions: %s\n" % e)
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

[**ListWorkflowExecutionsResponse**](ListWorkflowExecutionsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resubmit_workflow_execution**
> WorkflowExecution resubmit_workflow_execution(namespace, name)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.resubmit_workflow_execution(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->resubmit_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_workflow_execution**
> object terminate_workflow_execution(namespace, name)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.terminate_workflow_execution(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->terminate_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_workflow_execution**
> StreamResultOfWorkflowExecution watch_workflow_execution(namespace, name)



### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.watch_workflow_execution(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->watch_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**StreamResultOfWorkflowExecution**](StreamResultOfWorkflowExecution.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

