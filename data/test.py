import pandas as pd
from datetime import datetime,timezone,timedelta



if __name__ == "__main__":
    data = pd.read_csv('../judev/btc520-1125.csv')
    data2 = data[data.Datetime < "2022-05-20T00:02:00.000Z"]
    ss = '2022-05-20T00:02:00.000Z'

    d = datetime.strptime(ss, "%Y-%m-%dT%H:%M:%S.%f%z")
    d = d + timedelta(minutes=10)
    print(d.day)

    def time2str(datetimeA):

        return str(datetimeA.year)+'-'+str(datetimeA.month).zfill(2)+'-'+str(datetimeA.day).zfill(2)+'T' \
               +str(datetimeA.hour).zfill(2) \
    +':'+str(datetimeA.minute).zfill(2)+':'+str(datetimeA.second).zfill(2)+'.'+'000Z'

    print(data2)
    low = min(list(data2.High))
    print(low)