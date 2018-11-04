# zebitex-python3
Python3 wrapper for webitex API v1 (https://landing.zebitex.com/).

I am not associated -- use at your own risk, etc.

Installation
-------------

`pip install git+https://github.com/domble42/zebitex-python3.git`

Getting started
-------------
``` Python
from zebitex import Zebitex, ZebitexError

# instantiate your client
test_env = True # set to False to use in production
my_zebitex = Zebitex("<access key>", "<secret key>", test_env)

# retrieve you assets balances
my_assets_balances = my_zebitex.funds()

# open a new order
#my_zebitex.new_order('ltc',     # quote currency
#                    'btc',      # base currency
#                    'ask',      # order side (bid or ask)
#                    '0.321',    # price
#                    '0.123',    # volume
#                    'ltcbtc',   # market
#                    'limit'     # order type
#                    )

# list open orders
open_orders = my_zebitex.open_orders(page='1', per='11')
print(open_orders)

# cancel an opened order
#order_id = 1234
#cancel_order = my_zebitex.cancel_order(order_id)

# Manage error
try:
    # Another instance
    my_bad_zebitex = Zebitex("<GOOD access key>", "<BAD secret key>", test_env)
except ZebitexError as err:
    # Show details of error
    print("{}".format(err))
```

API Documentation
-------------

- Documentation: https://doc.zebitex.com/
- OpenAPI specification: https://doc.zebitex.com/v1/swagger.json
- Generate api keys for testing environnement: https://staging.zebitex.com/
- Generate api keys for production environnement: https://zebitex.com/profile/api-tokens

API's resources -> Wrapper's methods
------------------------------------

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
