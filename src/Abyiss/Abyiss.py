import requests

class StatusError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class InvalidApiKey(Exception):
    def __init__(self):
        super.__init__("Invalid API Key")

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
    ## concating the url
    KEY_PRE = '?apiKey='
    VERSION = 'v1/'
    EXCHANGE = 'exchanges/'
    EXSTAT = '/status'
    EXMARKET = '/markets'
    CURRENT_PRICE = '/currentPrice'
    SNAPSHOT = '/snapshot'
    AGG = '/aggregates/'
    LAST_AGG = '/lastAggregate'
    TRADES = '/trades'
    LAST_TRADE = '/lastTrade'
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
    def parse(self, r):
        if not r.status_code == 200:
            if r.status_code == 401:
                raise InvalidApiKey()
            raise StatusError(f'Received status: {r.status_code}', r.status_code)
        return r.json()

    # Reference Data
    def getExchanges(self):
        r = requests.get(self.build_url(self.EXCHANGE))
        return self.parse(r)

    def getExchangeDetails(self, exchange):
        r = requests.get(self.build_url(exchange))
        return self.parse(r)

    def getExchangeStatus(self, exchange):
        r = requests.get(self.build_url(exchange + self.EXSTAT))
        return self.parse(r)

    def getExchangeMarkets(self, exchange):
        r = requests.get(self.build_url(exchange + self.EXMARKET))
        return self.parse(r)

    def getMarketDetails(self, exchange, market):
        r = requests.get(self.build_url(exchange + '/' + market))
        return self.parse(r)

    # Market Data
    def currentPrice(self, exchange, market):
        r = requests.get(self.build_url(exchange + '/' + market + self.CURRENT_PRICE))
        return self.parse(r)

    def snapshot(self, exchange, market):
        r = requests.get(self.build_url(exchange + '/' + market + self.SNAPSHOT))
        return self.parse(r)
    
    def aggregates(self, exchange, market, time, limit = False):
        if not limit: 
            r = requests.get(self.build_url(exchange + '/' + market + self.AGG + time))
        else: 
            r = requests.get(self.build_url_limit(exchange + '/' + market + self.AGG + time, limit))
        return self.parse(r)

    def lastAggregate(self, exchange, market, time):
        r = requests.get(self.build_url(exchange + '/' + market + self.LAST_AGG + '/' + time))
        return self.parse(r)

    def trades(self, exchange, market, limit = False):
        if not limit:
            r = requests.get(self.build_url(exchange + '/' + market + self.TRADES))
        else:
            r = requests.get(self.build_url_limit(exchange + '/' + market + self.TRADES, limit))
        return self.parse(r)

    def lastTrade(self, exchange, market):
        r = requests.get(self.build_url(exchange + '/' + market + self.LAST_TRADE))
        return self.parse(r)

    def quotes(self, exchange, market):
        r = requests.get(self.build_url(exchange + '/' + market + self.QUOTES))
        return self.parse(r)

    def orderBook(self, exchange, market):
        r = requests.get(self.build_url(exchange + '/' + market + self.ORDERS))
        return self.parse(r)

