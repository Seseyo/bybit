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
httpClient = requests.Session()
recv_window = str(5000)
url = "https://api-testnet.bybit.com"  # Testnet endpoint

def HTTP_Request(endPoint,method,payload,Info):
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
    if method == "POST":
        response = httpClient.request(method, url+endPoint, headers=headers, data=payload)
    else:
        response = httpClient.request(method, url+endPoint+"?"+payload, headers=headers)
    # print(response.url)
    # pprint(response.text)
    print(Info + " Elapsed Time : " + str(response.elapsed))
    return response.json()


def genSignature(payload):
    param_str = str(time_stamp) + api_key + recv_window + payload
    hash = hmac.new(bytes(secret_key, "utf-8"), param_str.encode("utf-8"), hashlib.sha256)
    signature = hash.hexdigest()
    return signature

# Create Internal Transfer ( SPOT to UNIFIED )
# endpoint = "/asset/v3/private/transfer/inter-transfer"
# method = "POST"
# transferId = uuid.uuid4()
# params = '{"transferId": "' + str(transferId) +  '","coin": "USDT","amount": "1","from_account_type": "SPOT","to_account_type": "UNIFIED"}'
# HTTP_Request(endpoint, method, params, "InternalTransfer")

# Query Internal Transfer List
# endpoint = "/asset/v3/private/transfer/inter-transfer/list/query"
# method = "GET"
# params = 'coin=USDT'
# HTTP_Request(endpoint, method, params, "InternalTransferList")


endpoint = "/v5/order/create"
method = "POST"
params = {
    "category": "spot",
    "symbol": "BTCUSDT",
    "side": "Buy",
    "orderType": "Limit",
    "qty": "0.1",
    "price": "15600",
    "timeInForce": "PostOnly",
    "orderLinkId": "spot-test-postonly",
    "isLeverage": 0,
    "orderFilter": "Order"
}

result = ','.join([f'{key.capitalize()}: {value}' for key, value in params.items()])
print(result)

# place_order = HTTP_Request(endpoint, method, params, "Place order")
# pprint(place_order)
