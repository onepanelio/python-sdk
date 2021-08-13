# onepanel.core.api.ServiceServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service**](ServiceServiceApi.md#get_service) | **GET** /apis/v1beta1/{namespace}/service/{name} | 
[**has_service**](ServiceServiceApi.md#has_service) | **GET** /apis/v1beta/service/{name} | 
[**list_services**](ServiceServiceApi.md#list_services) | **GET** /apis/v1beta1/{namespace}/service | 


# **get_service**
> Service get_service(namespace, name)



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
    api_instance = onepanel.core.api.ServiceServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.get_service(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceServiceApi->get_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**Service**](Service.md)

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

# **has_service**
> HasServiceResponse has_service(name)



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
    api_instance = onepanel.core.api.ServiceServiceApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.has_service(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceServiceApi->has_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**HasServiceResponse**](HasServiceResponse.md)

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

# **list_services**
> ListServicesResponse list_services(namespace, page_size=page_size, page=page)



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
    api_instance = onepanel.core.api.ServiceServiceApi(api_client)
    namespace = 'namespace_example' # str | 
page_size = 56 # int |  (optional)
page = 56 # int |  (optional)

    try:
        api_response = api_instance.list_services(namespace, page_size=page_size, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceServiceApi->list_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**ListServicesResponse**](ListServicesResponse.md)

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

