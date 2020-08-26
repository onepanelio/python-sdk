# onepanel.core.api.WorkflowTemplateServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_workflow_template**](WorkflowTemplateServiceApi.md#archive_workflow_template) | **PUT** /apis/v1beta1/{namespace}/workflow_templates/{uid}/archive | 
[**clone_workflow_template**](WorkflowTemplateServiceApi.md#clone_workflow_template) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/clone/{name} | 
[**clone_workflow_template2**](WorkflowTemplateServiceApi.md#clone_workflow_template2) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/clone/{name}/{version} | 
[**create_workflow_template**](WorkflowTemplateServiceApi.md#create_workflow_template) | **POST** /apis/v1beta1/{namespace}/workflow_templates | 
[**create_workflow_template_version**](WorkflowTemplateServiceApi.md#create_workflow_template_version) | **POST** /apis/v1beta1/{namespace}/workflow_templates/{workflowTemplate.uid}/versions | 
[**get_workflow_template**](WorkflowTemplateServiceApi.md#get_workflow_template) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid} | 
[**get_workflow_template2**](WorkflowTemplateServiceApi.md#get_workflow_template2) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions/{version} | 
[**list_workflow_template_versions**](WorkflowTemplateServiceApi.md#list_workflow_template_versions) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions | 
[**list_workflow_templates**](WorkflowTemplateServiceApi.md#list_workflow_templates) | **GET** /apis/v1beta1/{namespace}/workflow_templates | 


# **archive_workflow_template**
> ArchiveWorkflowTemplateResponse archive_workflow_template(namespace, uid)



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
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.archive_workflow_template(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowTemplateServiceApi->archive_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**ArchiveWorkflowTemplateResponse**](ArchiveWorkflowTemplateResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_workflow_template**
> WorkflowTemplate clone_workflow_template(namespace, uid, name, version=version)



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
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
name = 'name_example' # str | 
version = 'version_example' # str |  (optional)

    try:
        api_response = api_instance.clone_workflow_template(namespace, uid, name, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowTemplateServiceApi->clone_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **name** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_workflow_template2**
> WorkflowTemplate clone_workflow_template2(namespace, uid, name, version)



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
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
name = 'name_example' # str | 
version = 'version_example' # str | 

    try:
        api_response = api_instance.clone_workflow_template2(namespace, uid, name, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowTemplateServiceApi->clone_workflow_template2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow_template**
> WorkflowTemplate create_workflow_template(namespace, body)



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
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = onepanel.core.api.WorkflowTemplate() # WorkflowTemplate | 

    try:
        api_response = api_instance.create_workflow_template(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowTemplateServiceApi->create_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**WorkflowTemplate**](WorkflowTemplate.md)|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow_template_version**
> WorkflowTemplate create_workflow_template_version(namespace, workflow_template_uid, body)



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
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_uid = 'workflow_template_uid_example' # str | 
body = onepanel.core.api.WorkflowTemplate() # WorkflowTemplate | 

    try:
        api_response = api_instance.create_workflow_template_version(namespace, workflow_template_uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowTemplateServiceApi->create_workflow_template_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **workflow_template_uid** | **str**|  | 
 **body** | [**WorkflowTemplate**](WorkflowTemplate.md)|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_template**
> WorkflowTemplate get_workflow_template(namespace, uid, version=version)



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
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
version = 'version_example' # str |  (optional)

    try:
        api_response = api_instance.get_workflow_template(namespace, uid, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowTemplateServiceApi->get_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_template2**
> WorkflowTemplate get_workflow_template2(namespace, uid, version)



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
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
version = 'version_example' # str | 

    try:
        api_response = api_instance.get_workflow_template2(namespace, uid, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowTemplateServiceApi->get_workflow_template2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**WorkflowTemplate**](WorkflowTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_template_versions**
> ListWorkflowTemplateVersionsResponse list_workflow_template_versions(namespace, uid)



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
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.list_workflow_template_versions(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowTemplateServiceApi->list_workflow_template_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**ListWorkflowTemplateVersionsResponse**](ListWorkflowTemplateVersionsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_templates**
> ListWorkflowTemplatesResponse list_workflow_templates(namespace, page_size=page_size, page=page, labels=labels)



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
        'Bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
page_size = 56 # int |  (optional)
page = 56 # int |  (optional)
labels = 'labels_example' # str |  (optional)

    try:
        api_response = api_instance.list_workflow_templates(namespace, page_size=page_size, page=page, labels=labels)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowTemplateServiceApi->list_workflow_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **labels** | **str**|  | [optional] 

### Return type

[**ListWorkflowTemplatesResponse**](ListWorkflowTemplatesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

