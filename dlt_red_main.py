
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

   

    reds = dlt.Red_Numbers
    dic = {}
    for nums in reds: 
        minValue = min(nums)
        if minValue not in dic.keys(): 
            dic[minValue] = 0
        dic[minValue] += 1
    print(dic)

    dic = {}
    count = 0
    for i in range(0,100):

        data1 = dlt.search_frency_from_last(i,1) #{0：4，1:1}
        data2 = dlt.search_frency_from_last(i,2) #{0:3,1:2}

        data3 = dlt.search_frency_from_last(i,3) #{0:3,1:2}
        data4 = dlt.search_frency_from_last(i,4) #{0:3,1:2}

        data5 = dlt.search_frency_from_last(i,5) #{0:2,1:1,2:2}
        data6 = dlt.search_frency_from_last(i,6) #{0:2,1:1,2:1,3:1}
        data7 = dlt.search_frency_from_last(i,7) #{0:2,1:1,3:2}
        data8 = dlt.search_frency_from_last(i,8) #{0:1,1:2,3:2}

        data9 = dlt.search_frency_from_last(i,9) #{0:1,1:2,3:2}
        data10 = dlt.search_frency_from_last(i,10) #{0:1,1:2,3:2}

        # data11 = dlt.search_frency_from_last(i,11)

        # data12 = dlt.search_frency_from_last(i,12)
        # data13 = dlt.search_frency_from_last(i,13)
        # data14 = dlt.search_frency_from_last(i,14)
        # data17 = dlt.search_frency_from_last(i,17)
        # data16 = dlt.search_frency_from_last(i,16)
        # data19 = dlt.search_frency_from_last(i,19)

        if data1[2] and data2[2] and data3[2] and data4[2] and\
             data5[2] and data6[2]:
            count += 1
            if i<20:
                print(True)
        else:
            if i<20:
                print(False)
    print(count)

    nums1 = dlt.number_next_appear_all(1)
    pd = pandas.Index(nums1)
    for i in range(2,7): 
        nums = dlt.number_next_appear_all(i)
        tem_pd = pandas.Index(nums)
        pd = pd & tem_pd
        nums = None
        tem_pd = None
    
    print(len(pd))

    datas = list(pd)
    test1 = []
    no_numbers = [1,7,8,11,13,14,15,16,17,18,28,29,30,34,35]
    for d in datas:
        dd = [d1 for d1 in d if d1 in no_numbers]
        if not dd:
            test1.append(d) 
        # dd1 = [d1 for d1 in d if d1 <10]
        # dd2 = [d1 for d1 in d if d1 >=10 and d1 < 20]
        # dd3 = [d1 for d1 in d if d1 >=20 and d1 < 30]
        # dd4 = [d1 for d1 in d if d1 >=30 and d1 < 36]
        # if len(dd1) == 0 and len(dd2) == 2 and len(dd3) == 2 and len(dd4) == 1: 
        #    test1.append(d)

    print(len(test1))
    #for ddd in test1: 
    with open('numbers.csv','w') as file: 
        writer = csv.writer(file)
        writer.writerows(test1)

        #print(ddd)
    last_num = []
    for dd in datas:
        for d in dd:
            if d not in last_num: 
                last_num.append(d)
    print(last_num) 
    

    # for j in range(1,11): 
    #     testList = [{}]
    #     for i in range(0,2000):
    #         data6 = dlt.search_frency_from_last(i,j)
    #         counter = Counter(data6[1])
    #         if counter not in testList:
    #             testList.append(counter)
    #             count = len(testList)
    #             testList[0][count-1] = 1
    #         else: 
    #             index = testList.index(counter)
    #             testList[0][index] += 1
    #     print(j)        
    #     for h in range(1,count): 
    #         frency = testList[0][h] / 2000
    #         if testList[0][h] >= 100 and testList[0][h] <150:
    #             print(testList[h],testList[0][h],testList[0][h] / 2000)
    #     print("********************************************************")
    #print(testList)


    # for i in range(0,10):
    #     print(dlt.search_frency_from_last(i,5)[2],dlt.search_frency_from_last(i,6)[2],dlt.search_frency_from_last(i,7)[2],\
    #         dlt.search_frency_from_last(i,8)[2],dlt.search_frency_from_last(i,9)[2],\
    #         dlt.search_frency_from_last(i,10)[2])

    for i in range(0,101):
        data = dlt.search_frency_from_last(i,6)
        if data[2]:
            count += 1


    # for i in range(4,20):
    #     print(i,dlt.numbers_appear_time_in_last_periods(i))
    data2 = dlt.numbers_appear_time_in_last_periods(2)
    data3 = dlt.numbers_appear_time_in_last_periods(3)
    data4 = dlt.numbers_appear_time_in_last_periods(4)
    data5 = dlt.numbers_appear_time_in_last_periods(5)
    data6 = dlt.numbers_appear_time_in_last_periods(6)
    data7 = dlt.numbers_appear_time_in_last_periods(7)
    data8 = dlt.numbers_appear_time_in_last_periods(8)
    data9 = dlt.numbers_appear_time_in_last_periods(9)
    data10 = dlt.numbers_appear_time_in_last_periods(10)
    #data11 = dlt.numbers_appear_time_in_last_periods(11)

    # for i in range(1,21):
    #     print(i,dlt.numbers_appear_time_in_last_periods(i))

    # for i in range(0,100):
    #     print(dlt.search_frency_from_last(i,19)[1])





