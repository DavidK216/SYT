import talib
import pandas as pd
'''
这块儿封装一些函数用来算传统指标吧
最好是 list进，list出
'''






'''
test
https://zhuanlan.zhihu.com/p/459685310
'''
if __name__ == '__main__':
    data = pd.read_csv('../judev/eth520-1211.csv')
    close = data['Close'].values
    SMA = talib.SMA(close, 5)
    print(SMA)