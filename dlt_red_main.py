
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
    dlt.search_data_from_net(1,21128)
    
    d = dlt.numbers_appear_time_in_last_periods_for_index(0,15)
    print(d)
    
    counter = {
        1:[Counter({0:5})],
        2:[Counter({0:4,1:1})],
        3:[Counter({0: 3, 1: 2})],
        4:[Counter({0: 4, 1: 1}),Counter({1: 3, 0: 2}),Counter({0: 3, 2: 1, 1: 1}),Counter({1: 2, 0: 2, 2: 1})],
        5:[Counter({0: 3, 1: 2}),Counter({0: 2, 1: 2, 2: 1}),Counter({1: 3, 0: 2}),Counter({0: 3, 2: 1, 1: 1})],
        
    }
    
    # for n in range(0,20): 
    #     dlt = DLT()
    #     dlt.search_data_from_net(1,21128-n)
    #     beego_times = {}
    #     for i in range(1,16): 
    #         data = dlt.search_frency_from_last(0,i)
    #         beego_times[i] = [Counter(data[1])]
            
    #     dlt1 = DLT()
    #     dlt1.search_data_from_net(1,21128-n)
    #     num1 = dlt1.number_next_appear_all_real(1,beego_times)
    #     pd = pandas.Index(num1)
    #     for i in range(2,15): 
    #         nums = dlt1.number_next_appear_all_real(i,beego_times)
    #         tem_pd = pandas.Index(nums)
    #         pd = pd & tem_pd
    #         nums = None
    #         tem_pd = None
    #     #print(len(pd))
    #     datas = list(pd)
    #     print(n,len(datas),datas)
    
    
    

    # datas = list(pd)

    filter_nums = {15:4,14:4,13:5,12:8,11:8,10:9,9:11,8:11,7:14,6:20,5:60,4:89,3:94,2:91,1:274}

    reds = dlt.Red_Numbers
   
    p_path = path.dirname(path.abspath(__file__))
    
    all_counters = []

    for j in range(1,16):
        temp_counter = {j:[]}
        s_path = p_path + ('/analyze_data/dlt/data_100_%s.csv' % j).replace('/',path.sep)   
        testList = [{}]
        for i in range(0,100):
            data6 = dlt.search_frency_from_last(i,j)
            counter = Counter(data6[1])
            if counter not in testList:
                testList.append(counter)
                count = len(testList)
                testList[0][count-1] = 1
            else: 
                index = testList.index(counter)
                testList[0][index] += 1
        # for h in range(1,count):
        #     if h > 0 and testList[0][h] > filter_nums[j]: 
        #         temp_counter[j].append(testList[h])
        # all_counters.append(temp_counter)
        with open(s_path,"w",newline='') as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(['Counter','nums','frency'])
            for h in range(1,count):
                writer.writerow([testList[h],testList[0][h],testList[0][h] / 2000]) 
            
        
        
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





