
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


def dlt_theory_appear_times(end,periods): 
    dlt = DLT(1,end)
    dlt.search_data_from_net()
    red_numbers = dlt.Red_Numbers
    blue_numbers = dlt.Blue_Numbers
    #for i in range(1,periods+1): 
    count = len(red_numbers)
    allDic = {}
    for p in range(1,periods+1):
        dic = {}
        for i in range(1,36): 
            dic[i] = 0
        for index in range(0,count-p): 
            current_reds = red_numbers[index]
            last_reds_p = red_numbers[index+1:index+p+1]
            for numbers in last_reds_p: 
                for num in current_reds: 
                    if num in numbers: 
                        dic[num] += 1
        allDic[p] = dic
    return allDic
        
if __name__ == '__main__': 
    csv_path = 'E:/work/d_and_s/Lottery_data.csv'.replace('/', path.sep)
    dlt = DLT()
    dlt.search_data_from_net(1,21115)
    dic = {}
    # for i in range(0,100):
    #     for p1 in range(1,21):
    #         for p2 in range(p1+1,21):
    #             for p3 in range(p2+1,21):
    #                 for p4 in range(p3+1,21):
    #                     key = '%s_%s_%s_%s' %(p1,p2,p3,p4)
    #                     if key not in dic.keys():
    #                         dic[key] = 0
    #                     data1 = dlt.search_frency_from_last(i,p1)
    #                     data6 = dlt.search_frency_from_last(i,p2) 
    #                     data3 = dlt.search_frency_from_last(i,p3)
    #                     data4 = dlt.search_frency_from_last(i,p4)
    #                     if data1[2] and data6[2] and data3[2] and data4[2]:
    #  
    #                        dic[key] += 1
    count = 0
    for i in range(0,100): 
        data4 = dlt.search_frency_from_last(i,4)

        data5 = dlt.search_frency_from_last(i,5)
        data6 = dlt.search_frency_from_last(i,6) 
        data7 = dlt.search_frency_from_last(i,7)
        data8 = dlt.search_frency_from_last(i,8)
        
        data9 = dlt.search_frency_from_last(i,9)
        data10 = dlt.search_frency_from_last(i,10)

        data11 = dlt.search_frency_from_last(i,11)

        data12 = dlt.search_frency_from_last(i,12)
        data13 = dlt.search_frency_from_last(i,13)
        data14 = dlt.search_frency_from_last(i,14)
        data17 = dlt.search_frency_from_last(i,17)
        data16 = dlt.search_frency_from_last(i,16)
        data19 = dlt.search_frency_from_last(i,19)
        if data5[2] and data6[2] and data7[2] and data12[2] \
            and data13[2] and data14[2] and data19[2] and data17[2] \
            and data11[2] and data9[2] and data10[2]:
            count += 1
    print(count)
    max = 0
    maxKey = ''
    for key,value in dic.items(): 
        if value >= 65: 
            print(key,value)

            
    for i in range(1,21): 
        count = 0
        for j in range(1,101):
            data = dlt.search_frency_from_last(j,i)
            if data[2]: 
                count += 1
        
        print(i,count)

    for i in range(4,20): 
        print(i,dlt.numbers_appear_time_in_last_periods(i))

    # data5 = dlt.numbers_appear_time_in_last_periods(5)
    # data6 = dlt.numbers_appear_time_in_last_periods(6)
    # data7 = dlt.numbers_appear_time_in_last_periods(7)
    # data8 = dlt.numbers_appear_time_in_last_periods(8)
    # data9 = dlt.numbers_appear_time_in_last_periods(9)
    # data10 = dlt.numbers_appear_time_in_last_periods(10)
    # data19 = dlt.numbers_appear_time_in_last_periods(19)
    # print(5,data5)
    # print(6,data6)
    # print(7,data7)
    # print(8,data8)
    # print(9,data7)
    # print(10,data10)
    # print(19,data19)
    # for i in range(0,100):
    #     print(dlt.search_frency_from_last(i,19)[1])
    
    # data5_0 = data5[0]
    # data5_1 = data5[1]
    # data5_2 = data5[2]

    # data6_0 = data6[0]
    # data6_1 = data6[1]
    # data6_2 = data6[2]

    # data7_0 = data7[0]
    # data7_1 = data7[1]
    # data7_2 = data7[2]

    # data8_0 = data8[0]
    # data8_1 = data8[1]
    # data8_2 = data8[2]
    # #data8_3 = data8[3]

    # data9_0 = data9[0]
    # data9_1 = data9[1]
    # data9_2 = data9[2]
    # #data9_3 = data9[3]

    # data10_0 = data10[0]
    # data10_1 = data10[1]
    # data10_2 = data10[2]
    # data10_3 = data10[3]

    # # data7_0 = data7[0]
    # # data7_1 = data7[1]
    # # data7_2 = data7[2]

    # # data12_0 = data12[0]
    # # data12_1 = data12[1]
    # # data12_2 = data12[2]
    # # data12_3 = data12[3]

    # # data19_0 = data19[0]
    # # data19_1 = data19[1]
    # # data19_2 = data19[2]
    # # data19_3 = data19[3]
    # # data19_4 = data19[4]
    # # data19_5 = data19[5]
    # # data19_6 = data19[6]

    # # data6_0_len = len(data6_0)
    # # data6_1_len = len(data6_1)
    # # data6_2_len = len(data6_2)
    
    # result_data5_0 = list(combinations(data5_0,4))
    # result_data5_1 = list(combinations(data5_1,3))
    # result_data5_2 = list(combinations(data5_2,1))
    
    # result_data6_0 = list(combinations(data6_0,3))
    # result_data6_1 = list(combinations(data6_1,3))
    # result_data6_2 = list(combinations(data6_2,2))

    # numbers_data6 = []
    # for num6_0 in result_data6_0: 
    #     for num6_1 in result_data6_1: 
    #         for num6_2 in result_data6_2: 
    #             nums = num6_0 + num6_1 + num6_2
    #             numbers_data6.append(tuple(sorted(nums)))

    # numbers_data5 = []
    # for num5_0 in result_data5_0: 
    #     for num5_1 in result_data5_1: 
    #         for num5_2 in result_data5_2: 
    #             nums = num5_0 + num5_1 + num5_2
    #             numbers_data5.append(tuple(sorted(nums)))

    # pd_data_5 = pandas.Index(numbers_data5)
    # pd_data_6 = pandas.Index(numbers_data6)

    # numbers_data5 = None
    # numbers_data6 = None

    # share_5_6 = pd_data_5 & pd_data_6
    # pd_data_5 = None
    # pd_data_6 = None
    # print(len(share_5_6))
    # # for item in share: 
    # # #     print(item)
    
    # result_data7_0 = list(combinations(data7_0,3))
    # result_data7_1 = list(combinations(data7_1,3))
    # result_data7_2 = list(combinations(data7_2,2))

    # result_data8_0 = list(combinations(data8_0,3))
    # result_data8_1 = list(combinations(data8_1,3))
    # result_data8_2 = list(combinations(data8_2,2))

    # result_data9_0 = list(combinations(data9_0,3))
    # result_data9_1 = list(combinations(data9_1,3))
    # result_data9_2 = list(combinations(data9_2,2))

    # numbers_data7 = []
    # for num7_0 in result_data7_0: 
    #     for num7_1 in result_data7_1: 
    #         for num7_2 in result_data7_2: 
    #             nums = num7_0 + num7_1 + num7_2
    #             numbers_data7.append(tuple(sorted(nums)))

    # numbers_data8 = []
    # for num8_0 in result_data8_0: 
    #     for num8_1 in result_data8_1: 
    #         for num8_2 in result_data8_2: 
    #             nums = num8_0 + num8_1 + num8_2
    #             numbers_data8.append(tuple(sorted(nums)))

    # numbers_data9 = []
    # for num9_0 in result_data9_0: 
    #     for num9_1 in result_data9_1: 
    #         for num9_2 in result_data9_2: 
    #             nums = num9_0 + num9_1 + num9_2
    #             numbers_data9.append(tuple(sorted(nums)))

    

    # pd_8 = pandas.Index(numbers_data8)
    # pd_9 = pandas.Index(numbers_data9)

    # numbers_data8 = None
    # #numbers_data9 = None

    # share_8_9 = pd_8  & pd_9
    # print(len(share_8_9))

    # pd_8 = None
    # pd_9 = None
    

    # pd_7_0 = pandas.Index(numbers_data7[0:1000000])
    # pd_7_1 = pandas.Index(numbers_data7[1000000:2000000])
    # pd_7_2 = pandas.Index(numbers_data7[2000000:3000000])
    # pd_7_3 = pandas.Index(numbers_data7[3000000:4000000])
    # pd_7_4 = pandas.Index(numbers_data7[4000000:5000000])
    # pd_7_5 = pandas.Index(numbers_data7[5000000:6000000])
    # pd_7_6 = pandas.Index(numbers_data7[6000000:7000000])
    # pd_7_7 = pandas.Index(numbers_data7[7000000:])
    # numbers_data7 = []
    
    
    # share7_0 = share_8_9 & pd_7_0
    # pd_7_0 = None
    # share7_1 = share_8_9 & pd_7_1
    # pd_7_1 = None
    # share7_2 = share_8_9 & pd_7_2
    # pd_7_1 = None
    # share7_3 = share_8_9 & pd_7_3
    # pd_7_3 = None
    # share7_4 = share_8_9 & pd_7_4
    # pd_7_4 = None
    # share7_5 = share_8_9 & pd_7_5
    # pd_7_5 = None
    # share7_6 = share_8_9 & pd_7_6
    # pd_7_6 = None
    # share7_7 = share_8_9 & pd_7_7
    # pd_7_7 = None
    # share_7_8_9 = share7_0 | share7_1 | share7_2 |share7_3 |share7_4|share7_5|share7_6|share7_7
    # print(len(share_7_8_9))
    # # tem_list = list(share3)
    # # share3 = None
    # # tem_list1 = list(share)
    # # share = None
    # share_5_6_7_8_9 = share_5_6 & share_7_8_9
    # share_5_6 = None 
    # share_7_8_9 = None
    # print(len(share_5_6_7_8_9))

    # result_data10_0 = list(combinations(data10_0,2))
    # result_data10_1 = list(combinations(data10_1,3))
    # result_data10_2 = list(combinations(data10_2,2))
    # result_data10_3 = list(combinations(data10_2,1))


    # numbers_data10 = []
    # for num10_0 in result_data10_0: 
    #     for num10_1 in result_data10_1: 
    #         for num10_2 in result_data10_2: 
    #             for num10_3 in result_data10_3: 
    #                 nums = num10_0 + num10_1 + num10_2 + num10_3
    #                 numbers_data10.append(tuple(sorted(nums)))

    # pd_10_0 = pandas.Index(numbers_data10[0:1000000])
    # pd_10_1 = pandas.Index(numbers_data10[1000000:2000000])
    # pd_10_2 = pandas.Index(numbers_data10[2000000:3000000])
    # pd_10_3 = pandas.Index(numbers_data10[3000000:4000000])
    # # pd_10_4 = pandas.Index(numbers_data10[4000000:5000000])
    # # pd_10_5 = pandas.Index(numbers_data10[5000000:])
    
    # share_10_0 = share_5_6_7_8_9 & pd_10_0
    # pd_10_0 = None
    # share_10_1 = share_5_6_7_8_9 & pd_10_1
    # pd_10_1 = None
    # share_10_2 = share_5_6_7_8_9 & pd_10_2
    # pd_10_2 = None
    # share_10_3 = share_5_6_7_8_9 & pd_10_3
    # pd_10_3 = None
    # # share_10_4 = share_5_6_7_8_9 & pd_10_4
    # # pd_10_4 = None
    # # share_10_5 = share_5_6_7_8_9 & pd_10_5
    # # pd_10_5 = None

    # numbers_data10 = None
    # shareFinal = share_10_0 | share_10_1 | share_10_2 | share_10_3
    # print(len(shareFinal))
    
    # datalist = list(shareFinal)
    # #filePath = 'D:/Code/GitRepositories/d_and_s/analyze_data/ssq/2021-10-6/final_data.csv'.replace('/',path.sep)
    # # with open(filePath,'w') as file: 
    # #     writer = csv.writer(file)
    # #     writer.writerow(("one","two","three","four","five","six","seven","eight"))
    # #     writer.writerows(datalist)
    #     #file.close() 
    # #datalist = []
    # # with open(filePath,'r') as csvfile: 
    # #     reader = csv.reader(csvfile)
    # #     print(reader)
    # #     for row in reader: 
    # #         if row and row[0] != 'one':
    # #             self.__count += 1
    # #             datalist.append([int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[6]),int(row[7])])
    # counter = {}
    # for data in datalist: 
    #     for item in data: 
    #         if item not in counter.keys(): 
    #             counter[item] = 0
    #         counter[item] += 1
    # print(counter)

    
    

    



    
    
   

    

  