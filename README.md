
# Abyiss Python Client - WebSocket & REST APIs

Python Client for Abyiss Cryptocurrency APIs.

To use our API please sign up for a free account here [Sign Up](https://www.abyiss.com/signin) and find your API Key in your [Dashboard](https://www.abyiss.com/dashboard).

### We will be adding some of the additional features to this client libary and our API in roughly in this order: 
* **WebSockets** - This will allow you to subscribe to real time cryptocurrency market data from the API.
* **Unified Endpoints** - This will allow you get a unified view of the entire cryptocurrency market.
* **CSV Export** - This will allow you to export the market data to a CSV file.
* **More Support** - Add support for more currencies, exchanges, markets, symbols, timeframes, functions, indicators and more.


If you have any problems with this library, please open an issue request on [Github](https://github.com/Abyiss/Client-python/issues) or for any additional support please email us at [support@abyiss.com](mailto:support@abyiss.com).


# Getting Started

To learn more about our API check out our [Documentation](https://docs.abyiss.com/) or continue reading below:



#### pip install Abyiss Python Library

``` pip install abyiss ```


```
from Abyiss import Abyiss


apiKey = "YOUR API KEY"" 

client = Abyiss.Client(apiKey) 

exchanges = client.getExchanges()

exchangeDetails = client.getExchangeDetails("coinbasepro")

exchangeStatus = client.getExchangeStatus("coinbasepro")

exchangeMarkets = client.getExchangeMarkets("coinbasepro")

exchangeMarketDetails = client.getMarketDetails("coinbasepro", "BTC-USDT")

aggregates = client.aggregates("coinbasepro", "BTC-USDT", "1h", '300')

trades = client.trades("coinbasepro", "BTC-USDT", '300')

quotes = client.quotes("coinbasepro", "BTC-USDT")

orderbook = client.orderBook("coinbasepro", "BTC-USDT")

```

