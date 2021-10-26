from object.dlt import DLT
from object.ssq import SSQ
from object.pls import PLS
from object.dlt import data_times
from os import path
import csv
from collections import Counter
from bs4 import BeautifulSoup   #引用BeautifulSoup库
import requests                 #引用requests

from itertools import combinations
import time
import pandas


if __name__ == '__main__': 
    ssq = SSQ(end='21120')
    ssq.search_data_from_net()

    # for i in range(1,21): 
    #     print(i,ssq.number_last_appear_theory_times(i))

    count = 0
    for i in range(0,100):

        data1 = ssq.search_frency_from_last(i,1) #{0：4，1:1}
        data2 = ssq.search_frency_from_last(i,2) #{0:3,1:2}

        data3 = ssq.search_frency_from_last(i,3) #{0:3,1:2}
        data4 = ssq.search_frency_from_last(i,4) #{0:3,1:2}

        # data5 = dlt.search_frency_from_last(i,5) #{0:2,1:1,2:2}
        # data6 = dlt.search_frency_from_last(i,6) #{0:2,1:1,2:1,3:1}
        # data7 = dlt.search_frency_from_last(i,7) #{0:2,1:1,3:2}
        # data8 = dlt.search_frency_from_last(i,8) #{0:1,1:2,3:2}

        # data9 = dlt.search_frency_from_last(i,9,'blue') #{0:1,1:2,3:2}
        # data10 = dlt.search_frency_from_last(i,10,'blue') #{0:1,1:2,3:2}

        # data11 = dlt.search_frency_from_last(i,11)

        # data12 = dlt.search_frency_from_last(i,12)
        # data13 = dlt.search_frency_from_last(i,13)
        # data14 = dlt.search_frency_from_last(i,14)
        # data17 = dlt.search_frency_from_last(i,17)
        # data16 = dlt.search_frency_from_last(i,16)
        # data19 = dlt.search_frency_from_last(i,19)

        if data1[2] and data2[2] and data3[2] and data4[2]:
            count += 1
            if i<20:
                print(True)
        else:
            if i<20:
                print(False)
    print(count)

    nums1 = ssq.number_next_appear_all(1)
    pd = pandas.Index(nums1)
    for i in range(2,5): 
        nums = ssq.number_next_appear_all(i)
        tem_pd = pandas.Index(nums)
        pd = pd & tem_pd
        nums = None
        tem_pd = None
    
    print(len(pd))
    test_list = list(pd)
    ddd = []
    for d in test_list: 
        dd = [d1 for d1 in d if d1<=18]
        if len(dd) == 5: 
            ddd.append(dd)

    print(len(ddd))
    if [1,7,8,12,13,18] in ddd: 
        print(True)

    # reds = ssq.Red_Numbers
    # for j in range(1,7): 
    #     testList = [{}]
    #     for i in range(0,2000):
    #         data6 = ssq.search_frency_from_last(i,j)
    #         counter = Counter(data6[1])
    #         if counter not in testList:
    #             testList.append(counter)
    #             count = len(testList)
    #             testList[0][count-1] = 1
    #         else: 
    #             index = testList.index(counter)
    #             testList[0][index] += 1
    #     print(j)   
    #     print(testList[h],testList[0][h],testList[0][h] / 2000)     
    #     for h in range(1,count): 
    #         frency = testList[0][h] / 2000
    #         if testList[0][h] >= 100 and testList[0][h] <150:
    #         print(testList[h],testList[0][h],testList[0][h] / 2000)
    #     print("********************************************************")