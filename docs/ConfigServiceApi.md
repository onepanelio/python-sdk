# onepanel.core.api.ConfigServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config**](ConfigServiceApi.md#get_config) | **GET** /apis/v1beta1/config | 
[**get_namespace_config**](ConfigServiceApi.md#get_namespace_config) | **GET** /apis/v1beta1/{namespace}/config | 


# **get_config**
> GetConfigResponse get_config()



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
    api_instance = onepanel.core.api.ConfigServiceApi(api_client)
    
    try:
        api_response = api_instance.get_config()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigServiceApi->get_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetConfigResponse**](GetConfigResponse.md)

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

# **get_namespace_config**
> GetNamespaceConfigResponse get_namespace_config(namespace)



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
    api_instance = onepanel.core.api.ConfigServiceApi(api_client)
    namespace = 'namespace_example' # str | 

    try:
        api_response = api_instance.get_namespace_config(namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigServiceApi->get_namespace_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 

### Return type

[**GetNamespaceConfigResponse**](GetNamespaceConfigResponse.md)

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

