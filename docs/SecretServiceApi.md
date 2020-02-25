# core.api.SecretServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_secret_key_value**](SecretServiceApi.md#add_secret_key_value) | **POST** /apis/v1beta1/{namespace}/secrets/{secret.name} | 
[**create_secret**](SecretServiceApi.md#create_secret) | **POST** /apis/v1beta1/{namespace}/secrets | 
[**delete_secret**](SecretServiceApi.md#delete_secret) | **DELETE** /apis/v1beta1/{namespace}/secrets/{name} | 
[**delete_secret_key**](SecretServiceApi.md#delete_secret_key) | **DELETE** /apis/v1beta1/{namespace}/secrets/{secretName}/keys/{key} | 
[**get_secret**](SecretServiceApi.md#get_secret) | **GET** /apis/v1beta1/{namespace}/secrets/{name} | 
[**list_secrets**](SecretServiceApi.md#list_secrets) | **GET** /apis/v1beta1/{namespace}/secrets | 
[**secret_exists**](SecretServiceApi.md#secret_exists) | **GET** /apis/v1beta1/{namespace}/secrets/{name}/exists | 
[**update_secret_key_value**](SecretServiceApi.md#update_secret_key_value) | **PATCH** /apis/v1beta1/{namespace}/secrets/{secret.name} | 


# **add_secret_key_value**
> AddSecretKeyValueResponse add_secret_key_value(namespace, secret_name, body)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
secret_name = 'secret_name_example' # str | 
body = core.api.Secret() # Secret | 

    try:
        api_response = api_instance.add_secret_key_value(namespace, secret_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->add_secret_key_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **secret_name** | **str**|  | 
 **body** | [**Secret**](Secret.md)|  | 

### Return type

[**AddSecretKeyValueResponse**](AddSecretKeyValueResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_secret**
> object create_secret(namespace, body)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = core.api.Secret() # Secret | 

    try:
        api_response = api_instance.create_secret(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->create_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**Secret**](Secret.md)|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret**
> DeleteSecretResponse delete_secret(namespace, name)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.delete_secret(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->delete_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**DeleteSecretResponse**](DeleteSecretResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret_key**
> DeleteSecretKeyResponse delete_secret_key(namespace, secret_name, key)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
secret_name = 'secret_name_example' # str | 
key = 'key_example' # str | 

    try:
        api_response = api_instance.delete_secret_key(namespace, secret_name, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->delete_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **secret_name** | **str**|  | 
 **key** | **str**|  | 

### Return type

[**DeleteSecretKeyResponse**](DeleteSecretKeyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret**
> Secret get_secret(namespace, name)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.get_secret(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->get_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**Secret**](Secret.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secrets**
> ListSecretsResponse list_secrets(namespace)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 

    try:
        api_response = api_instance.list_secrets(namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->list_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 

### Return type

[**ListSecretsResponse**](ListSecretsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_exists**
> SecretExistsResponse secret_exists(namespace, name)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.secret_exists(namespace, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->secret_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**SecretExistsResponse**](SecretExistsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secret_key_value**
> UpdateSecretKeyValueResponse update_secret_key_value(namespace, secret_name, body)



### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = core.api.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
secret_name = 'secret_name_example' # str | 
body = core.api.Secret() # Secret | 

    try:
        api_response = api_instance.update_secret_key_value(namespace, secret_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->update_secret_key_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **secret_name** | **str**|  | 
 **body** | [**Secret**](Secret.md)|  | 

### Return type

[**UpdateSecretKeyValueResponse**](UpdateSecretKeyValueResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

