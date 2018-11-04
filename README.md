# zebitex-python3
 Python3 wrapper for the webitex API v1. (https://landing.zebitex.com/)

- Documentation: https://doc.zebitex.com/
- OpenAPI specification: https://doc.zebitex.com/v1/swagger.json
- Generate api keys for testing environnement: https://staging.zebitex.com/
- Generate api keys for production environnement: https://zebitex.com/profile/api-tokens 

# Work in progress
|**Public/Private**|**Ressources**                      |**Method in wrapper **|**Developed**|**Documented**|**Tested**|
|:-----------------|:-----------------------------------|:---------------------------|:-:|:-:|:-:|
Public             | `/orders/tickers`                  | `tickers`                  | ✔ | ✘ | ✘ |
Public             | `/orders/ticker_summary/{market}`  | `ticker`                   | ✔ | ✘ | ✘ |
Public             | `/orders/orderbook`                | `orderbook`                | ✔ | ✘ | ✘ |
Public             | `/orders/trade_history`            | `public_trade_history`     | ✔ | ✘ | ✘ |
Private            | `/funds`                           | `funds`                    | ✔ | ✘ | ✘ |
Private            | `/funds/history`                   | `funding_history`          | ✘ | ✘ | ✘ |
Private            | `/history/account`                 | `account_history`          | ✘ | ✘ | ✘ |
Private            | `/history/orders`                  | `order_history`            | ✘ | ✘ | ✘ |
Private            | `/history/trades`                  | `trade_history`            | ✔ | ✘ | ✘ |
Public             | `/orders/current`                  | `open_order`               | ✔ | ✘ | ✘ |
Public             | `/orders/cancel_all`               | `cancel_all_orders`        | ✔ | ✘ | ✘ |
Public             | `/orders/{id}/cancel`              | `cancel_order`             | ✘ | ✘ | ✘ |
Public             | `/orders`                          | `new_order`                | ✔ | ✘ | ✘ |           | ` `                           
UNKNOW             | `/accounts`                        | `UNKNOW`                   | ✘ | ✘ | ✘ |
UNKNOW             | `/diagrams/history`                | `UNKNOW`                   | ✘ | ✘ | ✘ |
UNKNOW             | `/history/download/{file_name}`    | `UNKNOW`                   | ✘ | ✘ | ✘ |
UNKNOW             | `/orders/day_history`              | `UNKNOW`                   | ✘ | ✘ | ✘ |
UNKNOW             | `/withdrawals`                     | `UNKNOW`                   | ✘ | ✘ | ✘ |
UNKNOW             | `/orders/ticker_summary/{market}`  | `UNKNOW`                   | ✘ | ✘ | ✘ |

# TO DO
- Make doc and test.
- Exception handler.
- Packaging.
