from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining host is optional and default to http://localhost
# openapi_client.configuration.host = "http://localhost"
configuration = openapi_client.Configuration()
configuration.host = "http://localhost:8888"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecretServiceApi(api_client)
    namespace = 'default'  # str |
    secret_name = 'db-user-pass'  # str |
    body = openapi_client.ApiSecret()  # ApiSecret |
    body.data = {"Open": "api"}
    try:
        api_response = api_instance.add_secret_key_value(namespace, secret_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi->add_secret_key_value: %s\n" % e)
