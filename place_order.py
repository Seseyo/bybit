# imports block
import os

import yaml
from pprint import pprint

from connection.methods import BybitConnector


# logic block
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

new_conn = BybitConnector(config['platform'],
                          config['api_key'],
                          config['api_secret'],
                          str(5000))

endpoint = "/v5/order/create"
h_method = "POST"
params = {
    "category": "linear",
    "symbol": "BTCUSDT",
    "side": "Buy",
    "orderType": "Limit",
    "qty": "0.01",
    "price": "26641",
    "timeInForce": "PostOnly",
    "orderLinkId": "linear-test_2",
    "isLeverage": 0,
    "orderFilter": "Order"
}

result = '{'+','.join([f'"{key}": "{value}"' for key, value in params.items()])+'}'

place_order = new_conn.http_request(endpoint, h_method, result, "Place order 'linear'")
pprint(place_order)
