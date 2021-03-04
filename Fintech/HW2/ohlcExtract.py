
# coding: utf-8

import pandas as pd
import numpy as np
import argparse
#data = input("input:")

def load_data(data_path):
    data=pd.read_csv(data_path,encoding='big5',dtype={'成交日期':str,'商品代號':str,'到期月份(週別)':str,'成交時間':int,'成交價格' :float})
    data=data[data.商品代號 == 'TX     ']
    data=data[data['成交時間'] >= 84500]
    data=data[data['成交時間'] <= 134500]
    data=data[data['成交價格'] >= 0]
    return data
def processing(data):
    '''OHLC (open, high, low, close)'''
    data=np.array(data)
    min=999999
    flag=0
    for i in range(len(data)):
        if data[i][2][6] != '/':
            data[i][2] = int(data[i][2])
            if min > data[i][2]:
                   min = data[i][2]
        else:
            data[i][2] = int(9999999)
    for i in range(len(data)):
        if int(data[i][2]) == min:
            if flag == 0:
                op = int(data[i][4])
                lo = int(data[i][4])
                hi = int(data[i][4])
                flag=1
            if hi < int(data[i][4]):
                hi = int(data[i][4])
            if lo > int(data[i][4]):
                lo = int(data[i][4])
            cl = int(data[i][4])
    return (op,hi,lo,cl)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fintech OHLC')
    parser.add_argument('datetime', type=str,help='Path to Load Data')
    opts = parser.parse_args()
    data = load_data(opts.datetime)
    op,hi,lo,cl = processing(data)
    print('%d %d %d %d' %(op,hi,lo,cl))

