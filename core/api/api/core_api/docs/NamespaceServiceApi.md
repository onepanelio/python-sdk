# swagger_client.NamespaceServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_namespaces**](NamespaceServiceApi.md#list_namespaces) | **GET** /apis/v1beta1/namespaces | 


# **list_namespaces**
> ListNamespacesResponse list_namespaces()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NamespaceServiceApi(swagger_client.ApiClient(configuration))

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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

