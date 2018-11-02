#!/usr/bin/env python3

"""

"""

import time
import requests
import json
import hmac
import hashlib

class Zebitex():
    """ A simple wrapper  """

    def __init__(self, access_key, secret_key, is_staging=False):
        self.access_key = access_key
        self.secret_key = secret_key
        self.url = "https://staging.zebitex.com" if is_staging else "https://zebitex.com"

    def debug(self, method, url, params, header, json_payload):
        print("<mode=\"debug\">")
        print("""\tmethod = {}\n\turl = {}\n\tparams = {}\n\theader = {}\n\tjson = {}""".format(method, url, params, header, json_payload))
        print("</mode>")

    def get_signature_payload(self, verb, path, tonce, params):
        """ The signature_payload consist of uppercased HTTP verb, the API path without the host part, the tonce and all the params in JSON form.
        All separated with a vertical slash."""
        json_params = json.dumps(params) if params else "{}"
        payload = "{}|{}|{}|{}".format(verb.upper(), path, tonce, json_params)
        return hmac.new(self.secret_key.encode(), payload.encode(), hashlib.sha256).hexdigest()

    def get_authorization_header(self, verb, path, params):
        """ The Authorization header:
            - access_key - your token access_key
            - signature - a signature_payload HMAC SHA256 signed with your token secret_key
            - tonce - 13 digits timestamp
            - signed_params - a semicolon separated list of the param names submitted and signed in the request            
        """
        tonce = int(time.time()) * 1000
        signature = self.get_signature_payload(verb, path, tonce, params)
        signed_params = ";".join(params.keys()) if params else ""
        authorization_header_format = "ZEBITEX-HMAC-SHA256 access_key={}, signature={}, tonce={}, signed_params={}"
        authorization_header = authorization_header_format.format(self.access_key, signature, tonce, signed_params)
        return {"Authorization" : authorization_header}

    def make_request(self, level, verb, path, params=None):
        user_agent = {"User-Agent": "zebitex-python3 0.0.1 alpha version"}
        authorization_header = {}
        if level == "PRIVATE":
            authorization_header = self.get_authorization_header(verb, path, params)
        if verb == "POST":
            json_payload = json.dumps(params)
            params = None
        else:
            json_payload = True
        url = self.url + path
        headers = {**user_agent, **authorization_header}
        self.debug(verb, url, params, headers, json.dumps(params))
        return requests.request(verb, url, params=params, headers=headers, json=json_payload)

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

    def new_order(self,bid, ask, side, price, amount, market, ord_type):
        query = {"bid":bid, "ask":ask, "side":side, "price":price, "amount":amount, "market":market, "ord_type":ord_type}
        return self.make_request("PRIVATE", "POST", "/api/v1/orders", query)

def test():
    api = Zebitex(access_key="<YOUT ACCESS KEY>", secret_key="<YOUR SECRET KEY>", is_staging=True)
    t = api.open_orders()
    print(t.text)
    return 0

if __name__ == "__main__":
    test()
