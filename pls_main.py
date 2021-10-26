
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
    
    count = 0
    for i in range(0,1000):

        data1 = pls.search_frency_from_last(i,1) #{0：4，1:1}
        data2 = pls.search_frency_from_last(i,2) #{0:3,1:2}

        data3 = pls.search_frency_from_last(i,3) #{0:3,1:2}
        data4 = pls.search_frency_from_last(i,4) #{0:3,1:2}

        data5 = pls.search_frency_from_last(i,5) #{0:2,1:1,2:2}
        data6 = pls.search_frency_from_last(i,6) #{0:2,1:1,2:1,3:1}
        # data7 = pls.search_frency_from_last(i,7) #{0:2,1:1,3:2}
        # data8 = pls.search_frency_from_last(i,8) #{0:1,1:2,3:2}

        # data9 = pls.search_frency_from_last(i,9) #{0:1,1:2,3:2}
        # data10 = pls.search_frency_from_last(i,10) #{0:1,1:2,3:2}

        # data11 = pls.search_frency_from_last(i,11)

        # data12 = pls.search_frency_from_last(i,12)
        # data13 = pls.search_frency_from_last(i,13)
        # data14 = pls.search_frency_from_last(i,14)
        # data17 = pls.search_frency_from_last(i,17)
        # data16 = pls.search_frency_from_last(i,16)
        # data19 = pls.search_frency_from_last(i,19)

        if data1[2] and data2[2] and data3[2] and data4[2] and\
             data5[2] and data6[2]:
            count += 1
            if i<20:
                print(True)
        else:
            if i<20:
                print(False)
    print(count)

    nums1 = pls.number_next_appear_all(1)
    pd = pandas.Index(nums1)
    for i in range(2,7): 
        nums = pls.number_next_appear_all(i)
        tem_pd = pandas.Index(nums)
        pd = pd & tem_pd
        nums = None
        tem_pd = None
    
    print(len(pd))


    # reds = pls.complex_num_6
    # for j in range(1,11): 
    #     testList = [{}]
    #     for i in range(0,2000):
    #         data6 = pls.search_frency_from_last(i,j)
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
    #         if testList[0][h] >= 50:
    #             print(testList[h],testList[0][h],testList[0][h] / 2000)
    #     print("********************************************************")