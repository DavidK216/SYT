import pandas as pd
import numpy as np

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
        for i in range(float_list):
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
        if prefer == 'label-10min-4class':
            splitdata = self.data[self.data.Datetime < sample_datatime]
            if 1:
                return [0,0,0,1]
        return None

