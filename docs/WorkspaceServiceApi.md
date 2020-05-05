# onepanel.core.api.WorkspaceServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspaceServiceApi.md#create_workspace) | **POST** /apis/v1beta1/{namespace}/workspaces | 
[**update_workspace_status**](WorkspaceServiceApi.md#update_workspace_status) | **PUT** /apis/v1beta1/{namespace}/workspaces/{uid}/status | 


# **create_workspace**
> Workspace create_workspace(namespace, body)



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
    api_instance = onepanel.core.api.WorkspaceServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = onepanel.core.api.Workspace() # Workspace | 

    try:
        api_response = api_instance.create_workspace(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspaceServiceApi->create_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**Workspace**](Workspace.md)|  | 

### Return type

[**Workspace**](Workspace.md)

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

# **update_workspace_status**
> object update_workspace_status(namespace, uid, body)



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
    api_instance = onepanel.core.api.WorkspaceServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.WorkspaceStatus() # WorkspaceStatus | 

    try:
        api_response = api_instance.update_workspace_status(namespace, uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspaceServiceApi->update_workspace_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **body** | [**WorkspaceStatus**](WorkspaceStatus.md)|  | 

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

