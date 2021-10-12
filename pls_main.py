
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
    pls = PLS(100000)
    pls.search_data_from_net()
    # for i in range(20,21):
    #     print(pls.number_last_appear_theory_times(i,'first'))
    count = 0
    for i in range(0,1):
        data1 = pls.search_frency_from_last(i,1)
        data2 = pls.search_frency_from_last(i,2)
        data3 = pls.search_frency_from_last(i,3)
        data4 = pls.search_frency_from_last(i,4)
        data5 = pls.search_frency_from_last(i,5)
        data6 = pls.search_frency_from_last(i,6)
        data7 = pls.search_frency_from_last(i,7)
        data8 = pls.search_frency_from_last(i,8)
        data9 = pls.search_frency_from_last(i,9)
        data10 = pls.search_frency_from_last(i,10)
        if data1[2] and data2[2] and data3[2] and data4[2] and data5[2] \
           and data6[2] and data7[2] and data8[2] and data9[2] and data10[2]: 
            count += 1
    print(count)
    print(pls.numbers_appear_time_in_last_periods(20))

    data1_0 = data1[0]
    data1_1 = data1[1]

    data2_0 = data2[0]
    data2_1 = data2[1]
    
    data3_0 = data1[0]
    data3_1 = data1[1]
