# onepanel.core.api.LabelServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_labels**](LabelServiceApi.md#add_labels) | **POST** /apis/v1beta1/{namespace}/{resource}/{uid}/labels | 
[**delete_label**](LabelServiceApi.md#delete_label) | **DELETE** /apis/v1beta1/{namespace}/{resource}/{uid}/labels/{key} | 
[**get_labels**](LabelServiceApi.md#get_labels) | **GET** /apis/v1beta1/{namespace}/{resource}/{uid}/labels | 
[**replace_labels**](LabelServiceApi.md#replace_labels) | **PUT** /apis/v1beta1/{namespace}/{resource}/{uid}/labels | 


# **add_labels**
> GetLabelsResponse add_labels(namespace, resource, uid, body)



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
    api_instance = onepanel.core.api.LabelServiceApi(api_client)
    namespace = 'namespace_example' # str | 
resource = 'resource_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.Labels() # Labels | 

    try:
        api_response = api_instance.add_labels(namespace, resource, uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LabelServiceApi->add_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **resource** | **str**|  | 
 **uid** | **str**|  | 
 **body** | [**Labels**](Labels.md)|  | 

### Return type

[**GetLabelsResponse**](GetLabelsResponse.md)

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

# **delete_label**
> GetLabelsResponse delete_label(namespace, resource, uid, key)



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
    api_instance = onepanel.core.api.LabelServiceApi(api_client)
    namespace = 'namespace_example' # str | 
resource = 'resource_example' # str | 
uid = 'uid_example' # str | 
key = 'key_example' # str | 

    try:
        api_response = api_instance.delete_label(namespace, resource, uid, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LabelServiceApi->delete_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **resource** | **str**|  | 
 **uid** | **str**|  | 
 **key** | **str**|  | 

### Return type

[**GetLabelsResponse**](GetLabelsResponse.md)

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

# **get_labels**
> GetLabelsResponse get_labels(namespace, resource, uid)



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
    api_instance = onepanel.core.api.LabelServiceApi(api_client)
    namespace = 'namespace_example' # str | 
resource = 'resource_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.get_labels(namespace, resource, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LabelServiceApi->get_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **resource** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**GetLabelsResponse**](GetLabelsResponse.md)

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

# **replace_labels**
> GetLabelsResponse replace_labels(namespace, resource, uid, body)



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
    api_instance = onepanel.core.api.LabelServiceApi(api_client)
    namespace = 'namespace_example' # str | 
resource = 'resource_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.Labels() # Labels | 

    try:
        api_response = api_instance.replace_labels(namespace, resource, uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LabelServiceApi->replace_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **resource** | **str**|  | 
 **uid** | **str**|  | 
 **body** | [**Labels**](Labels.md)|  | 

### Return type

[**GetLabelsResponse**](GetLabelsResponse.md)

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

