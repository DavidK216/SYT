import pandas as pd
import numpy as np
from datetime import datetime,timezone,timedelta
import logging
class Data:
    def __init__(self, df):
        self.data = df

    '''预处理函数-离散化'''
    def pre_dis(self, feature_name, n, sample_ratio=0.1):
        float_list = list(self.data[feature_name].sample(frac=sample_ratio))
        float_list.sort()
        scales = [float_list[int(len(float_list) / (n + 1)) * i] for i in range(1, n + 1)]
        return scales

    '''k线计算'''
    def kline(self, feature_name, n,):
        float_list = list(self.data[feature_name])
        result_list = []
        for i in range(len(float_list)):
            result_list.append(np.mean(float_list[max(0,i-n),i]))
        return result_list

    '''
    单条数据特征计算，对每条数据统计之前存在的特征
    如近30分钟方差，均值
    '''
    def feature_column_get(self, sample_datatime):
        splitdata = self.data[self.data.Datetime < sample_datatime]

        pass

    def label_build(self, sample_datatime, prefer = 'label-10min-4class'):
        def time2str(datetimeA):
            return str(datetimeA.year) + '-' + str(datetimeA.month).zfill(2) + '-' + str(datetimeA.day).zfill(2) + 'T' \
                   + str(datetimeA.hour).zfill(2) \
                   + ':' + str(datetimeA.minute).zfill(2) + ':' + str(datetimeA.second).zfill(2) + '.' + '000Z'

        if prefer == 'label-10min-4class':
            endday = datetime.strptime(sample_datatime, "%Y-%m-%dT%H:%M:%S.%f%z")+ timedelta(minutes=10)
            enddaystr = time2str(endday)
            splitdata = self.data[self.data.Datetime < enddaystr]
            splitdata = splitdata[splitdata.Datetime > sample_datatime]
            openlist = list(splitdata.Open)
            if len(openlist) < 5:
                logging.warning("太短了，细狗")
                return None
            high = max(list(splitdata.High))
            low = min(list(splitdata.High))
            if high-low < (openlist[0]+openlist[9])/500:
                return [0,0,0,1]
            elif high-openlist[0]>openlist[0]/100:
                return [1,0,0,0]
            elif openlist[0]-low>openlist[0]/100:
                return [0,1,0,0]
            else:
                return [0,0,1,0]
        return None

