
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
    dlt.search_data_from_net(1,21116)
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
    for i in range(0,11): 

        data3 = dlt.search_frency_from_last(i,3)
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
        data11 = dlt.search_frency_from_last(i,11)
        if data6[2] and data7[2] \
            and data8[2] and data9[2] and data10[2]: 
            count += 1
    print(count)
    max = 0
    maxKey = ''
    for key,value in dic.items(): 
        if value >= 65: 
            print(key,value)

    # for i in range(0,10): 
    #     print(dlt.search_frency_from_last(i,5)[2],dlt.search_frency_from_last(i,6)[2],dlt.search_frency_from_last(i,7)[2],\
    #         dlt.search_frency_from_last(i,8)[2],dlt.search_frency_from_last(i,9)[2],\
    #         dlt.search_frency_from_last(i,10)[2])

            
    for i in range(1,21): 
        count = 0
        for j in range(1,101):
            data = dlt.search_frency_from_last(j,i)
            if data[2]: 
                count += 1
        
        print(i,count)

    # for i in range(4,20): 
    #     print(i,dlt.numbers_appear_time_in_last_periods(i))

    data4 = dlt.numbers_appear_time_in_last_periods(4)
    data5 = dlt.numbers_appear_time_in_last_periods(5)
    data6 = dlt.numbers_appear_time_in_last_periods(6)
    data7 = dlt.numbers_appear_time_in_last_periods(7)
    data8 = dlt.numbers_appear_time_in_last_periods(8)
    data9 = dlt.numbers_appear_time_in_last_periods(9)
    data10 = dlt.numbers_appear_time_in_last_periods(10)
    data11 = dlt.numbers_appear_time_in_last_periods(11)
  
    # for i in range(0,100):
    #     print(dlt.search_frency_from_last(i,19)[1])

#     data4_0 = data4[0]
#     data4_1 = data4[1]
#     data4_2 = data4[2]
    
#     data5_0 = data5[0]
#     data5_1 = data5[1]
#     data5_2 = data5[2]
#    # data5_3 = data5[3]

#     data6_0 = data6[0]
#     data6_1 = data6[1]
#     data6_2 = data6[2]
#     data6_3 = data6[3]

#     data7_0 = data7[0]
#     data7_1 = data7[1]
#     data7_2 = data7[2]
#     data7_3 = data7[3]

#     data8_0 = data8[0]
#     data8_1 = data8[1]
#     data8_2 = data8[2]
#     data8_3 = data8[3]

#     data9_0 = data9[0]
#     data9_1 = data9[1]
#     data9_2 = data9[2]
#     data9_3 = data9[3]

#     data10_0 = data10[0]
#     data10_1 = data10[1]
#     data10_2 = data10[2]
#     data10_3 = data10[3]

#     data11_0 = data11[0]
#     data11_1 = data11[1]
#     data11_2 = data11[2]
#     data11_3 = data11[3]

#     result_data4_0 = list(combinations(data4_0,4))
#     result_data4_1 = list(combinations(data4_1,3))
#     result_data4_2 = list(combinations(data4_2,1))
    
#     result_data5_0 = list(combinations(data5_0,4))
#     result_data5_1 = list(combinations(data5_1,3))
#     result_data5_2 = list(combinations(data5_2,1))
#     #result_data5_3 = list(combinations(data5_3,1))
    

#     numbers_data4 = []
#     for num4_0 in result_data4_0:
#         for num4_1 in result_data4_1:
#             #for num4_2 in result_data4_2:
#             nums = num4_0 + num4_1
#             numbers_data4.append(tuple(sorted(nums)))
#     print({4:len(numbers_data4)})

#     numbers_data5 = []
#     for num5_0 in result_data5_0: 
#         for num5_1 in result_data5_1: 
#             #for num5_2 in result_data5_2: 
#             nums = num5_0 + num5_1
#             numbers_data5.append(tuple(sorted(nums)))

#     print({5:len(numbers_data5)})

#     pd_4 = pandas.Index(numbers_data4)
#     pd_5 = pandas.Index(numbers_data5)
#     numbers_data5 = None
#     numbers_data4 = None
#     share_4_5 = pd_4 & pd_5
#     #pd_4 = None
#     #pd_5 = None
#     # print(len(share_4_5))

#     result_data6_0 = list(combinations(data6_0,2))
#     result_data6_1 = list(combinations(data6_1,3))
#     result_data6_2 = list(combinations(data6_2,2))
#     result_data6_3 = list(combinations(data6_3,1))
    
#     result_data7_0 = list(combinations(data7_0,2))
#     result_data7_1 = list(combinations(data7_1,3))
#     result_data7_2 = list(combinations(data7_2,2))
#     result_data7_3 = list(combinations(data7_3,1))

