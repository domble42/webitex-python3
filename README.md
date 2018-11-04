# zebitex-python3
 Python3 wrapper for the webitex API v1. (https://landing.zebitex.com/)

- Documentation: https://doc.zebitex.com/
- OpenAPI specification: https://doc.zebitex.com/v1/swagger.json
- Generate api keys for testing environnement: https://staging.zebitex.com/
- Generate api keys for production environnement: https://zebitex.com/profile/api-tokens

# Work in progress
|**Visiblity**   |**Ressources**                     |**Associated method**       |**Developed**|**Documented**|**Tested**|
|:---------------|:----------------------------------|:-------------------------|:-:|:-:|:-:|
PUBLIC           | `/orders/tickers`                 | `tickers()`              | ✔ | ✘ | ✘ |
PUBLIC           | `/orders/ticker_summary/{market}` | `ticker()`               | ✔ | ✘ | ✘ |
PUBLIC           | `/orders/orderbook`               | `orderbook()`            | ✔ | ✘ | ✘ |
PUBLIC           | `/orders/trade_history`           | `public_trade_history()` | ✔ | ✘ | ✘ |
PRIVATE          | `/funds`                          | `funds()`                | ✔ | ✘ | ✘ |
PRIVATE          | `/funds/history`                  | `funding_history()`      | ✘ | ✘ | ✘ |
PRIVATE          | `/history/account`                | `account_history()`      | ✘ | ✘ | ✘ |
PRIVATE          | `/history/orders`                 | `order_history()`        | ✘ | ✘ | ✘ |
PRIVATE          | `/history/trades`                 | `trade_history()`        | ✔ | ✘ | ✘ |
PRIVATE          | `/orders/current`                 | `open_order()`           | ✔ | ✘ | ✘ |
PRIVATE          | `/orders/cancel_all`              | `cancel_all_orders()`    | ✔ | ✘ | ✘ |
PRIVATE          | `/orders/{id}/cancel`             | `cancel_order()`         | ✘ | ✘ | ✘ |
PRIVATE          | `/orders`                         | `new_order()`            | ✔ | ✘ | ✘ |
UNKNOW (private) | `/accounts`                       | `UNKNOW00()`             | ✘ | ✘ | ✘ |
UNKNOW (private) | `/diagrams/history`               | `UNKNOW01()`             | ✘ | ✘ | ✘ |
UNKNOW (private) | `/history/download/{file_name}`   | `UNKNOW02()`             | ✘ | ✘ | ✘ |
UNKNOW (private) | `/orders/day_history`             | `UNKNOW03()`             | ✘ | ✘ | ✘ |
UNKNOW (private) | `/withdrawals`                    | `UNKNOW04()`             | ✘ | ✘ | ✘ |
UNKNOW (private) | `/orders/ticker_summary/{market}` | `UNKNOW05()`             | ✘ | ✘ | ✘ |

# TO DO
- Factoring
- Documentation
- Tests
- Exception handler
- Packaging
- ...
