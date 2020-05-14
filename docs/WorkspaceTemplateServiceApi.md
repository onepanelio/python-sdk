# onepanel.core.api.WorkspaceTemplateServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace_template**](WorkspaceTemplateServiceApi.md#create_workspace_template) | **POST** /apis/v1beta1/{namespace}/workspace_templates | 
[**generate_workspace_template_workflow_template**](WorkspaceTemplateServiceApi.md#generate_workspace_template_workflow_template) | **POST** /apis/v1beta1/{namespace}/workspace_templates/{uid}/workflow_template | 
[**get_workspace_template**](WorkspaceTemplateServiceApi.md#get_workspace_template) | **GET** /apis/v1beta1/{namespace}/workspace_templates/{uid} | 
[**list_workspace_template_versions**](WorkspaceTemplateServiceApi.md#list_workspace_template_versions) | **GET** /apis/v1beta1/{namespace}/workspace_templates/{uid}/versions | 
[**list_workspace_templates**](WorkspaceTemplateServiceApi.md#list_workspace_templates) | **GET** /apis/v1beta1/{namespace}/workspace_templates | 
[**update_workspace_template**](WorkspaceTemplateServiceApi.md#update_workspace_template) | **PUT** /apis/v1beta1/{namespace}/workspace_templates/{uid} | 


# **create_workspace_template**
> WorkspaceTemplate create_workspace_template(namespace, body)



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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = onepanel.core.api.WorkspaceTemplate() # WorkspaceTemplate | 

    try:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_workspace_template_workflow_template**
> WorkflowTemplate generate_workspace_template_workflow_template(namespace, uid, body)



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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.WorkspaceTemplate() # WorkspaceTemplate | 

    try:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_template**
> WorkspaceTemplate get_workspace_template(namespace, uid, version=version)



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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
version = 'version_example' # str |  (optional)

    try:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspace_templates**
> ListWorkspaceTemplatesResponse list_workspace_templates(namespace, page_size=page_size, page=page)



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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
page_size = 56 # int |  (optional)
page = 56 # int |  (optional)

    try:
        api_response = api_instance.list_workspace_templates(namespace, page_size=page_size, page=page)
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

### Return type

[**ListWorkspaceTemplatesResponse**](ListWorkspaceTemplatesResponse.md)

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

# **update_workspace_template**
> WorkspaceTemplate update_workspace_template(namespace, uid, body)



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
    api_instance = onepanel.core.api.WorkspaceTemplateServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.WorkspaceTemplate() # WorkspaceTemplate | 

    try:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

