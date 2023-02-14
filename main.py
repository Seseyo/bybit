from pybit import spot
from pprint import pprint

session = spot.HTTP(endpoint='https://api-testnet.bybit.com')
info = session.query_symbol()

pprint(info['result'][0])