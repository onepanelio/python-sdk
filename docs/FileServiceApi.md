# onepanel.core.api.FileServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_object_download_presigned_url**](FileServiceApi.md#get_object_download_presigned_url) | **GET** /apis/v1beta1/{namespace}/files/presigned-url/{key} | 
[**list_files**](FileServiceApi.md#list_files) | **GET** /apis/v1beta1/{namespace}/files/list/{path} | 


# **get_object_download_presigned_url**
> GetPresignedUrlResponse get_object_download_presigned_url(namespace, key)



### Example

* Api Key Authentication (Bearer):
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
        'authorization': 'YOUR_ACCESS_TOKEN'
    }
)
configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.FileServiceApi(api_client)
    namespace = 'namespace_example' # str | 
key = 'key_example' # str | 

    try:
        api_response = api_instance.get_object_download_presigned_url(namespace, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->get_object_download_presigned_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **key** | **str**|  | 

### Return type

[**GetPresignedUrlResponse**](GetPresignedUrlResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> ListFilesResponse list_files(namespace, path, page=page, per_page=per_page)



### Example

* Api Key Authentication (Bearer):
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
        'authorization': 'YOUR_ACCESS_TOKEN'
    }
)
configuration.api_key_prefix['authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.FileServiceApi(api_client)
    namespace = 'namespace_example' # str | 
path = 'path_example' # str | 
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

    try:
        api_response = api_instance.list_files(namespace, path, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **path** | **str**|  | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ListFilesResponse**](ListFilesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

