from __future__ import print_function
import time
import io
import codecs, json
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
configuration.api_key['authorization'] = ''
configuration.api_key_prefix['authorization'] = 'Bearer'  # Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    api_client.configuration.host = "http://localhost:8888"

    # Create an instance of the API class
    api_instance = core.api.WorkflowServiceApi(api_client)
    namespace = 'aleksandr' # str |
    name = 'a57c6e-67gm2' # str |
    pod_name = 'a57c6e-67gm2-1678814003' # str |

    # try:
    #     reader = codecs.getreader('utf-8')
    #     api_response = api_instance.watch_workflow_execution(namespace, name,  _preload_content=False)
    #     for chunk in api_response.stream():
    #         chunkStr = chunk.decode("UTF-8").strip()  # str |
    #         if chunkStr is not "":
    #             # Pretty print the JSON
    #             pprint(json.loads(chunkStr))
    #
    #     # show authentication
    #     # update md files
    # except ApiException as e:
    #     print("Exception when calling WorkflowServiceApi->watch_workflow_execution: %s\n" % e)

    container_name = 'main' # str |

    try:
        api_response = api_instance.get_workflow_execution_logs(namespace, name, pod_name, container_name, _preload_content=False)
        for chunk in api_response.stream():
            chunkStr = chunk.decode("UTF-8").strip()  # str |
            if chunkStr is not "":
                # Pretty print the JSON
                pprint(json.loads(chunkStr))
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow_execution_logs: %s\n" % e)

    # try:
    #     api_response = api_instance.get_workflow_execution_metrics(namespace, name, pod_name)
    #     pprint(api_response)
    # except ApiException as e:
    #     print("Exception when calling WorkflowServiceApi->get_workflow_execution_metrics: %s\n" % e)