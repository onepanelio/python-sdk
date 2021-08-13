# onepanel.core.api.WorkflowServiceApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_workflow_execution_metrics**](WorkflowServiceApi.md#add_workflow_execution_metrics) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid}/metric | 
[**add_workflow_execution_statistics**](WorkflowServiceApi.md#add_workflow_execution_statistics) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid}/statistics | 
[**clone_workflow_execution**](WorkflowServiceApi.md#clone_workflow_execution) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid} | Clone a Workflow. This is the same as running it again.
[**create_workflow_execution**](WorkflowServiceApi.md#create_workflow_execution) | **POST** /apis/v1beta1/{namespace}/workflow_executions | Creates a Workflow
[**cron_start_workflow_execution_statistic**](WorkflowServiceApi.md#cron_start_workflow_execution_statistic) | **POST** /apis/v1beta1/{namespace}/workflow_executions/{uid}/cron_start_statistics | 
[**get_workflow_execution**](WorkflowServiceApi.md#get_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid} | 
[**get_workflow_execution_logs**](WorkflowServiceApi.md#get_workflow_execution_logs) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/pods/{podName}/containers/{containerName}/logs | 
[**get_workflow_execution_metrics**](WorkflowServiceApi.md#get_workflow_execution_metrics) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/pods/{podName}/metrics | 
[**get_workflow_execution_statistics_for_namespace**](WorkflowServiceApi.md#get_workflow_execution_statistics_for_namespace) | **GET** /apis/v1beta1/{namespace}/workflow_execution/statistics | 
[**list_workflow_executions**](WorkflowServiceApi.md#list_workflow_executions) | **GET** /apis/v1beta1/{namespace}/workflow_executions | 
[**list_workflow_executions_field**](WorkflowServiceApi.md#list_workflow_executions_field) | **GET** /apis/v1beta/{namespace}/field/workflow_executions/{fieldName} | 
[**resubmit_workflow_execution**](WorkflowServiceApi.md#resubmit_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/resubmit | 
[**terminate_workflow_execution**](WorkflowServiceApi.md#terminate_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/terminate | 
[**update_workflow_execution_metrics**](WorkflowServiceApi.md#update_workflow_execution_metrics) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/metric | 
[**update_workflow_execution_status**](WorkflowServiceApi.md#update_workflow_execution_status) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{uid}/status | 
[**watch_workflow_execution**](WorkflowServiceApi.md#watch_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{uid}/watch | 


# **add_workflow_execution_metrics**
> WorkflowExecutionsMetricsResponse add_workflow_execution_metrics(namespace, uid, body)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.AddWorkflowExecutionsMetricsRequest() # AddWorkflowExecutionsMetricsRequest | 

    try:
        api_response = api_instance.add_workflow_execution_metrics(namespace, uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->add_workflow_execution_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **body** | [**AddWorkflowExecutionsMetricsRequest**](AddWorkflowExecutionsMetricsRequest.md)|  | 

### Return type

[**WorkflowExecutionsMetricsResponse**](WorkflowExecutionsMetricsResponse.md)

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

# **add_workflow_execution_statistics**
> object add_workflow_execution_statistics(namespace, uid, body)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.Statistics() # Statistics | 

    try:
        api_response = api_instance.add_workflow_execution_statistics(namespace, uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->add_workflow_execution_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **body** | [**Statistics**](Statistics.md)|  | 

### Return type

**object**

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

# **clone_workflow_execution**
> WorkflowExecution clone_workflow_execution(namespace, uid)

Clone a Workflow. This is the same as running it again.

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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        # Clone a Workflow. This is the same as running it again.
        api_response = api_instance.clone_workflow_execution(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->clone_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

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

# **create_workflow_execution**
> WorkflowExecution create_workflow_execution(namespace, body)

Creates a Workflow

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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
body = onepanel.core.api.CreateWorkflowExecutionBody() # CreateWorkflowExecutionBody | 

    try:
        # Creates a Workflow
        api_response = api_instance.create_workflow_execution(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**CreateWorkflowExecutionBody**](CreateWorkflowExecutionBody.md)|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

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

# **cron_start_workflow_execution_statistic**
> object cron_start_workflow_execution_statistic(namespace, uid, body)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.Statistics() # Statistics | 

    try:
        api_response = api_instance.cron_start_workflow_execution_statistic(namespace, uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->cron_start_workflow_execution_statistic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **body** | [**Statistics**](Statistics.md)|  | 

### Return type

**object**

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

# **get_workflow_execution**
> WorkflowExecution get_workflow_execution(namespace, uid)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.get_workflow_execution(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

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

# **get_workflow_execution_logs**
> StreamResultOfLogStreamResponse get_workflow_execution_logs(namespace, uid, pod_name, container_name)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
pod_name = 'pod_name_example' # str | 
container_name = 'container_name_example' # str | 

    try:
        api_response = api_instance.get_workflow_execution_logs(namespace, uid, pod_name, container_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **pod_name** | **str**|  | 
 **container_name** | **str**|  | 

### Return type

[**StreamResultOfLogStreamResponse**](StreamResultOfLogStreamResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_execution_metrics**
> GetWorkflowExecutionMetricsResponse get_workflow_execution_metrics(namespace, uid, pod_name)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
pod_name = 'pod_name_example' # str | 

    try:
        api_response = api_instance.get_workflow_execution_metrics(namespace, uid, pod_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **pod_name** | **str**|  | 

### Return type

[**GetWorkflowExecutionMetricsResponse**](GetWorkflowExecutionMetricsResponse.md)

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

# **get_workflow_execution_statistics_for_namespace**
> GetWorkflowExecutionStatisticsForNamespaceResponse get_workflow_execution_statistics_for_namespace(namespace)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 

    try:
        api_response = api_instance.get_workflow_execution_statistics_for_namespace(namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution_statistics_for_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 

### Return type

[**GetWorkflowExecutionStatisticsForNamespaceResponse**](GetWorkflowExecutionStatisticsForNamespaceResponse.md)

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

# **list_workflow_executions**
> ListWorkflowExecutionsResponse list_workflow_executions(namespace, workflow_template_uid=workflow_template_uid, workflow_template_version=workflow_template_version, page_size=page_size, page=page, order=order, labels=labels, phase=phase, include_system=include_system)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
workflow_template_uid = 'workflow_template_uid_example' # str |  (optional)
workflow_template_version = 'workflow_template_version_example' # str |  (optional)
page_size = 56 # int |  (optional)
page = 56 # int |  (optional)
order = 'order_example' # str |  (optional)
labels = 'labels_example' # str |  (optional)
phase = 'phase_example' # str |  (optional)
include_system = True # bool |  (optional)

    try:
        api_response = api_instance.list_workflow_executions(namespace, workflow_template_uid=workflow_template_uid, workflow_template_version=workflow_template_version, page_size=page_size, page=page, order=order, labels=labels, phase=phase, include_system=include_system)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflow_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **workflow_template_uid** | **str**|  | [optional] 
 **workflow_template_version** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **labels** | **str**|  | [optional] 
 **phase** | **str**|  | [optional] 
 **include_system** | **bool**|  | [optional] 

### Return type

[**ListWorkflowExecutionsResponse**](ListWorkflowExecutionsResponse.md)

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

# **list_workflow_executions_field**
> ListWorkflowExecutionsFieldResponse list_workflow_executions_field(namespace, field_name)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
field_name = 'field_name_example' # str | 

    try:
        api_response = api_instance.list_workflow_executions_field(namespace, field_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflow_executions_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **field_name** | **str**|  | 

### Return type

[**ListWorkflowExecutionsFieldResponse**](ListWorkflowExecutionsFieldResponse.md)

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

# **resubmit_workflow_execution**
> WorkflowExecution resubmit_workflow_execution(namespace, uid)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.resubmit_workflow_execution(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->resubmit_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**WorkflowExecution**](WorkflowExecution.md)

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

# **terminate_workflow_execution**
> object terminate_workflow_execution(namespace, uid)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.terminate_workflow_execution(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->terminate_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

**object**

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

# **update_workflow_execution_metrics**
> WorkflowExecutionsMetricsResponse update_workflow_execution_metrics(namespace, uid, body)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.UpdateWorkflowExecutionsMetricsRequest() # UpdateWorkflowExecutionsMetricsRequest | 

    try:
        api_response = api_instance.update_workflow_execution_metrics(namespace, uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->update_workflow_execution_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **body** | [**UpdateWorkflowExecutionsMetricsRequest**](UpdateWorkflowExecutionsMetricsRequest.md)|  | 

### Return type

[**WorkflowExecutionsMetricsResponse**](WorkflowExecutionsMetricsResponse.md)

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

# **update_workflow_execution_status**
> object update_workflow_execution_status(namespace, uid, body)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 
body = onepanel.core.api.WorkflowExecutionStatus() # WorkflowExecutionStatus | 

    try:
        api_response = api_instance.update_workflow_execution_status(namespace, uid, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->update_workflow_execution_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 
 **body** | [**WorkflowExecutionStatus**](WorkflowExecutionStatus.md)|  | 

### Return type

**object**

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

# **watch_workflow_execution**
> StreamResultOfWorkflowExecution watch_workflow_execution(namespace, uid)



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
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str | 
uid = 'uid_example' # str | 

    try:
        api_response = api_instance.watch_workflow_execution(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->watch_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**StreamResultOfWorkflowExecution**](StreamResultOfWorkflowExecution.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

