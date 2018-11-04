# zebitex-python3
Python3 wrapper for webitex API v1 (https://landing.zebitex.com/).
I am Not associated -- use at your own risk, etc.

Installation
-------------

- for most recent stable release:
`pip install zebitex-python3` # Not implemented yet.

- for bleeding edge development:
`pip install git+https://github.com/domble42/zebitex-python3.git`

API Documentation
-------------

- Documentation: https://doc.zebitex.com/
- OpenAPI specification: https://doc.zebitex.com/v1/swagger.json
- Generate api keys for testing environnement: https://staging.zebitex.com/
- Generate api keys for production environnement: https://zebitex.com/profile/api-tokens

Work in progress
-------------

|**Visiblity** |**Ressources**                     |**Associated method**       |**Developed**|**Documented**|**Tested**|
|:-------------|:----------------------------------|:-------------------------|:-:|:-:|:-:|
PUBLIC         | `/orders/tickers`                 | `tickers()`              | ✔ | ✘ | ✘ |
PUBLIC         | `/orders/ticker_summary/{market}` | `ticker()`               | ✔ | ✘ | ✘ |
PUBLIC         | `/orders/orderbook`               | `orderbook()`            | ✔ | ✘ | ✘ |
PUBLIC         | `/orders/trade_history`           | `public_trade_history()` | ✔ | ✘ | ✘ |
PRIVATE        | `/funds`                          | `funds()`                | ✔ | ✘ | ✘ |
PRIVATE        | `/funds/history`                  | `funding_history()`      | ✘ | ✘ | ✘ |
PRIVATE        | `/history/account`                | `account_history()`      | ✘ | ✘ | ✘ |
PRIVATE        | `/history/orders`                 | `order_history()`        | ✘ | ✘ | ✘ |
PRIVATE        | `/history/trades`                 | `trade_history()`        | ✔ | ✘ | ✘ |
PRIVATE        | `/orders/current`                 | `open_order()`           | ✔ | ✘ | ✘ |
PRIVATE        | `/orders/cancel_all`              | `cancel_all_orders()`    | ✔ | ✘ | ✘ |
PRIVATE        | `/orders/{id}/cancel`             | `cancel_order()`         | ✘ | ✘ | ✘ |
PRIVATE        | `/orders`                         | `new_order()`            | ✔ | ✘ | ✘ |
UNKNOW         | `/accounts`                       | `UNKNOW00()`             | ✘ | ✘ | ✘ |
UNKNOW         | `/diagrams/history`               | `UNKNOW01()`             | ✘ | ✘ | ✘ |
UNKNOW         | `/history/download/{file_name}`   | `UNKNOW02()`             | ✘ | ✘ | ✘ |
UNKNOW         | `/orders/day_history`             | `UNKNOW03()`             | ✘ | ✘ | ✘ |
UNKNOW         | `/withdrawals`                    | `UNKNOW04()`             | ✘ | ✘ | ✘ |
UNKNOW         | `/orders/ticker_summary/{market}` | `UNKNOW05()`             | ✘ | ✘ | ✘ |
