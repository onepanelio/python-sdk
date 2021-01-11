# onepanel.core.api.AuthServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token**](AuthServiceApi.md#get_access_token) | **POST** /apis/v1beta1/auth/get_access_token | 
[**is_authorized**](AuthServiceApi.md#is_authorized) | **POST** /apis/v1beta1/auth | 
[**is_valid_token**](AuthServiceApi.md#is_valid_token) | **POST** /apis/v1beta1/auth/token | 


# **get_access_token**
> GetAccessTokenResponse get_access_token(body)



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
    api_instance = onepanel.core.api.AuthServiceApi(api_client)
    body = onepanel.core.api.GetAccessTokenRequest() # GetAccessTokenRequest | 

    try:
        api_response = api_instance.get_access_token(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthServiceApi->get_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetAccessTokenRequest**](GetAccessTokenRequest.md)|  | 

### Return type

[**GetAccessTokenResponse**](GetAccessTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_authorized**
> IsAuthorizedResponse is_authorized(body)



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
    api_instance = onepanel.core.api.AuthServiceApi(api_client)
    body = onepanel.core.api.IsAuthorized() # IsAuthorized | 

    try:
        api_response = api_instance.is_authorized(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthServiceApi->is_authorized: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IsAuthorized**](IsAuthorized.md)|  | 

### Return type

[**IsAuthorizedResponse**](IsAuthorizedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_valid_token**
> IsValidTokenResponse is_valid_token(body)



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
    api_instance = onepanel.core.api.AuthServiceApi(api_client)
    body = onepanel.core.api.IsValidTokenRequest() # IsValidTokenRequest | 

    try:
        api_response = api_instance.is_valid_token(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthServiceApi->is_valid_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IsValidTokenRequest**](IsValidTokenRequest.md)|  | 

### Return type

[**IsValidTokenResponse**](IsValidTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

