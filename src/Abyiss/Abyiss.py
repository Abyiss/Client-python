
import requests



class Client:

    # |******************************************************************************************************
    # |      ABYISS PUBLIC CLIENT CLASS
    # |******************************************************************************************************
    # |> *
    # |> *   This is the main interation point that the user will use when using Abyiss' client.
    # |> *   This class contains all of the functions which allows data interation
    # |> *
    # |******************************************************************************************************

    ## global variables
    BASE_URL = 'https://api.abyiss.com/'
    API_KEY = ''
    BASE_LIMIT = 200
    STATUS_OK = 200
    ## concating the url
    KEY_PRE = '?apiKey='
    VERSION = 'v1/'
    EXCHANGE = 'exchanges/'
    EXSTAT = '/status'
    EXMARKET = '/markets'
    AGG = '/aggregates/'
    TRADES = '/trades'
    QUOTES = '/quotes'
    ORDERS = '/orders'

    # class constructor
    def __init__(self, api_key: str = '', base_api_url: str = ''):
        self.api_key = api_key
        if not base_api_url:
            self.base_api_url = self.BASE_URL
        else:
            self.base_api_url = base_api_url

    # creates the base url
    def build_url(self, mode):
        return self.base_api_url + self.VERSION + mode + self.KEY_PRE + self.api_key

    def build_url_limit(self, mode, l):
        return self.base_api_url + self.VERSION + mode + self.KEY_PRE + self.api_key + '&limit=' + l


    # checks status returned
    def status_OK(self, r):
        if not r.status_code == self.STATUS_OK:
            print("ERROR CODE: ", r.status_code)
            return 0

    # Reference Data
    def getExchanges(self):
        r = requests.get(self.build_url(self.EXCHANGE))
        self.status_OK(r)
        return r.json()

    def getExchangeDetails(self, exchange):
        r = requests.get(self.build_url(exchange))
        self.status_OK(r)
        return r.json()

    def getExchangeStatus(self, exchange):
        r = requests.get(self.build_url(exchange + self.EXSTAT))
        self.status_OK(r)
        return r.json()

    def getExchangeMarkets(self, exchange):
        r = requests.get(self.build_url(exchange + self.EXMARKET))
        self.status_OK(r)
        return r.json()

    def getMarketDetails(self, exchange, market):
        r = requests.get(self.build_url(exchange + '/' + market))
        self.status_OK(r)
        return r.json()

    # Market Data
    def aggregates(self, exchange, market, time, limit):
        r = requests.get(self.build_url_limit(exchange + '/' + market + self.AGG + time, limit))
        self.status_OK(r)
        return r.json()

    def trades(self, exchange, market, limit):
        r = requests.get(self.build_url_limit(exchange + '/' + market + self.TRADES, limit))
        self.status_OK(r)
        return r.json()

    def quotes(self, exchange, market):
        r = requests.get(self.build_url(exchange + '/' + market + self.QUOTES))
        self.status_OK(r)
        return r.json()

    def orderBook(self, exchange, market):
        r = requests.get(self.build_url(exchange + '/' + market + self.ORDERS))
        self.status_OK(r)
        return r.json()

