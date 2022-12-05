import talib as tb 
import numpy as np
from talib import MA_Type

##########测试talib函数##########
##########输入的测试数据为100个随机的样本########
close = np.random.random(100)

###最简单的指标: MovingPrice指标，平滑计算一段时间内的价格（平均值）#########
###前29个为NAN，故剔除NAN################################
###接口為輸入的实时数据#################################
def calculateMovingPrice(close):
    output = tb.SMA(close)
    #剔除NaN
    output=output[29:]
    return output

###Bolling bands with triple exponential moving average:（三线移动平均,前七個為nan，故剔除）
###输入的是实时数据#################
def BollingBands(close):
    matype=MA_Type.T3
    upper,middle,lower = tb.BBANDS(close, matype)
    T3=[]
    T3.append(upper[7:])
    T3.append(middle[7:])
    T3.append(lower[7:])
    return T3

####前n个为NaN,其中n表示的是timeperiod的长度######
def Moment(close,timeperiod):
    output=tb.MOM(close, timeperiod)
    output=output[timeperiod:]
    return output
