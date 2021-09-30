from object.dlt import DLT
from object.ssq import SSQ
from os import path
import csv

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
    dlt = DLT(1,21113)
    dlt.search_data_from_net()
    
    dataList = []
    for i in range(0,dlt.Count): 
        data = [i]
        for index in range(5): 
            data.append(dlt.Red_Numbers[i][index])
        data.append(dlt.Blue_Numbers[i][0])
        data.append(dlt.Blue_Numbers[i][1])
        dataList.append(data)
    with open("Lottery_data.csv",'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['期号','号码1', '号码2', '号码3', '号码4', '号码5', '号码6', '号码7'])
        writer.writerows(dataList)


  