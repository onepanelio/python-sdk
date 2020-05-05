from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint
import codecs, json

configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IkFjSjAycmxjQ2FOeDVxXzhfQl9haXcxNFFEUElqNDI0TVhTNURjeHF6VzAifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkZWZhdWx0LXRva2VuLXhjNm5yIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImRlZmF1bHQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI5MTczMWY0YS00ZmQ5LTRjYTAtOGU0Yy1jZDcwNzMwNjlhOTAiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06ZGVmYXVsdCJ9.Vt1l7obVw4bRNdT9a6Roql0-QKIOxjDKmgqX6jsfshIAPxKeZcdWBgyo_f2tLPqxwPDTf33_HM92qhq68A-4jnySNgtYTC0TMYFzWYK5VArUx4c5itN2bQ-xucNzaJTULnEiR3y02qYcS89cdBIUORIWTHNdLcbPphGe9THD4KOWHY86-wXyFTgjOhjcbJzrUp89nEHndRa43iTbpyYhgfW407pQ6t93GSbDWjPAbtygCJ5o9Nr1XiVpdCjnaxPDEJXIJJejXJnOCziPqBzP6whtVDCuIsbeZnyijxBostQrwhAHk9-Qz8gUNjTJCI8xD3zeTqAmK1HtxoIat6vERA'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost:8888"
# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.WorkflowServiceApi(api_client)
    
    try:
        api_response = api_instance.watch_workflow_execution("rush", "pytorch-1-4-6g79k", _preload_content=False)
        for chunk in api_response.stream():
            decoded_chunk = chunk.decode("UTF-8").strip()
            if decoded_chunk is not "":
                pprint(json.loads(decoded_chunk))
    except ApiException as e:
        print("Exception when calling NamespaceServiceApi->list_namespaces: %s\n" % e)
