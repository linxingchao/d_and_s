
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
    dlt.search_data_from_net(1,21119)

   

    reds = dlt.Blue_Numbers
    for j in range(1,11): 
        testList = [{}]
        for i in range(0,2000):
            data6 = dlt.search_frency_from_last(i,j,'blue')
            counter = Counter(data6[1])
            if counter not in testList:
                testList.append(counter)
                count = len(testList)
                testList[0][count-1] = 1
            else: 
                index = testList.index(counter)
                testList[0][index] += 1
        print(j)        
        for h in range(1,count): 
            frency = testList[0][h] / 2000
            if testList[0][h] >= 100 and testList[0][h] <150:
                print(testList[h],testList[0][h],testList[0][h] / 2000)
        print("********************************************************")
   
    for i in range(0,101):
        data = dlt.search_frency_from_last(i,6)
        if data[2]:
            count += 1





