import requests
import urllib


BASE_URI = "http://devtestapi-us-east-2-cx2-5a0fbb3e5a034dabbd5b291bec1210c6-0000.us-east.containers.appdomain.cloud/"
BASE_LIMIT = 20

class Client:

    # |******************************************************************************************************
    # |      ABYISS PUBLIC CLIENT CLASS
    # |******************************************************************************************************
    # |> *  
    # |> *   This is the main interation point that the user will use when using Abyiss' client.
    # |> *   This class contains all of the functions which allows data interation
    # |> *  
    # |******************************************************************************************************
   

    def __init__(self, api_key: str = '', secret_key: str = '', base_api_uri: str = ''):
        self.api_key = api_key
        self.secret_key = secret_key
        if not base_api_uri:
            self.base_api_uri = BASE_URI
        else:
            self.base_api_uri = base_api_uri
        self.session = requests.session()

    def _build_session(self):
        # Internal helper for creating a requests `session` with the correctauthentication handling.

        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })

    #def _create_api_uri(self, *parts: str):
        # Internal helper for creating a valid endpoint
    #    return urljoin(self.base_api_uri. '/'.join(imap(quote, parts)))

    def _handle_response(self, response):
        # Internal helper to ensure the response is valid
        print(f"Status code: {response.status_code}")
        if not str(response.status_code).startswith('2'):
            raise LookupError(f"Response came back with code {response.status_code}")

    def _apply_limit(self, passed_uri:str, limit_qty:int = BASE_LIMIT):
        # Internal helper to pass limit onto each uri
        uri = f"{passed_uri}&limit={limit_qty}"
        return uri

    def _build_request(self, passed_uri: str, *res, **params):
        uri = passed_uri

        for r in res:
            uri = '{}/{}'.format(uri, r)
        if params:
            uri = '{}?{}'.format(uri, urllib.urlencode(params))

        self._build_session()
        response = self.session.get(uri)
        self._handle_response(response)
        return response.json()

    # |*********************************
    # | > MAIN FUNCTIONS
    # |*********************************

    def ping(self):
        uri = (f"{self.base_api_uri}ping")
        print(f"Getting request from {uri}")
        return self._build_request(uri)

    def get_exchanges(self, *res, **params):
        uri = (f"{self.base_api_uri}v1/exchanges")
        #if limit > 0:
        #    uri = self._apply_limit(uri, limit)
        return self._build_request(uri, res, params)