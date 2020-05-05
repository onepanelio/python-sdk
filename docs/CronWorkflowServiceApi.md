# onepanel.core.api.CronWorkflowServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cron_workflow**](CronWorkflowServiceApi.md#create_cron_workflow) | **POST** /apis/v1beta1/{namespace}/cron_workflow | 
[**get_cron_workflow**](CronWorkflowServiceApi.md#get_cron_workflow) | **GET** /apis/v1beta1/{namespace}/cron_workflow/{name} | 
[**list_cron_workflows**](CronWorkflowServiceApi.md#list_cron_workflows) | **GET** /apis/v1beta1/{namespace}/cron_workflows | 
[**list_cron_workflows2**](CronWorkflowServiceApi.md#list_cron_workflows2) | **GET** /apis/v1beta1/{namespace}/cron_workflows/{workflow_template_name} | 
[**terminate_cron_workflow**](CronWorkflowServiceApi.md#terminate_cron_workflow) | **DELETE** /apis/v1beta1/{namespace}/cron_workflows/{name}/terminate | 
[**update_cron_workflow**](CronWorkflowServiceApi.md#update_cron_workflow) | **PUT** /apis/v1beta1/{namespace}/cron_workflow/{name} | 


# **create_cron_workflow**
> CronWorkflow create_cron_workflow(namespace, body)



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
    api_instance = onepanel.core.api.CronWorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = onepanel.core.api.CronWorkflow() # CronWorkflow | 

    try:
        api_response = api_instance.create_cron_workflow(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronWorkflowServiceApi->create_cron_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**CronWorkflow**](CronWorkflow.md)|  | 

### Return type

[**CronWorkflow**](CronWorkflow.md)

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

# **get_cron_workflow**
> CronWorkflow get_cron_workflow(namespace, name)



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
    api_instance = onepanel.core.api.CronWorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.get_cron_workflow(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronWorkflowServiceApi->get_cron_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**CronWorkflow**](CronWorkflow.md)

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

# **list_cron_workflows**
> ListCronWorkflowsResponse list_cron_workflows(namespace, workflow_template_name=workflow_template_name, page_size=page_size, page=page)



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
    api_instance = onepanel.core.api.CronWorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_name = 'workflow_template_name_example' # str |  (optional)
page_size = 56 # int |  (optional)
page = 56 # int |  (optional)

    try:
        api_response = api_instance.list_cron_workflows(namespace, workflow_template_name=workflow_template_name, page_size=page_size, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronWorkflowServiceApi->list_cron_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **workflow_template_name** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**ListCronWorkflowsResponse**](ListCronWorkflowsResponse.md)

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

# **list_cron_workflows2**
> ListCronWorkflowsResponse list_cron_workflows2(namespace, workflow_template_name, page_size=page_size, page=page)



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
    api_instance = onepanel.core.api.CronWorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_name = 'workflow_template_name_example' # str | 
page_size = 56 # int |  (optional)
page = 56 # int |  (optional)

    try:
        api_response = api_instance.list_cron_workflows2(namespace, workflow_template_name, page_size=page_size, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronWorkflowServiceApi->list_cron_workflows2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **workflow_template_name** | **str**|  | 
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**ListCronWorkflowsResponse**](ListCronWorkflowsResponse.md)

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

# **terminate_cron_workflow**
> object terminate_cron_workflow(namespace, name)



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
    api_instance = onepanel.core.api.CronWorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.terminate_cron_workflow(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronWorkflowServiceApi->terminate_cron_workflow: %s\n" % e)
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

# **update_cron_workflow**
> CronWorkflow update_cron_workflow(namespace, name, body)



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
    api_instance = onepanel.core.api.CronWorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 
body = onepanel.core.api.CronWorkflow() # CronWorkflow | 

    try:
        api_response = api_instance.update_cron_workflow(namespace, name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronWorkflowServiceApi->update_cron_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 
 **body** | [**CronWorkflow**](CronWorkflow.md)|  | 

### Return type

[**CronWorkflow**](CronWorkflow.md)

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

