import pandas as pd



if __name__ == "__main__":
    data = pd.read_csv('../judev/btc520-1125.csv')
    data2 = data[data.Datetime < "2022-05-20T00:02:00.000Z"]
    print(data2)