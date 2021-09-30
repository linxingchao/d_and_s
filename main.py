from object.dlt import DLT
from object.ssq import SSQ
from os import path

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
    print(dlt.red_numbers_appear_times())
    print(len(dlt.Blue_Numbers))
    print(dlt_theory_appear_times(21113,20))