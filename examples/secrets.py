from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with core.api.ApiClient() as api_client:
    api_client.configuration.host = "http://localhost:8888"

    # Create an instance of the API class
    api_instance = core.api.SecretServiceApi(api_client)
    namespace = 'aleksandr' # str |
    body = core.api.Secret() # Secret |
    body.name = "onepanel-example"
    body.data = {"key1":"value1"}

    try:
        api_response = api_instance.create_secret(namespace, body)
        pprint(api_response)

        api_response = api_instance.get_secret(namespace, body.name)
        pprint(api_response)

        api_response = api_instance.list_secrets(namespace)
        pprint(api_response)

        api_response = api_instance.secret_exists(namespace, body.name)
        pprint(api_response)

        body.data = {"addedkey":"addedkeyvalue"}
        api_response = api_instance.add_secret_key_value(namespace, body.name,body)
        pprint(api_response)
        api_response = api_instance.get_secret(namespace, body.name)
        pprint(api_response)

        body.data = {"key1": "updatedvalue"}
        api_response = api_instance.update_secret_key_value(namespace, body.name,body)
        pprint(api_response)
        api_response = api_instance.get_secret(namespace, body.name)
        pprint(api_response)

        api_response = api_instance.delete_secret_key(namespace, body.name, "key1")
        pprint(api_response)
        api_response = api_instance.get_secret(namespace, body.name)
        pprint(api_response)

        api_response = api_instance.delete_secret(namespace, body.name)
        pprint(api_response)
        api_response = api_instance.list_secrets(namespace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretServiceApi: %s\n" % e)

