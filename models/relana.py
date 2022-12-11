import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':

    eth = list(pd.read_csv('../judev/eth520-1211.csv')['Open'])
    btc = list(pd.read_csv('../judev/btc520-1125.csv')['Open'])

    eth = eth[:len(btc)]

    #btc = btc[99 * int(len(btc) / 100):]
    #eth = eth[99 * int(len(eth) / 100):]


    ratio = [b/e for (b,e) in zip(btc,eth)]
    avr = []
    for i in range(len(ratio)):
        if i<20 or i+10>len(ratio):
            avr.append(ratio[i])
            continue
        avr.append(np.mean(np.array(ratio[i-5:i+5])))
    eth = np.array(eth)
    btc = np.array(btc)
    avr = np.array(avr)

    #print(avr)
    dbtc = []
    deth = []
    davr = []
    for i in range(len(btc)):
        if i<20 or i+10>len(btc):continue
        sbtc = btc[i-5:i+5]
        seth = eth[i-5:i+5]
        savr = avr[i-5:i+5]
        dbtc.append(np.var(sbtc / np.mean(sbtc)))
        deth.append(np.var(seth / np.mean(seth)))
        davr.append(np.var(savr / np.mean(savr)))
        #davr.append(np.mean(savr / np.mean(savr)))
    #print(ratio)

    x = [i for i in range(len(ratio))]

    print('btc: ', np.mean(dbtc))
    print('eth: ', np.mean(deth))
    print('ratio: ', np.mean(davr))
    #plt.plot(x, ratio)
    #plt.show()