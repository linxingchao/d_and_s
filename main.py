from typing import ValuesView
from object.dlt import DLT
from object.ssq import SSQ
from os import path
import csv
from collections import Counter


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
    # dlt = DLT(1,21113)
    # dlt.search_data_from_net()
    # dataList = []
    # for i in range(0,dlt.Count): 
    #     data = [i]
    #     for index in range(5): 
    #         data.append(dlt.Red_Numbers[i][index])
    #     data.append(dlt.Blue_Numbers[i][0])
    #     data.append(dlt.Blue_Numbers[i][1])
    #     dataList.append(data)
    # with open("Lottery_data.csv",'w') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(['期号','号码1', '号码2', '号码3', '号码4', '号码5', '号码6', '号码7'])
    #     writer.writerows(dataList)
    dlt = DLT()
    dlt.search_data_from_csv(csv_path)
    print(20,dlt.number_last_appear_theory_times(20,'red'))
    #print(dlt.numbers_last_appear_times_probability(20,'red'))
    # print(dlt.numbers_appear_time_in_last_periods(20,'red'))
    # count = 0
    data1 = dlt.search_frency_from_last(1,1)

    dic = {}
    for i in range(0,100):
        for p1 in range(1,21):
            for p2 in range(p1+1,21):
                for p3 in range(p2+1,21):
                    key = '%s_%s_%s' %(p1,p2,p3)
                    if key not in dic.keys():
                        dic[key] = 0
                    data1 = dlt.search_frency_from_last(i,p1)
                    data2 = dlt.search_frency_from_last(i,p2) 
                    data3 = dlt.search_frency_from_last(i,p3)
                    if data1[2] and data2[2] and data3[2]:
                        dic[key] += 1

    max = 0
    maxKey = ''
    for key,value in dic.items(): 
        if value >= 60: 
            print(key,value)

    for i in (2,3,4):
        print(i,dlt.numbers_appear_time_in_last_periods(i))
            
    # for i in range(1,21): 
    #     count = 0
    #     for j in range(1,101):
    #         data = dlt.search_frency_from_last(j,i)
    #         if data[2]: 
    #             count += 1
    #     print(i,count)

    

  