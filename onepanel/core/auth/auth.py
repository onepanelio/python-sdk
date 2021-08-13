import os.path
import onepanel.core.api

from onepanel.core.api.rest import ApiException
from onepanel.core.error import InvalidCredentialsException, MissingHostException, MissingTokenException

LOCAL_TOKEN_PATH = '/var/run/secrets/kubernetes.io/serviceaccount/token'


def get_access_token(username=None, token=None, skip_local_check=False, host=None):
    if not skip_local_check and os.path.exists(LOCAL_TOKEN_PATH):
        with open(LOCAL_TOKEN_PATH) as f:
            return f.read()

    if host is None:
        host = os.getenv('ONEPANEL_API_URL')
        if host is None:
            raise MissingHostException()

    if token is None:
        raise MissingTokenException('Token not set and no token found on system')

    configuration = onepanel.core.api.Configuration(host=host)
    configuration.api_key_prefix['authorization'] = 'Bearer'

    with onepanel.core.api.ApiClient(configuration) as api_client:
        try:
            api_instance = onepanel.core.api.AuthServiceApi(api_client)
            body = onepanel.core.api.GetAccessTokenRequest(username=username, token=token)
            api_response = api_instance.get_access_token(body)
            return api_response.access_token
        except ApiException as e:
            if e.status == 400:
                raise InvalidCredentialsException('The provided credentials are invalid')

            raise e