
from object.dlt import DLT
from object.ssq import SSQ
from object.pls import PLS
from os import path
import csv
from collections import Counter
from bs4 import BeautifulSoup   #引用BeautifulSoup库
import requests                 #引用requests

from itertools import combinations


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
    dlt.search_data_from_net(1,21114)
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
    #                         dic[key] += 1

    # max = 0
    # maxKey = ''
    # for key,value in dic.items(): 
    #     if value >= 65: 
    #         print(key,value)

            
    for i in range(1,21): 
        count = 0
        for j in range(1,101):
            data = dlt.search_frency_from_last(j,i)
            if data[2]: 
                count += 1
        if count > 65:
            print(i,count)

    data6 = dlt.numbers_appear_time_in_last_periods(6)
    data7 = dlt.numbers_appear_time_in_last_periods(7)
    data12 = dlt.numbers_appear_time_in_last_periods(12)
    data19 = dlt.numbers_appear_time_in_last_periods(19)
    print(6,data6)
    print(7,data7)
    print(12,data12)
    print(19,data19)

    data6_0 = data6[0]
    data6_1 = data6[1]
    data6_2 = data6[2]

    data7_0 = data7[0]
    data7_1 = data7[1]
    data7_2 = data7[2]

    data12_0 = data12[0]
    data12_1 = data12[1]
    data12_2 = data12[2]
    data12_3 = data12[3]

    data19_0 = data19[0]
    data19_1 = data19[1]
    data19_2 = data19[2]
    data19_3 = data19[3]
    data19_4 = data19[4]
    data19_5 = data19[5]
    data19_6 = data19[6]

    data6_0_len = len(data6_0)
    data6_1_len = len(data6_1)
    data6_2_len = len(data6_2)
    
    
    result_data6_0 = list(combinations(data6_0,4))
    result_data6_1 = list(combinations(data6_1,4))
    result_data6_2 = list(combinations(data6_2,2))

    result_data7_0 = list(combinations(data7_0, 3))
    result_data7_1 = list(combinations(data7_1, 4))
    result_data7_2 = list(combinations(data7_2, 2))

    result_data12_0 = list(combinations(data12_0, 2))
    result_data12_1 = list(combinations(data12_1, 3))
    result_data12_2 = list(combinations(data12_2, 3))
    result_data12_3 = list(combinations(data12_3, 2))

    result_data19_0 = list(combinations(data19_0, 1))
    result_data19_1 = list(combinations(data19_1, 2))
    result_data19_2 = list(combinations(data19_2, 3))
    result_data19_3 = list(combinations(data19_3, 3))
    result_data19_4 = list(combinations(data19_4, 2))
    result_data19_5 = list(combinations(data19_5, 1))
    result_data19_6 = list(combinations(data19_6, 1))

    match_nums_6 = []
    for nums0 in result_data6_0: 
        for nums1 in result_data6_1: 
            for nums2 in result_data6_2:
                nums = nums0 + nums1 + nums2
                match_nums_6.append(nums)

    match_nums_7 = []
    for num0 in result_data7_0: 
        for num1 in result_data7_1: 
            for num2 in result_data7_2: 
                nums = num0 + num1 + num2
                match_nums_7.append(nums)

    match_nums_12 = []
    for num0 in result_data12_0: 
        for num1 in result_data12_1: 
            for num2 in result_data12_2: 
                for num3 in result_data12_3:
                    nums = num0 + num1 +num2 + num3 
                    match_nums_12.append(nums)

    match_nums_19 = []
    for num0 in result_data19_0: 
        for num1 in result_data19_1: 
            for num2 in result_data19_2: 
                for num3 in result_data19_3:
                    for num4 in result_data19_4: 
                        for num5 in result_data19_5:
                            for num6 in result_data19_6: 
                                nums = num0 + num1 +num2 + num3 + num4 + num5 + num6
                                match_nums_12.append(nums)


    nums_test = []
    for nums6 in match_nums_6: 
        for nums7 in match_nums_7: 
               if set(nums7).issubset(nums6): 
                nums_test.append(nums6)

    print(len(nums_test))





    # match_data12_1 = []
    # data12_1_len = len(data12_1)
    # for i in range(0,data12_1_len): 
    #     for j in range(i+1,data12_1_len): 
    #         for k in range(j+1,data12_1_len): 
    #             num1 = data12_1[i]
    #             num2 = data12_1[j]
    #             num3 = data12_1[k]
    #             if set([num1,num2,num3]) in set(data19_1): 
    #                 continue
    #             if set([num1,num2,num3]) in set(data19_4): 
    #                 continue
    #             if set([num1,num2]) in set(data19_5) or set([num1,num3]) in set(data19_5) \
    #                 or set([num2,num3]) in set(data19_5): 
    #                 continue
    #             print(num1,num2,num3)
    #             match_data12_1.append(num1)
    #             match_data12_1.append(num2)
    #             match_data12_1.append(num3)
    # print(len(match_data12_1))
    # print(set(match_data12_1))

    # match_data12_2 = []
    # data12_2_len = len(data12_2)
    # for i in range(0,data12_2_len): 
    #     for j in range(i+1,data12_2_len): 
    #         for k in range(j+1,data12_2_len): 
    #             num1 = data12_2[i]
    #             num2 = data12_2[j]
    #             num3 = data12_2[k]
    #             if set([num1,num2,num3]) in set(data19_4): 
    #                 continue
    #             if set([num1,num2]) in set(data19_5) or set([num1,num3]) in set(data19_5) \
    #                 or set([num2,num3]) in set(data19_5): 
    #                 continue
    #             print(num1,num2,num3)
    #             match_data12_2.append(num1)
    #             match_data12_2.append(num2)
    #             match_data12_2.append(num3)
    # print(len(match_data12_2))
    # print(set(match_data12_2))

    # match_data6_1 = []
    # data6_1_len = len(data6_1)
    # for i in range(0,data6_1_len):
    #     for j in range(i+1, data6_1_len): 
    #         for m in range(j+1,data6_1_len): 
    #             for n in range(m+1,data6_1_len): 
    #                 num1 = data6_1[i]
    #                 num2 = data6_1[j]
    #                 num3 = data6_1[m]
    #                 num4 = data6_1[n]

    #                 if set([num1,num2,num3]) in set(data7_2) or set([num1,num2,num4]) in set(data7_2) \
    #                     or set([num4,num2,num3]) in set(data7_2): 
    #                     continue
    #                 if set([num1,num2,num3,num4]) in set(data12_1): 
    #                     continue
    #                 if set([num1,num2,num3,num4]) in set(data12_2): 
    #                     continue 
    #                 if set([num1,num2,num3]) in set(data12_3) or set([num1,num2,num4]) in set(data12_3) \
    #                     or set([num4,num2,num3]) in set(data12_3): 
    #                     continue
    #                 if set([num1,num2,num3]) in set(data19_1) or set([num1,num2,num4]) in set(data19_1) \
    #                     or set([num4,num2,num3]) in set(data19_1): 
    #                     continue 
    #                 if set([num1,num2,num3,num4]) in set(data19_3): 
    #                     continue
    #                 if set([num1,num2,num3,num4]) in set(data19_2): 
    #                     continue
    #                 if set([num1,num2,num3]) in set(data19_4) or set([num1,num2,num4]) in set(data19_4) \
    #                     or set([num4,num2,num3]) in set(data19_4): 
    #                     continue 
    #                 if set([num1,num2]) in set(data19_5) or set([num1,num3]) in set(data19_5) \
    #                     or set([num1,num4]) in set(data19_5) or set([num3,num2]) in set(data19_5)\
    #                     or set([num4,num2]) in set(data19_5) or set([num4,num2]) in set(data19_5): 
    #                     continue
    #                 match_data6_1.append([num1,num2,num3,num4])
    # print(len(match_data6_1))



    



    
    
   

    

  