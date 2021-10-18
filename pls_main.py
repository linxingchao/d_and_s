
from object.dlt import DLT
from object.ssq import SSQ
from object.pls import PLS
from os import path
import csv
from collections import Counter
from bs4 import BeautifulSoup   #引用BeautifulSoup库
import requests                 #引用requests

from itertools import combinations
import time
import pandas



if __name__ == '__main__': 
    pls = PLS(5993)
    pls.search_data_from_net()
    # for i in range(20,21):
    #     print(pls.number_last_appear_theory_times(i,'first'))
    count = 0
    dic = {'first':[],'second':[],'third':[]}
    modes = ['first','second','third']
    for i in range(0,100):
        for mode in modes:
            data1 = pls.search_frency_from_last(i,1,mode)
            data2 = pls.search_frency_from_last(i,2,mode)
            data3 = pls.search_frency_from_last(i,3,mode)
            data4 = pls.search_frency_from_last(i,4,mode)
            data5 = pls.search_frency_from_last(i,5,mode)
            data6 = pls.search_frency_from_last(i,6,mode)
            data7 = pls.search_frency_from_last(i,7,mode)
            data8 = pls.search_frency_from_last(i,8,mode)
            data9 = pls.search_frency_from_last(i,9,mode)
            data10 = pls.search_frency_from_last(i,10,mode)
            if data1[2] and data2[2] and data3[2] and data4[2] and data5[2] \
                and data6[2]: #and data7[2] and data8[2] and data9[2] and data10[2]: 
                dic[mode].append(True)
            else: 
                dic[mode].append(False)
    count = 0
    for i in range(0,100): 
        if dic['first'][i] and dic['second'][i] and dic['third'][i]: 
            count += 1
            print(True)
        else:
            print(False)
    print(count)
    
    modes = ['first','second','third']
    for m in modes:
        d1 = pls.number_next_appear_all(1,m)
        pd = pandas.Index(d1)
        for i in range(2,7): 
            d = pls.number_next_appear_all(i,m)
            temp_pd = pandas.Index(d)
            pd = pd & temp_pd
        l = list(pd)
        print(l)
    #print(pls.numbers_appear_time_in_last_periods(10))
