
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
    pls = PLS(6000)
    pls.search_data_from_net()
    
    
    count = 0
    
    for i in range(100): 
        data = pls.number_no_apear_in_periods(i,2,'com_3')
        if data[0]: 
            count += 1
    print(count)
    

    counter = pls.number_chazhi_for_index(0,100)
    print(counter)

    nums = []
    for num1 in combinations([0,1,2,3,4,5,6,7,8,9],1): 
        for num2 in combinations([0,1,2,3,4,5,6,7,8,9],1):
            for num3 in combinations([0,1,2,3,4,5,6,7,8,9],1):
                temp_num = num1 + num2 + num3
                nums.append(temp_num)
    pd1 = pandas.Index(nums)

    nums2 = []
    [nums2.append(tuple(num)) for num in pls.numbers]
    pd2 = pandas.Index(nums2)

    counter1 = Counter(nums2)
    #print(counter)

    pd = pd1.difference(pd2)

    li = list(pd)
    print(li)


    # count = 0
    # max = 0
    # tem = 0
    # test_list = []
    # for i in range(5000): 
    #     flag = pls.number_no_apear_in_periods(i,2)
    #     if flag[0] == False: 
    #         tem += 1
    #         if tem > max: 
    #             max = tem
    #     else:
    #         test_list.append(tem) 
    #         tem = 0

    #     if flag[0]: 
    #         count += 1
    #     if i < 20: 
    #         print(flag[0],flag[1]) 
    # print(count)
    # print(max)
    # counter = Counter(test_list)

    # print('**************************************************************')
    
    # count = 0
    # for i in range(0,100):

    #     data1 = pls.search_frency_from_last(i,1) #{0：4，1:1}
    #     data2 = pls.search_frency_from_last(i,2) #{0:3,1:2}

    #     data3 = pls.search_frency_from_last(i,3) #{0:3,1:2}
    #     data4 = pls.search_frency_from_last(i,4) #{0:3,1:2}

    #     data5 = pls.search_frency_from_last(i,5) #{0:2,1:1,2:2}
    #     data6 = pls.search_frency_from_last(i,6) #{0:2,1:1,2:1,3:1}
    #     data7 = pls.search_frency_from_last(i,7)
    #     data8 = pls.search_frency_from_last(i,8)
    #     # data7 = pls.search_frency_from_last(i,7) #{0:2,1:1,3:2}
    #     # data8 = pls.search_frency_from_last(i,8) #{0:1,1:2,3:2}

    #     # data9 = pls.search_frency_from_last(i,9) #{0:1,1:2,3:2}
    #     # data10 = pls.search_frency_from_last(i,10) #{0:1,1:2,3:2}

    #     # data11 = pls.search_frency_from_last(i,11)

    #     # data12 = pls.search_frency_from_last(i,12)
    #     # data13 = pls.search_frency_from_last(i,13)
    #     # data14 = pls.search_frency_from_last(i,14)
    #     # data17 = pls.search_frency_from_last(i,17)
    #     # data16 = pls.search_frency_from_last(i,16)
    #     # data19 = pls.search_frency_from_last(i,19)
        
    #     if data1[2] and data2[2] and data3[2] and data4[2] and\
    #          data5[2] and data6[2] and data7[2]and data8[2]:
    #         count += 1
    #         if i<50:
    #             print(True)
    #     else:
    #         if i<50:
    #             print(False)
    # print(count)

    # nums1 = pls.number_next_appear_all(1)
    # pd = pandas.Index(nums1)
    # for i in range(2,9): 
    #     nums = pls.number_next_appear_all(i)
    #     tem_pd = pandas.Index(nums)
    #     pd = pd & tem_pd
    #     nums = None
    #     tem_pd = None
    
    # print(len(pd))

    # last_list = list(pd)
    # print(last_list)
    
    count = 0
    for i in range(100): 
        data = pls.number_has_appear_in_periods(i,4)
        if data[0]: 
            count += 1
    print(count)
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count = 0
    max = 0
    temp = 0
    for i in range(30): 
        flag3 = pls.number_has_perios_in_periods(i,3)
        flag1 = pls.number_has_perios_in_periods(i,1)
        flag2 = pls.number_has_perios_in_periods(i,2)

        if flag1['front'] == 1: 
            count_1 += 1
        if flag2['front'] == 1: 
            count_2 += 1
        if flag3['front'] == 2: 
            count_3 += 1

        if flag3['front'] == 2 and flag3['after'] == 1: 
            count += 1
            if i < 50: 
                print(i)
        
        # if flag2['front'] == 1 and flag['front'] == 2 and flag['after'] == 1 : 
        #     count += 1
        #     if i<50: 
        #         print(i)
            
        # else: 
        #     temp += 1
        #     if temp > max: 
        #        max = temp
        # if i < 20: 
        #     print(flag)
    print(count_1,count_2,count_3)
    print(count)
    print(max)

    # reds = pls.complex_num_6
    # for j in range(1,15): 
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
    #     total = 0 
    #     for h in range(1,count): 
    #         # frency = testList[0][h] / 2000
            
    #         if testList[0][h] >= 50:
    #             total += testList[0][h]
    #             print(testList[h],testList[0][h],testList[0][h] / 2000)
    #     print('totaol:%s' % total)
    #     print("********************************************************")