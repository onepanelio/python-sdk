from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = core.api.SecretServiceApi(api_client)
    namespace = 'namespace_example' # str |
    body = core.api.Secret() # Secret |

    try:
        api_response = api_instance.create_secret(namespace, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->create_secret: %s\n" % e)