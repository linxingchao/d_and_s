
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
    csv_path = 'E:/work/d_and_s/Lottery_data.csv'.replace('/', path.sep)
    dlt = DLT()
    dlt.search_data_from_net(1,21120)

    count = 0
    for i in range(0,100):

        data1 = dlt.search_frency_from_last(i,1,'blue') #{0：4，1:1}
        data2 = dlt.search_frency_from_last(i,2,'blue') #{0:3,1:2}

        data3 = dlt.search_frency_from_last(i,3,'blue') #{0:3,1:2}
        data4 = dlt.search_frency_from_last(i,4,'blue') #{0:3,1:2}

        data5 = dlt.search_frency_from_last(i,5,'blue') #{0:2,1:1,2:2}
        data6 = dlt.search_frency_from_last(i,6,'blue') #{0:2,1:1,2:1,3:1}
        data7 = dlt.search_frency_from_last(i,7,'blue') #{0:2,1:1,3:2}
        data8 = dlt.search_frency_from_last(i,8,'blue') #{0:1,1:2,3:2}

        data9 = dlt.search_frency_from_last(i,9,'blue') #{0:1,1:2,3:2}
        data10 = dlt.search_frency_from_last(i,10,'blue') #{0:1,1:2,3:2}

        # data11 = dlt.search_frency_from_last(i,11)

        # data12 = dlt.search_frency_from_last(i,12)
        # data13 = dlt.search_frency_from_last(i,13)
        # data14 = dlt.search_frency_from_last(i,14)
        # data17 = dlt.search_frency_from_last(i,17)
        # data16 = dlt.search_frency_from_last(i,16)
        # data19 = dlt.search_frency_from_last(i,19)

        if data1[2] and data2[2] and data3[2] and data4[2] and\
             data5[2] and data6[2] and data7[2] and data8[2] and data9[2] and data10[2]:
            count += 1
            if i<20:
                print(True)
        else:
            if i<20:
                print(False)
    print(count)

    nums1 = dlt.number_next_appear_all(1,'blue')
    pd = pandas.Index(nums1)
    for i in range(2,11): 
        nums = dlt.number_next_appear_all(i,'blue')
        tem_pd = pandas.Index(nums)
        pd = pd & tem_pd
        nums = None
        tem_pd = None
    
    print(len(pd))

    datas = list(pd)
    for d in datas: 
        print(d)

    # reds = dlt.Blue_Numbers
    # for j in range(1,11): 
    #     testList = [{}]
    #     for i in range(0,2000):
    #         data6 = dlt.search_frency_from_last(i,j,'blue')
    #         counter = Counter(data6[1])
    #         if counter not in testList:
    #             testList.append(counter)
    #             count = len(testList)
    #             testList[0][count-1] = 1
    #         else: 
    #             index = testList.index(counter)
    #             testList[0][index] += 1
    #     print(j)   
    #     #print(testList[h],testList[0][h],testList[0][h] / 2000)     
    #     for h in range(1,count): 
    #         # frency = testList[0][h] / 2000
    #         # if testList[0][h] >= 100 and testList[0][h] <150:
    #         print(testList[h],testList[0][h],testList[0][h] / 2000)
    #     print("********************************************************")
   
    # for i in range(0,101):
    #     data = dlt.search_frency_from_last(i,6)
    #     if data[2]:
    #         count += 1





