import requests

url = 'http://localhost:8888/apis/v1beta1/aleksandr/workflow_executions/a57c6e-5bpcd/pods/a57c6e-5bpcd-2505719024/containers/main/logs'
r = requests.get(url,
    headers={'authorization':'Bearer <token>'},
    stream=True,
    verify=False)
for content in r.iter_lines():
    print(content.decode("utf-8"))