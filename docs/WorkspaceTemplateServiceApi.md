# onepanel.core.api.WorkspaceTemplateServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_workspace_template**](WorkspaceTemplateServiceApi.md#archive_workspace_template) | **PUT** /apis/v1beta1/{namespace}/workspace_templates/{uid}/archive | Archives a WorkspaceTemplate
[**create_workspace_template**](WorkspaceTemplateServiceApi.md#create_workspace_template) | **POST** /apis/v1beta1/{namespace}/workspace_templates | Creates a WorkspaceTemplate
[**generate_workspace_template_workflow_template**](WorkspaceTemplateServiceApi.md#generate_workspace_template_workflow_template) | **POST** /apis/v1beta1/{namespace}/workspace_templates/{uid}/workflow_template | Get the generated WorkflowTemplate for a WorkspaceTemplate
[**get_workspace_template**](WorkspaceTemplateServiceApi.md#get_workspace_template) | **GET** /apis/v1beta1/{namespace}/workspace_templates/{uid} | Get a WorkspaceTemplate
[**list_workspace_template_versions**](WorkspaceTemplateServiceApi.md#list_workspace_template_versions) | **GET** /apis/v1beta1/{namespace}/workspace_templates/{uid}/versions | 
[**list_workspace_templates**](WorkspaceTemplateServiceApi.md#list_workspace_templates) | **GET** /apis/v1beta1/{namespace}/workspace_templates | 
[**list_workspace_templates_field**](WorkspaceTemplateServiceApi.md#list_workspace_templates_field) | **GET** /apis/v1beta/{namespace}/field/workspace_templates/{fieldName} | 
[**update_workspace_template**](WorkspaceTemplateServiceApi.md#update_workspace_template) | **PUT** /apis/v1beta1/{namespace}/workspace_templates/{uid} | Updates a WorkspaceTemplate


# **archive_workspace_template**
> WorkspaceTemplate archive_workspace_template(namespace, uid)

Archives a WorkspaceTemplate

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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        # Archives a WorkspaceTemplate
        api_response = api_instance.archive_workspace_template(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspaceTemplateServiceApi->archive_workspace_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**WorkspaceTemplate**](WorkspaceTemplate.md)

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

# **create_workspace_template**
> WorkspaceTemplate create_workspace_template(namespace, body)

Creates a WorkspaceTemplate

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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = onepanel.core.api.WorkspaceTemplate() # WorkspaceTemplate | 

    try:
        # Creates a WorkspaceTemplate
        api_response = api_instance.create_workspace_template(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspaceTemplateServiceApi->create_workspace_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**WorkspaceTemplate**](WorkspaceTemplate.md)|  | 

### Return type

[**WorkspaceTemplate**](WorkspaceTemplate.md)

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

# **generate_workspace_template_workflow_template**
> WorkflowTemplate generate_workspace_template_workflow_template(namespace, uid, body)

Get the generated WorkflowTemplate for a WorkspaceTemplate

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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.WorkspaceTemplate() # WorkspaceTemplate | 

    try:
        # Get the generated WorkflowTemplate for a WorkspaceTemplate
        api_response = api_instance.generate_workspace_template_workflow_template(namespace, uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspaceTemplateServiceApi->generate_workspace_template_workflow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **body** | [**WorkspaceTemplate**](WorkspaceTemplate.md)|  | 

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
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_template**
> WorkspaceTemplate get_workspace_template(namespace, uid, version=version)

Get a WorkspaceTemplate

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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
version = 'version_example' # str |  (optional)

    try:
        # Get a WorkspaceTemplate
        api_response = api_instance.get_workspace_template(namespace, uid, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspaceTemplateServiceApi->get_workspace_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**WorkspaceTemplate**](WorkspaceTemplate.md)

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

# **list_workspace_template_versions**
> ListWorkspaceTemplateVersionsResponse list_workspace_template_versions(namespace, uid)



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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.list_workspace_template_versions(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspaceTemplateServiceApi->list_workspace_template_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**ListWorkspaceTemplateVersionsResponse**](ListWorkspaceTemplateVersionsResponse.md)

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

# **list_workspace_templates**
> ListWorkspaceTemplatesResponse list_workspace_templates(namespace, page_size=page_size, page=page, order=order, labels=labels, uid=uid)



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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
page_size = 56 # int |  (optional)
page = 56 # int |  (optional)
order = 'order_example' # str |  (optional)
labels = 'labels_example' # str |  (optional)
uid = 'uid_example' # str |  (optional)

    try:
        api_response = api_instance.list_workspace_templates(namespace, page_size=page_size, page=page, order=order, labels=labels, uid=uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspaceTemplateServiceApi->list_workspace_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **labels** | **str**|  | [optional] 
 **uid** | **str**|  | [optional] 

### Return type

[**ListWorkspaceTemplatesResponse**](ListWorkspaceTemplatesResponse.md)

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

# **list_workspace_templates_field**
> ListWorkspaceTemplatesFieldResponse list_workspace_templates_field(namespace, field_name)



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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
field_name = 'field_name_example' # str | 

    try:
        api_response = api_instance.list_workspace_templates_field(namespace, field_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspaceTemplateServiceApi->list_workspace_templates_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **field_name** | **str**|  | 

### Return type

[**ListWorkspaceTemplatesFieldResponse**](ListWorkspaceTemplatesFieldResponse.md)

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

# **update_workspace_template**
> WorkspaceTemplate update_workspace_template(namespace, uid, body)

Updates a WorkspaceTemplate

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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.WorkspaceTemplate() # WorkspaceTemplate | 

    try:
        # Updates a WorkspaceTemplate
        api_response = api_instance.update_workspace_template(namespace, uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspaceTemplateServiceApi->update_workspace_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **body** | [**WorkspaceTemplate**](WorkspaceTemplate.md)|  | 

### Return type

[**WorkspaceTemplate**](WorkspaceTemplate.md)

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