#     result_data8_0 = list(combinations(data8_0,2))
#     result_data8_1 = list(combinations(data8_1,3))
#     result_data8_2 = list(combinations(data8_2,2))
#     result_data8_3 = list(combinations(data8_3,1))

#     result_data9_0 = list(combinations(data9_0,2))
#     result_data9_1 = list(combinations(data9_1,3))
#     result_data9_2 = list(combinations(data9_2,2))
#     result_data9_3 = list(combinations(data9_3,1))

#     result_data10_0 = list(combinations(data10_0,2))
#     result_data10_1 = list(combinations(data10_1,3))
#     result_data10_2 = list(combinations(data10_2,2))
#     result_data10_3 = list(combinations(data10_3,1))

#     result_data11_0 = list(combinations(data11_0,2))
#     result_data11_1 = list(combinations(data11_1,3))
#     result_data11_2 = list(combinations(data11_2,2))
#     result_data11_3 = list(combinations(data11_3,1))

#     numbers_data6 = []
#     for num6_0 in result_data6_0: 
#         for num6_1 in result_data6_1: 
#             for num6_2 in result_data6_2: 
#                 #for num6_3 in result_data6_3: 
#                 nums = num6_0 + num6_1 + num6_2 
#                 numbers_data6.append(tuple(sorted(nums)))
#     print({6:len(numbers_data6)})

#     numbers_data7 = []
#     for num7_0 in result_data7_0: 
#         for num7_1 in result_data7_1: 
#             for num7_2 in result_data7_2: 
#                 #for num7_3 in result_data7_3: 
#                 nums = num7_0 + num7_1 + num7_2
#                 numbers_data7.append(tuple(sorted(nums)))
#     print({7:len(numbers_data7)})

#     numbers_data8 = []
#     for num8_0 in result_data8_0: 
#         for num8_1 in result_data8_1: 
#             for num8_2 in result_data8_2: 
#                 #for num8_3 in result_data8_3: 
#                 nums = num8_0 + num8_1 + num8_2
#                 numbers_data8.append(tuple(sorted(nums)))
#     print({8:len(numbers_data8)})

#     numbers_data9 = []
#     for num9_0 in result_data9_0: 
#         for num9_1 in result_data9_1: 
#             for num9_2 in result_data9_2: 
#                 #for num9_3 in result_data9_3: 
#                 nums = num9_0 + num9_1 + num9_2
#                 numbers_data9.append(tuple(sorted(nums)))
#     print({9:len(numbers_data9)})

#     numbers_data10 = []
#     for num10_0 in result_data10_0: 
#         for num10_1 in result_data10_1: 
#             for num10_2 in result_data10_2: 
#                 #for num10_3 in result_data10_3: 
#                 nums = num10_0 + num10_1 + num10_2 
#                 numbers_data10.append(tuple(sorted(nums)))
#     print({10:len(numbers_data10)})

#     numbers_data11 = []
#     for num11_0 in result_data11_0: 
#         for num11_1 in result_data11_1: 
#             for num11_2 in result_data11_2: 
#                 #for num11_3 in result_data11_3: 
#                     nums = num11_0 + num11_1 + num11_2
#                     numbers_data11.append(tuple(sorted(nums)))
#     print({11:len(numbers_data11)})

#     pd_6 = pandas.Index(numbers_data6)
#     pd_7 = pandas.Index(numbers_data7)
#     pd_8 = pandas.Index(numbers_data8)
#     pd_9 = pandas.Index(numbers_data9)
#     pd_10 = pandas.Index(numbers_data10)
#     pd_11 = pandas.Index(numbers_data11)
#     numbers_data6 = None
#     numbers_data7 = None
#     numbers_data8 = None
#     numbers_data9 = None
#     numbers_data10 = None

#     share_6_7_8_9_10 = pd_6 & pd_7 & pd_8 & pd_9 & pd_10
#     pd_6 = None
#     pd_7 = None
#     pd_8 = None
#     pd_9 = None
#     pd_10 = None
#     print(len(share_6_7_8_9_10))

#     counts = []
#     for item in share_6_7_8_9_10: 
#         for num in item: 
#             if num not in counts: 
#                 counts.append(num)
#     print(counts)

#     pd_fianal= share_6_7_8_9_10 & pd_11 &share_4_5

#     print(len(pd_fianal))

#     list1 = list(share_4_5)
#     list1_len = len(list1)
#     list2 = list(share_6_7_8_9_10)
#     list2_len = len(list2)

#     finale_nums = []
#     for i in range(0,list1_len): 
#         num1 = list1[i]
#         for j in range(0,list2_len): 
#             num2 = list2[j]
#             if num2 in finale_nums: 
#                 continue
#             if set(num1).issubset(set(num2)): 
#                 finale_nums.append(num2)

    # temp_list1 = list(share_4_5)
    # temp_list2 = list(share_6_7_8_9_10)

    #  



  