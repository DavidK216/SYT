## 致力于小容量策略，让温饱无产者小范围财务自由
# 赚点品茶钱


# requirements
## talib  不太好装  
### win10到官网找一个自己装 https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
### mac 先用brew下下来再装
### pandas之类的之后会列出


## 目前的任务
### 项目架构搭建
### 尝试一个简单策略
「模型」：简单mlp 

「样本」：{「fea」:{
历史金融指标;统计指标
};「label」:{「未来10分钟涨跌」:{涨,跌,平,大回撤性波动涨跌}}}

「特征计算」：

第一版：写talib的函数，被样本构造函数调用，构造样本【对齐线上但效率很低，之后再改进】

第二版：离线算特征表，累计计算