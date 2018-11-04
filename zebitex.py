#!/usr/bin/env python3

"""

"""

import time
import requests
import json
import hmac
import hashlib

class Zebitex():
    """ A simple wrapper
    
    """

    def __init__(self, access_key, secret_key, is_staging=False):
        self.access_key = access_key
        self.secret_key = secret_key
        self.url = "https://staging.zebitex.com" if is_staging else "https://zebitex.com"

    def get_signature_payload(self, verb, path, tonce, params=None):
        """ The signature_payload consist of uppercased HTTP verb, the API path without the host part, the tonce and all the params in JSON form.
        All separated with a vertical slash."""
        json_params = json.dumps(params) if params else "{}"
        payload = "{}|{}|{}|{}".format(verb.upper(), path, str(tonce), json_params.replace(' ', ''))
        signature = hmac.new(self.secret_key.encode(), payload.encode(), hashlib.sha256).hexdigest()
        return (signature)

    def get_authorization_header(self, verb, path, params):
        """ The Authorization header:
            - access_key - your token access_key
            - signature - a signature_payload HMAC SHA256 signed with your token secret_key
            - tonce - 13 digits timestamp
            - signed_params - a semicolon separated list of the param names submitted and signed in the request            
        """
        tonce = int(time.time() * 1000)
        signature = self.get_signature_payload(verb, path, tonce, params)
        signed_params = ";".join(params.keys()) if params else ""
        authorization_header_format = "ZEBITEX-HMAC-SHA256 access_key={}, signature={}, tonce={}, signed_params={}"
        authorization_header = authorization_header_format.format(self.access_key, signature, tonce, signed_params)
        return {"Authorization" : authorization_header}

    def make_request(self, level, verb, path, params=None):
        user_agent = {"User-Agent": "zebitex-python3 0.0.1 alpha version"}
        authorization_header = {}
        params = {k: str(v) for k,v in params.items()} if params else None
        if level == "PRIVATE":
            authorization_header = self.get_authorization_header(verb, path, params)
        url = self.url + path
        headers = {**user_agent, **authorization_header}
        return requests.request(verb, url, params=params, headers=headers, json=True)

    def funds(self):
        return self.make_request("PRIVATE", "GET", "/api/v1/funds")

    def tickers(self):
        return self.make_request("PUBLIC", "GET", "/api/v1/orders/tickers")

    def ticker(self, market):
        return self.make_request("PUBLIC", "GET", "/api/v1/orders/ticker_summary/{}".format(market))

    def orderbook(self, market):
        return self.make_request("PUBLIC", "GET", "/api/v1/orders/orderbook", {"market":market})

    def public_trade_history(self, market):
        return self.make_request("PUBLIC", "GET", "/api/v1/orders/trade_history", {"market":market})

    def open_orders(self, page=1, per=10):
        query = {"page": page, "per": per}
        return self.make_request("PRIVATE", "GET", "/api/v1/orders/current", query)

    def trade_history(self, side, start_date, end_date, page, per):
        query = {"side":side, "start_date":start_date, "end_date":end_date, "page":page, "per":per}
        return self.make_request("PRIVATE", "GET", "/api/v1/history/trades", query)

    def cancel_all_orders(self):
        return self.make_request("PRIVATE", "DELETE", "/api/v1/orders/cancel_all")

    def cancel_order(self, id_order):
        return self.make_request("PRIVATE", "DELETE", "/api/v1/orders/{}/cancel".format(str(id_order)), {"id": str(id_order)})

    def new_order(self, bid, ask, side, price, amount, market, ord_type):
        query = {"bid":bid, "ask":ask, "side":side, "price":price, "amount":amount, "market":market, "ord_type":ord_type}
        return self.make_request("PRIVATE", "POST", "/api/v1/orders", query)

def test():
    """ """
    api = Zebitex("<ACCESS KEY>", "<SECRETE KEY>", True)
    t = api.new_order('ltc', # quote currency
                'btc', # base currency
                'ask', # order side (bid or ask)
                '0.321', # price
                '0.123', # volume
                'ltcbtc', # market
                'limit' # order type
    )
    print(t)
    if str(t) is "200":
        print(t.text)
    t = api.open_orders()
    print(t)
    print(t.text)
    return 0

if __name__ == "__main__":
    test()
