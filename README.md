# zebitex-python3
 Python3 wrapper for the webitex API v1. (https://landing.zebitex.com/)

- Documentation: https://doc.zebitex.com/
- OpenAPI specification: https://doc.zebitex.com/v1/swagger.json
- Generate api keys for testing environnement: https://staging.zebitex.com/
- Generate api keys for production environnement: https://zebitex.com/profile/api-tokens 

# Work in progress
|**Path**|**Method**|**Developed**|**Documented**|**Tested**|
|:---------------------------------|:---------------------------|:-:|:-:|:-:|
`/orders/tickers`                  | `tickers`                  | ✔ | ✘ | ✘ |
`/orders/ticker_summary/{market}`  | `ticker`                   | ✔ | ✘ | ✘ |
`/orders/orderbook`                | `orderbook`                | ✔ | ✘ | ✘ |
`/orders/trade_history`            | `public_trade_history`     | ✔ | ✘ | ✘ |
`/funds`                           | `funds`                    | ✔ | ✘ | ✘ |
`/history/trades`                  | `trade_history`            | ✔ | ✘ | ✘ |
`/orders/current`                  | `open_order`               | ✔ | ✘ | ✘ |
`/orders/cancel_all`               | `cancel_all_orders`        | ✔ | ✘ | ✘ |
`/orders`                          | `new_order`                | ✔ | ✘ | ✘ |
` `                                | ` `                        |   |   |   |
`/accounts`                        | `UNKNOW`                   | ✘ | ✘ | ✘ |
`/diagrams/history`                | `UNKNOW`                   | ✘ | ✘ | ✘ |
`/funds/history`                   | `UNKNOW`                   | ✘ | ✘ | ✘ |
`/history/account`                 | `UNKNOW`                   | ✘ | ✘ | ✘ |
`/history/orders`                  | `UNKNOW`                   | ✘ | ✘ | ✘ |
`/history/download/{file_name}`    | `UNKNOW`                   | ✘ | ✘ | ✘ |
`/orders/day_history`              | `UNKNOW`                   | ✘ | ✘ | ✘ |
`/orders/{id}/cancel`              | `UNKNOW`                   | ✘ | ✘ | ✘ |
`/withdrawals`                     | `UNKNOW`                   | ✘ | ✘ | ✘ |
`/orders/ticker_summary/{market}`  | `UNKNOW`                   | ✘ | ✘ | ✘ |

# TO DO
- logger
- meta programming.
