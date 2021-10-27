[![Tests](https://github.com/Abyiss/abyiss-express-deferred-REST/actions/workflows/nodejs.yml/badge.svg?branch=production)](https://github.com/Abyiss/abyiss-express-deferred-REST/actions/workflows/nodejs.yml)

# Abyiss Python Client - WebSocket & REST APIs

Pyton client for the Abyiss Cryptocurrency API.

This API is currently in the beta. As of this writing (10/27/21) the current version is v1.0.6.

While the API is in beta we will offer it as a free service and will not be charging any money. When we transition out of beta we will offer it as a paid service. We suggest signing up for a free account to take advantage of our API and additional offers [Sign Up](https://www.abyiss.com/login) 


#### We will be adding the following additional features to this client libary in roughly in this order: 
* **API Keys** - This will allow you to access the API with a key attached to your free account.
* **WebSockets** - This will allow you to subscribe to real time cryptocurrency market data from the API.
* **pip Package** - This will allow you to install the client as a pip package.
* **Unified Enpoints** - This will allow you get a unified view of the entire cryptocurrency market.
* **CSV Export** - This will allow you to export the market data to a CSV file.
* **More Support** Add support for more currencies, exchanges, markets, symbols, timeframes, functions, indicators and more.

If you have any problems with this libary please open an issue request on [Github](https://github.com/Abyiss/Client-python/issues)

To find more information about Abyiss please visit [Abyiss.com](https://www.abyiss.com/)

For any additional support please email us at [contact@abyiss.com](mailto:contact@abyiss.com)



# Getting Started

This API provides quick access to market data for storage, analysis, visualization, indicator development, algorithmic trading, strategy backtesting, bot programming, and related software engineering.

It is intended to be used by **coders, developers, technically-skilled traders, data-scientists and financial analysts** for powering software.

Currently to ping our API you can use the following endpoint: 

## [169.63.179.247/ping](http://169.63.179.247/ping)


Our base url is **169.63.179.247**

To learn more about our other endpoints please read below:



## Endpoints

### Ping
#### ***/ping*** 
* Returns a 200 status code upon successful query.
* Returns a static object:
  - **ping**: "Hello Abyiss"
* Example Response:
    ```json
    {"ping":"Hello Abyiss"}
    ```

### Cryptocurrency Exchanges

#### ***/v1/exchanges***
* Returns a 200 status code upon successful query.
* Returns an array of all exchanges in the form of market objects that the api offers.
* Response market object properties:
  - **name**: the official name of the exchange.
  -  **id**: the id of the exchange used within the api routes.
* Example Response:
    ```
    /v1/exchanges
    ```
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

#### ***/v1/{exchange id}***
* Returns a 200 status code upon successfuly query.
* Returns an objects with properties about the exchange.
* Response object properties:
  - **name**: the official name of the exchange.
  - **id**: the id of the exchange used within the api routes.
  - **url**: the exchange's official website url.
  - **hasTrades**: a boolean of whether the api can be used to query market trades on the exchange.
  - **hasAggregates**: a boolean of whether the api can be used to query market candle aggregates on the exchange.
  - **aggregateTimeframes**: an object containing all of the timeframes supported for market candle aggregates.
* Example Response:
    ```
    /v1/coinbasepro
    ```
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

#### ***/v1/{exchange id}/status***
* Returns a 200 status code upon successful query.
* Returns an object with properties that describe an exchange's status.
* Response object properties:
  - **status**: The status of the exchange. 'ok' is good.
  - **updated**: Unix timestamp of last time the exchage's status was updated.
* Example Response:
    ```
    /v1/coinbasepro/status
    ```
    ```json
    {
        "status":"ok",
        "updated":1634929487916
    }
    ```

#### ***/v1/{exchange id}/markets***
* Returns a 200 status code upon successful query.
* Returns a list of all market ids on the exchange.
* Example Response:
    ```
    /v1/coinbasepro/markets
    ```
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

#### ***/v1/{exchange id}/{market id}***
* Returns a 200 status code upon successful query.
* Returns an object with properties about the market.
* Response object properties:
  - **exchange**: The exchange id the market is on.
  - **symbol**: The symbol of the market.
  - **active**: Boolean whether the market is active on the exchange.
  - **base**: The base of the market. eg: The quantity that is bought.
  - **quote**: The quote of the market. eg: The currency being compared.
  - **percentage**:
  - **taker**:
  - **maker**:
  - **spot**:
* Example Response:
    ```
    /v1/coinbasepro/BTC-USD
    ```
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

#### ***/v1/{exchange id}/{market id}/trades***
* Returns a 200 status code upon successful query.
* Returns an array of recent trades that have occurred on an exchange for that market.
* Recent trade properties:
  - **exchange**: The exchange id the trade occurred on.
  - **market**: The market id - what was traded.
  - **id**: The -exchange specific- unique id of the trade. Some exchanges do not have this.
  - **timestamp**: The unix timestamp that trade was executed.
  - **price**: The quote currency price of the market.
  - **size**: The quantity traded.
  - **cost**: The quote cost: size * price.
  - **side**: Whether the trade was a buy or sell.
* Example Response:
    ```
    /v1/coinbasepro/BTC-USD/trades
    ```
    ```json
    [
        {
            "exchange":"coinbasepro",
            "market":"BTC/USD",
            "id":"225294919",
            "timestamp":"1634929741281",
            "price":60344.64,
            "size":0.00013204,
            "cost":7.967906265599999,
            "side":"buy"
        },
        {
            "exchange":"coinbasepro",
            "market":"BTC/USD",
            "id":"225294920",
            "timestamp":"1634929741466",
            "price":60344.64,
            "size":0.00004882,
            "cost":2.9460253248,
            "side":"buy"
        },
        {
            "exchange":"coinbasepro",
            "market":"BTC/USD",
            "id":"225294922",
            "timestamp":"1634929741579",
            "price":60347.03,
            "size":0.00994284,
            "cost":600.0208637651999,
            "side":"buy"
        },
        {
            "exchange":"coinbasepro",
            "market":"BTC/USD",
            "id":"225294921",
            "timestamp":"1634929741579",
            "price":60344.64,
            "size":0.00150799,
            "cost":90.99911367360001,
            "side":"buy"
        }
    ]
    ```

#### ***/v1/{exchange id}/{market id}/aggregates/{aggregate size}***
* Returns a 200 status code upon successful query.
* Returns an array of recent aggregate candlesticks for a given aggregate size on a given market on a given exchange.
* aggregate size is exchange-specific and are listed in the endpoint: /v1/{exchange}
* Recent aggregate properties:
  - **exchange**: The exchange id the aggregate was calculated on.
  - **market**: The market id the aggregate was calculated on.
  - **timestamp**: The unix timestamp for the start of the aggregate calculation, which defines the aggregate's scope.
  - **open**: The first, or opening, price of the aggregate's scope.
  - **high**: The highest price recorded within the scope of the aggregate.
  - **low**: The lowest price recorded within the scope of the aggregate.
  - **close**: The last, or closing, price within the aggregate's scope.
  - **volume**: The volume within the aggregate's scope.
* Example Response:
    ```
    /v1/coinbasepro/btc-usd/aggregates/1m
    ```
    ```json
    [
        {
            "exchange":"coinbasepro",
            "market":"BTC/USD",
            "timestamp":1635171720000,
            "open":63217.48,
            "high":63224.51,
            "low":63167.99,
            "close":63182.8,
            "volume":7.6732551
        },
        {
            "exchange":"coinbasepro",
            "market":"BTC/USD",
            "timestamp":1635171780000,
            "open":63182.79,
            "high":63207.06,
            "low":63157.97,
            "close":63181.38,
            "volume":6.05976851
        },
        {
            "exchange":"coinbasepro",
            "market":"BTC/USD",
            "timestamp":1635171840000,
            "open":63176.86,
            "high":63189.6,
            "low":63157.97,
            "close":63161.38,
            "volume":3.70058086
        }
    ]
    ```

### Redirects
#### ***/*** 
- redirects to https://abyiss.com
#### ***/abyiss*** 
- redirects to https://abyiss.com



## Notes about the REST Client