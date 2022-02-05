import pyupbit

#https://github.com/sharebook-kr/pyupbit

# tickers = pyupbit.get_tickers()
# print(tickers)

price = pyupbit.get_current_price("KRW-XRP")
print(price)

# df = pyupbit.get_ohlcv("KRW-BTC")
# df = pyupbit.get_ohlcv("KRW-BTC", interval="day1")
# df = pyupbit.get_ohlcv("KRW-BTC", interval="minute1")
df = pyupbit.get_ohlcv("KRW-BTC", count=5)
print(df)

orderbook = pyupbit.get_orderbook("KRW-BTC")
# print(orderbook)

access_key = "XfxFlIfTtQqE0wPGeTrJu3PlvhaPPEbKlOKkDosx"
secret_key = "kpcZ2syIsPKrx3Sbtuql2x0Ae74jhmxJMsxnxLnR"

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())