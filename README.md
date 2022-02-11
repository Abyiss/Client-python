
# Abyiss Python Client - WebSocket & REST APIs

Python Client for Abyiss Cryptocurrency APIs.

To use our API please sign up for a free account here: [Sign Up](https://www.abyiss.com/signin), and find your API Key in your [Dashboard](https://www.abyiss.com/dashboard).

## Please use our official [Documentation](https://docs.abyiss.com/). It contains all the latest updates.

### We will be adding some of the additional features to this client libary and our API in roughly in this order: 
* **WebSockets** - This will allow you to subscribe to real time cryptocurrency market data from the API.
* **Unified Endpoints** - This will allow you get a unified view of the entire cryptocurrency market.
* **CSV Export** - This will allow you to export the market data to a CSV file.
* **More Support** - Add support for more currencies, exchanges, markets, symbols, timeframes, functions, indicators and more.


If you have any problems with this library, please open an issue request on [Github](https://github.com/Abyiss/Client-python/issues) or for any additional support please email us at [support@abyiss.com](mailto:support@abyiss.com).


# Getting Started

### Install Abyiss Python Library

``` pip install abyiss ```


### Quick Start - Copy & Paste Code 
```python
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


# More Details


### Abyiss Client

```python
apiKey = "(s2nKF1s2S^Xj6(43z6x6VCh18Ao5Qhu@*6" 

# Create an instance of the Abyiss class with your API key
client = Abyiss.Client(apiKey) 
```

* Instance of the Abyiss class with your API key

* Parameters:
  - **apiKey**: String. Your Abyiss API Key

* Returns a 200 status code upon successful query.



## Reference Data


### Get Exchanges

```python
exchanges = client.getExchanges()
```

* Returns an array of all supported exchanges in the form of market objects.

* Parameters:
  - **exchange**: String. Unique exchange identifier used by Abyiss.

* Response Attributes:
  - **name**: String. The official name of the exchange.
  -  **id**: String. Unique exchange identifier used by Abyiss.

* Response Object:
    ```json
    [
        {
            "name":"Binance",
            "id":"binance"
        },
        {
            "name":"Binance US",
            "id":"binanceus"
        },
        {
            "name":"Coinbase Pro",
            "id":"coinbasepro"
        },
        {
            "name":"BitBay",
            "id":"bitbay"
        }
    ]
    ```


### Get Exchange Details

```python
exchangeDetails = client.getExchangeDetails("exchange id")
```

* Returns an object with properties about the exchange.

* Parameters:
  - **exchange id**: String. Unique exchange identifier used by Abyiss.

* Response Attributes:
  - **name**: String. the official name of the exchange.
  - **id**: String. the id of the exchange used within the api routes.
  - **url**: String. the exchange's official website url.
  - **hasTrades**: Boolean. Whether the api can be used to query market trades on the exchange.
  - **hasAggregates**: Boolean. Whether the api can be used to query market candle aggregates on the exchange.
  - **aggregateTimeframes**: Object containing all of the timeframes supported for market candle aggregates.

* Response Object:
    ```json
    {
        "name":"Coinbase Pro",
        "id":"coinbasepro",
        "url":"https://pro.coinbase.com/",
        "hasTrades":true,
        "hasAggregates":true,
        "aggregateTimeframes":
        {
            "1m":60,
            "5m":300,
            "15m":900,
            "1h":3600,
            "6h":21600,
            "1d":86400
        }
    }
    ```


### Get Exchange Status

```python
exchangeStatus = client.getExchangeStatus("exchange id*")
```

* Returns an object with properties that describe an exchange's status.

* Parameters:
  - **exchange id**: String. Unique exchange identifier used by Abyiss.

* Response Attributes:
  - **status**: String. The status of the exchange. 'ok' is good.
  - **updated**: Int. Unix timestamp of last time the exchage's status was updated.

* Response Object:
    ```json
    {
        "status":"ok",
        "updated":1634929487916
    }
    ```



### Get Exchange Markets

```python
exchangeMarkets = client.getExchangeMarkets("exchange id*")
```

* Returns an array of all crypto pair ids on the exchange.

* Parameters:
  - **exchange id**: String. Unique exchange identifier used by Abyiss.

* Response Attributes:
  - **pair id**: String. Unique Crypto Pair identifier used by the exchange.

* Response Object:
    ```json
    [
        "OGN/BTC",
        "REQ/BTC",
        "KEEP/USD",
        "AAVE/USD",
        "SKL/GBP",
        "MIR/EUR",
        "FORTH/EUR",
        "DOT/USDT"
    ]
    ```


### Get Exchange Markets Details

```python
exchangeMarketDetails = client.getMarketDetails("exchange id*", "market id*")
```

* Returns an object with properties about the crypto pair.

* Parameters:
  - **exchange id**: String. Unique exchange identifier used by Abyiss.
  - **market id**: String. Unique Crypto Pair identifier used by the exchange.

* Response Attributes:
  - **exchange**: String. Unique identifier used by Abyiss for the exchange.
  - **symbol**: String. The symbol of the market.
  - **id**: String. Unique identifier used by Abyiss for the market.
  - **active**: Boolean. Whether the market is active on the exchange.
  - **base**: String. The base of the market. eg: The quantity that is bought.
  - **quote**: String. The quote of the market. eg: The currency being compared.
  - **percentage**: Boolean. Whether the taker and maker fee rate is a multiplier or a fixed flat amount.
  - **taker**: Float. Taker fee rate, 0.002 = 0.2%.
  - **maker**: Float. Maker fee rate, 0.0016 = 0.16%.
  - **spot**: String. Exchange type that the market is listed on.

* Response Object:
    ```json
    {
        "exchange":"coinbasepro",
        "symbol":"BTC/USD",
        "id":"BTC-USD",
        "active":true,
        "base":"BTC",
        "quote":"USD",
        "percentage":true,
        "taker":0.005,
        "maker":0.005,
        "type":"spot"
    }
    ```

## Market Data

### Aggregates

```python
aggregates = client.aggregates("exchange id*", "market id*", "aggregate size*", 'limit')
```

* Returns an array of recent aggregate candlesticks of a given aggregate size for a market on an exchange.

* Parameters:
  - **exchange id**: String. Unique exchange identifier used by Abyiss.
  - **market id**: String. Unique Crypto Pair identifier used by the exchange.
  - **aggregate size**: String. Aggregate bar or candlestick time frame. (1m, 5m, 15m, 1h, 6h, 1d)
  - **limit**: String. Optional. Number of results per request. Maximum 500. (default 200)

* Response Attributes:
  - **exchange**: String. Unique identifier used by Abyiss for the exchange.
  - **market**: String. Unique identifier used by Abyiss for the market.
  - **timestamp**: integer. Unix timestamp of the start of the aggregate calculation. Defining the scope.
  - **open**: float. The first, or opening, price of the aggregate's scope.
  - **high**: float. The highest price recorded within the scope of the aggregate.
  - **low**: float. The lowest price recorded within the scope of the aggregate.
  - **close**: float. The last, or closing, price within the aggregate's scope.
  - **volume**: float. The volume within the aggregate's scope.

* Response Object:
    ```json
    {
        "exchange": "coinbasepro",
        "market": "BTC/USD",
        "timestamp": 1639532040000,
        "open": 48080,
        "high": 48111.79,
        "low": 48080,
        "close": 48088.72,
        "volume": 2.55482409
    }
    ```


### Trades

```python
trades = client.trades("exchange id*", "market id*", 'limit')
```
* Returns an array of recent trades that have occurred on an exchange for a crypto pair.

* Parameters:
  - **exchange id**: String. Unique exchange identifier used by Abyiss.
  - **market id**: String. Unique Crypto Pair identifier used by the exchange.
  - **limit**: String. Optional. Number of results per request. Maximum 500. (default 200)

* Response Attributes:
  - **exchange**: String. Unique identifier used by Abyiss for the exchange.
  - **market**: String. Unique identifier used by Abyiss for the market.
  - **id**: String. The exchange specific unique id of the trade.
  - **timestamp**: string. Unix timestamp of the start of the aggregate calculation. Defining the scope.
  - **price**: float. The quote currency price of the market.
  - **size**: float. The quantity traded.
  - **cost**: float. The quote cost: (size * price).
  - **side**: string. Whether the trade was a buy or sell.

* Response Object:
    ```json
    {
        "exchange": "coinbasepro",
        "market": "BTC/USD",
        "id": "251180247",
        "timestamp": "1639534096083",
        "price": 47887.03,
        "size": 0.00013904,
        "cost": 6.6582126511999995,
        "side": "sell"
    }
    ```


### Quotes

```python
quotes = client.quotes("exchange id*", "market id*")
```

* Returns an array of recent quotes that have occurred on an exchange for a crypto pair.

* Parameters:
  - **exchange id**: String. Unique exchange identifier used by Abyiss.
  - **market id**: String. Unique Crypto Pair identifier used by the exchange.

* Response Attributes:
  - **exchange**: String. Unique identifier used by Abyiss for the exchange.
  - **market**: String. Unique identifier used by Abyiss for the market.
  - **bid price**: float. The bid price.
  - **bid size**: float. The bid size.
  - **ask price**: float. The ask price.
  - **ask size**: float. The ask size.
  - **timestamp**: integer. Unix timestamp of the start of the aggregate calculation. Defining the scope.


* Response Object:
    ```json
    {
        "exchange":"coinbasepro",
        "market":"BTC/USD",
        "nonce":14601360013,
        "bids":
        [
            [
                61947.91,
                1.48088
            ],
            [
                61947.9,
                0.5
            ],
            [
                61944.07,
                0.44094
            ]
        ],
        "asks":
        [
            [
                61947.92,
                2.28573
            ],
            [
                61952.89,
                0.11214
            ],
            [
                61952.9,
                0.50224
            ]
        ]
    }
    ```


### Level 2 OrderBook

```python
level2 = client.orderBook("exchange id*", "market id*")
```

* Returns a snapshot of the recent level 2 orderbook for a crypto pair on an exchange.

* Parameters:
  - **exchange id**: String. Unique exchange identifier used by Abyiss.
  - **market id**: String. Unique Crypto Pair identifier used by the exchange.

* Response Attributes:
  - **exchange**: String. Unique identifier used by Abyiss for the exchange.
  - **market**: String. Unique identifier used by Abyiss for the market.
  - **bid price**: float. The bid price.
  - **bid size**: float. The bid size.
  - **ask price**: float. The ask price.
  - **ask size**: float. The ask size.
  - **timestamp**: integer. Unix timestamp of the start of the aggregate calculation. Defining the scope.


* Response Object:
    ```json
    {
        "exchange":"coinbasepro",
        "market":"BTC/USD",
        "nonce":14601360013,
        "bids":
        [
            [
                61947.91,
                1.48088
            ],
            [
                61947.9,
                0.5
            ],
            [
                61944.07,
                0.44094
            ]
        ],
        "asks":
        [
            [
                61947.92,
                2.28573
            ],
            [
                61952.89,
                0.11214
            ],
            [
                61952.9,
                0.50224
            ]
        ]
    }
    ```

