from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'namespace_example' # str |
    uid = 'uid_example' # str |

    try:
        api_response = api_instance.archive_workflow_template(namespace, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->archive_workflow_template: %s\n" % e)