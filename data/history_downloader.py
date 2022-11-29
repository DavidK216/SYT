import ccxt
import pandas as pd
binance_exchange = ccxt.binance({
    'timeout': 15000,
    'enableRateLimit': True
})

print('交易所id：', binance_exchange.id)
print('交易所名称：', binance_exchange.name)
print('支持的时间频率：', binance_exchange.timeframes)
print('最长等待时间(s)：', binance_exchange.timeout / 1000)
print('访问频率(s)：', binance_exchange.rateLimit / 1000)

binance_markets = binance_exchange.load_markets()
#print(list(binance_markets.keys()))

usdtlist = []
for i in binance_markets:
    if "/USDT" in i:usdtlist.append(i)

usdtlist = usdtlist[:10]
print(usdtlist)

symbol = 'BTC/USDT'
btc_usdt_market = binance_markets[symbol]

since = binance_exchange.parse8601('2022-05-20T00:00:00Z')
end = binance_exchange.milliseconds() - 60 * 1000  # 前一分钟
all_kline_data = []
while since < end:
    symbol = 'BTC/USDT'
    kline_data = binance_exchange.fetch_ohlcv(symbol, since=since, timeframe='1m')
    print(binance_exchange.iso8601(since))
    if len(kline_data):
       # 更新获取时间
        since = kline_data[len(kline_data) - 1][0]
        all_kline_data += kline_data
    else:
        break

all_kline_data_df = pd.DataFrame(all_kline_data)
all_kline_data_df.columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Vol']
all_kline_data_df['Datetime'] = all_kline_data_df['Datetime'].apply(binance_exchange.iso8601)


#all_kline_data_df.to_csv('test.csv',index=False)