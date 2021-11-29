
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
    # dlt = DLT()
    # dlt.search_data_from_net(1,21129)
    
    # d = dlt.numbers_appear_time_in_last_periods_for_index(0,15)
    # print(d)
    
    
    # counter = {
    #     1:[Counter({0:5})],
    #     2:[Counter({0:4,1:1})],
    #     3:[Counter({0: 3, 1: 2})],
    #     4:[Counter({0: 4, 1: 1}),Counter({1: 3, 0: 2}),Counter({0: 3, 2: 1, 1: 1}),Counter({1: 2, 0: 2, 2: 1})],
    #     5:[Counter({0: 3, 1: 2}),Counter({0: 2, 1: 2, 2: 1}),Counter({1: 3, 0: 2}),Counter({0: 3, 2: 1, 1: 1})],
        
    # }
    
    test_list = []
    dlt = DLT()
    dlt.search_data_from_net(1,21130)
    
    
    for n in range(0,1000): 
        temp_str = ''
        for i in range(1,6): 
            data = dlt.search_frency_from_last(n,i)
            temp_str += '<%s-%s>-' % (str(i),str(data[1]))
        test_list.append(temp_str)
    
    counter = Counter(test_list)
    for key,value in counter.items(): 
        if value >5: 
            print(key,value)
                 
    
    
    print(dlt.numbers_appear_time_in_last_periods_for_index(0,8))
    
    
    all_counters = {}
    
    filter_nums = {15:10,14:10,13:14,12:15,11:20,10:30,9:40,8:50,7:50,6:50,5:60,4:89,3:94,2:91,1:274}

    reds = dlt.Red_Numbers
   
    p_path = path.dirname(path.abspath(__file__))
    

    for j in range(1,16):
        #temp_counter = {j:[]}
        all_counters[j] = []
        #s_path = p_path + ('/analyze_data/dlt/data_100_%s.csv' % j).replace('/',path.sep)   
        testList = [{}]
        for i in range(0,2000):
            data6 = dlt.search_frency_from_last(i,j)
            counter = Counter(data6[1])
            if counter not in testList:
                testList.append(counter)
                count = len(testList)
                testList[0][count-1] = 1
            else: 
                index = testList.index(counter)
                testList[0][index] += 1
        for h in range(1,count):
            if h > 0 and testList[0][h] > filter_nums[j]: 
                all_counters[j].append(testList[h])
        # with open(s_path,"w",newline='') as csvfile: 
        #     writer = csv.writer(csvfile)
        #     writer.writerow(['Counter','nums','frency'])
        #     for h in range(1,count):
        #         writer.writerow([testList[h],testList[0][h],testList[0][h] / 2000]) 
            
    num1 = dlt.number_next_appear_all_real(0,1,all_counters)
    pd = pandas.Index(num1)
    for i in range(2,16): 
        nums = dlt.number_next_appear_all_real(0,i,all_counters)
        tem_pd = pandas.Index(nums)
        pd = pd & tem_pd
        nums = None
        tem_pd = None
    #print(len(pd))
    datas = list(pd)
    print(len(datas))  
    
    for n in range(0,100): 
        temp_str = ''
        for i in range(1,10): 
            data = dlt.search_frency_from_last(n,i)
            temp_str += '<%s-%s>-' % (str(i),str(data[1]))
        test_list.append(temp_str)
    
    counter = Counter(test_list)
    for key,value in counter.items(): 
        if value >5: 
            print(key,value)
                 
    
    
    for n in range(0,20): 
        beego_times = {}
        for i in range(1,17): 
            data = dlt.search_frency_from_last(n,i)
            beego_times[i] = [Counter(data[1])]
    
            
        num1 = dlt.number_next_appear_all_real(n+1,1,beego_times)
        pd = pandas.Index(num1)
        for i in range(2,9): 
            nums = dlt.number_next_appear_all_real(n+1,i,beego_times)
            tem_pd = pandas.Index(nums)
            pd = pd & tem_pd
            nums = None
            tem_pd = None
        #print(len(pd))
        datas = list(pd)
        print(n,len(datas))
    
