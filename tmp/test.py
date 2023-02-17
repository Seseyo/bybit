btc_data = new_conn.http_request("/v5/market/recent-trade", "GET",
                                    params['get_history_btcusdt'],
                                    "History data 'linear'")

btc_points = [{x['time']: x['price']} for x in btc_data['result']['list']]
btc_time = [x['time'] for x in btc_data['result']['list']]
btc_price = [x['price'] for x in btc_data['result']['list']]

eth_data = new_conn.http_request("/v5/market/recent-trade", "GET",
                                    params['get_history_ethusdt'],
                                    "History data 'linear'")

eth_points = [{x['time']: x['price']} for x in eth_data['result']['list']]
eth_time = [x['time'] for x in eth_data['result']['list']]
eth_price = [x['price'] for x in eth_data['result']['list']]

print('btc_time:')
print_time(btc_time[0])
print('eth_time:')
print_time(eth_time[0])

'''
place_order = new_conn.http_request("/v5/order/create", "POST", 
                                    params['place_order'],
                                    "Place order 'linear'")
pprint(place_order)
'''