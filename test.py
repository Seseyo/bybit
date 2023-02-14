# Import pybit and define the HTTP object.
from pybit import HTTP  # supports inverse perp & futures, usdt perp, spot.
from pybit.spot import HTTP
from pprint import pprint

from pybit import inverse_perpetual  # <-- import HTTP & WSS for inverse perp
from pybit import spot  # <-- import HTTP & WSS for spot

# Unauthenticated
session_unauth = inverse_perpetual.HTTP(endpoint="https://api-testnet.bybit.com")

# Authenticated
session_auth = inverse_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com",
    api_key="lQfazGAVDo5uTHxAXz",
    api_secret="9Vp2FRFja1xl3LXxhC77NqO6qyD3pNONv78H"
)

# pprint(session_auth.get_wallet_balance(coin="BTC"))

#pprint(session_unauth.latest_information_for_symbol(symbol="EOSUSD"))

pprint(session_unauth.orderbook(symbol="EOSUSD"))
