from pybit import usdc_perpetual

import requests
import time
import hashlib
import hmac
import uuid
import datetime
from pprint import pprint

import matplotlib.pyplot as plt

api_key = 'lQfazGAVDo5uTHxAXz'
secret_key = '9Vp2FRFja1xl3LXxhC77NqO6qyD3pNONv78H'
recv_window = str(5000)
base_url = "https://api-testnet.bybit.com"  # Testnet endpoint

httpClient = requests.Session()


def HTTP_Request(end_point, h_method, payload, info):
    global time_stamp
    time_stamp = str(int(time.time() * 10 ** 3))
    signature = genSignature(payload)
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-SIGN-TYPE': '2',
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }
    if h_method == "POST":
        response = httpClient.request(h_method, base_url+end_point, headers=headers, data=payload)
    else:
        response = httpClient.request(h_method, base_url+end_point+"?"+payload, headers=headers)
    # print(response.url)
    # pprint(response.text)
    print(info + " Elapsed Time : " + str(response.elapsed))
    return response.json()


def genSignature(payload):
    param_str = str(time_stamp) + api_key + recv_window + payload
    hash = hmac.new(bytes(secret_key, "utf-8"), param_str.encode("utf-8"), hashlib.sha256)
    signature = hash.hexdigest()
    return signature

params_temp = '{"transferId": "' + str(1) +  '","coin": "USDT","amount": "1","from_account_type": "SPOT","to_account_type": "UNIFIED"}'

endpoint = "/v5/order/create"
h_method = "POST"
params = {
    "category": "linear",
    "symbol": "BTCUSDT",
    "side": "Buy",
    "orderType": "Limit",
    "qty": "0.01",
    "price": "21770",
    "timeInForce": "PostOnly",
    "orderLinkId": "linear-test_1",
    "isLeverage": 0,
    "orderFilter": "Order"
}

result = ','.join([f'"{key}": "{value}"' for key, value in params.items()])
result = '{'+result+'}'
#print(result)
#print(params_temp)
### def HTTP_Request(end_point, h_method, payload, info):

place_order = HTTP_Request(endpoint, h_method, result, "Place order 'linear'")
pprint(place_order)
