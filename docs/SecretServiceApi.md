# openapi_client.SecretServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_secret_key_value**](SecretServiceApi.md#add_secret_key_value) | **POST** /apis/v1beta1/{namespace}/secrets/{secret.name} | 
[**create_secret**](SecretServiceApi.md#create_secret) | **POST** /apis/v1beta1/{namespace}/secrets | 
[**delete_secret**](SecretServiceApi.md#delete_secret) | **DELETE** /apis/v1beta1/{namespace}/secrets/{name} | 
[**delete_secret_key**](SecretServiceApi.md#delete_secret_key) | **DELETE** /apis/v1beta1/{namespace}/secrets/{secret.name} | 
[**get_secret**](SecretServiceApi.md#get_secret) | **GET** /apis/v1beta1/{namespace}/secrets/{name} | 
[**list_secrets**](SecretServiceApi.md#list_secrets) | **GET** /apis/v1beta1/{namespace}/secrets | 
[**secret_exists**](SecretServiceApi.md#secret_exists) | **GET** /apis/v1beta1/{namespace}/secrets/{name}/exists | 
[**update_secret_key_value**](SecretServiceApi.md#update_secret_key_value) | **PATCH** /apis/v1beta1/{namespace}/secrets/{secret.name} | 


# **add_secret_key_value**
> ApiAddSecretKeyValueResponse add_secret_key_value(namespace, secret_name, body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
secret_name = 'secret_name_example' # str | 
body = openapi_client.ApiSecret() # ApiSecret | 

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
 **body** | [**ApiSecret**](ApiSecret.md)|  | 

### Return type

[**ApiAddSecretKeyValueResponse**](ApiAddSecretKeyValueResponse.md)

### Authorization

No authorization required

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

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = openapi_client.ApiSecret() # ApiSecret | 

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
 **body** | [**ApiSecret**](ApiSecret.md)|  | 

### Return type

**object**

### Authorization

No authorization required

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
> ApiDeleteSecretResponse delete_secret(namespace, name)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecretServiceApi(api_client)
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

[**ApiDeleteSecretResponse**](ApiDeleteSecretResponse.md)

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

# **delete_secret_key**
> ApiDeleteSecretKeyResponse delete_secret_key(namespace, secret_name)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
secret_name = 'secret_name_example' # str | 

    try:
        api_response = api_instance.delete_secret_key(namespace, secret_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->delete_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **secret_name** | **str**|  | 

### Return type

[**ApiDeleteSecretKeyResponse**](ApiDeleteSecretKeyResponse.md)

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

# **get_secret**
> ApiSecret get_secret(namespace, name)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecretServiceApi(api_client)
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

[**ApiSecret**](ApiSecret.md)

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

# **list_secrets**
> ApiListSecretsResponse list_secrets(namespace)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecretServiceApi(api_client)
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

[**ApiListSecretsResponse**](ApiListSecretsResponse.md)

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

# **secret_exists**
> ApiSecretExistsResponse secret_exists(namespace, name)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecretServiceApi(api_client)
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

[**ApiSecretExistsResponse**](ApiSecretExistsResponse.md)

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

# **update_secret_key_value**
> ApiUpdateSecretKeyValueResponse update_secret_key_value(namespace, secret_name)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str | 
secret_name = 'secret_name_example' # str | 

    try:
        api_response = api_instance.update_secret_key_value(namespace, secret_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->update_secret_key_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **secret_name** | **str**|  | 

### Return type

[**ApiUpdateSecretKeyValueResponse**](ApiUpdateSecretKeyValueResponse.md)

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

