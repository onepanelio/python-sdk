# core.api.NamespaceServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_namespaces**](NamespaceServiceApi.md#list_namespaces) | **GET** /apis/v1beta1/namespaces | 


# **list_namespaces**
> ListNamespacesResponse list_namespaces()



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
    api_instance = core.api.NamespaceServiceApi(api_client)
    
    try:
        api_response = api_instance.list_namespaces()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NamespaceServiceApi->list_namespaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListNamespacesResponse**](ListNamespacesResponse.md)

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

