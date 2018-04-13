import requests


BTC_PRICE_URL_coinmarketcap = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=RUB'

def btcprice(msg):
    btc_price_usd, btc_price_rub = get_btc_price()
    msg = 'USD: ' + str(btc_price_usd) + ' | RUB: ' + str(btc_price_rub)
    return (msg)

def get_btc_price():
    r = requests.get(BTC_PRICE_URL_coinmarketcap)
    response_json = r.json()
    usd_price = response_json[0]['price_usd']
    rub_rpice = response_json[0]['price_rub']
    return usd_price, rub_rpice