import pandas as pd
from datetime import datetime,timezone,timedelta
import logging
from data import Data

if __name__ == "__main__":
    data = pd.read_csv('../judev/btc520-1125.csv')
    data = Data(data)
    print(data.pre_dis('Vol', 9, sample_ratio=0.1))
    print(data.kline('Vol', 10))
    logging.warning("xxx")
