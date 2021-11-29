
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
    test_list = []
    dlt = DLT()
    dlt.search_data_from_net(1,21130)
    for n in range(0,100): 
        temp_str = ''
        for i in range(1,5): 
            data = dlt.search_frency_from_last(n,i,'blue')
            temp_str += '<%s-%s>-' % (str(i),str(data[1]))
        test_list.append(temp_str)
    
    counter = Counter(test_list)
    for key,value in counter.items(): 
        if value >5: 
            print(key,value)
                 
    
    test = {1:[{0:2}],2:[{0:2}],3:[{0:2}],4:[{0:1,1:1}]}
    test1 = {1:[{0:2}],2:[{0:2}],3:[{0:2}],4:[{0:2}]}
    test3 = {1:[{0:2}],2:[{0:1,1:1}],3:[{0:1,1:1}],4:[{0:1,1:1}]}
    test4 = {1:[{0:2}],2:[{0:2}],3:[{0:1,1:1}],4:[{0:1,1:1}]}
    test5 = {1:[{0:1,1:1}],2:[{0:1,1:1}],3:[{0:1,1:1}],4:[{0:1,1:1}]}
    
    all_test = [test,test1,test3,test4,test5]
    
    num1 = dlt.number_next_appear_all_real(n+1,1,test,'blue')
    pd = pandas.Index(num1)
    for i in range(2,5): 
        nums = dlt.number_next_appear_all_real(n+1,i,test,'blue')
        tem_pd = pandas.Index(nums)
        pd = pd & tem_pd
        nums = None
        tem_pd = None
    #print(len(pd))
    datas = list(pd)
    print(n,len(datas),datas)
    
    
    
    for n in range(0,20): 
        beego_times = {}
        for i in range(1,8): 
            data = dlt.search_frency_from_last(n,i,'blue')
            beego_times[i] = [Counter(data[1])]
    
            
        num1 = dlt.number_next_appear_all_real(n+1,1,beego_times,'blue')
        pd = pandas.Index(num1)
        for i in range(2,8): 
            nums = dlt.number_next_appear_all_real(n+1,i,beego_times,'blue')
            tem_pd = pandas.Index(nums)
            pd = pd & tem_pd
            nums = None
            tem_pd = None
        #print(len(pd))
        datas = list(pd)
        print(n,len(datas),datas)

    

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





