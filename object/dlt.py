from typing import Counter
from object.lottery import Lottery

from bs4 import BeautifulSoup   #引用BeautifulSoup库
import requests                 #引用requests
import os                       #os
import pandas as pd
import csv
import codecs
import collections
from itertools import combinations

thoery_data = {
    'red':{
        1:{
            0:5,1:1
        },
        2:{
            0:5,1:2,
        },
        3:{
            #6
            0:4,1:2,2:1
        },
        4:{
            #6
            0:3,1:2,2:1
        },
        5:{ # 7
            0:3,1:2,2:1
        },
        6:{ #8
            0:3,1:3,2:1,3:1
        },
        7:{#8
            0:2,1:3,2:2,3:1
        },
        8:{#8
            0:2,1:3,2:2,3:1
        },
        9:{#8
            0:2,1:3,2:2,3:1
        },
        10:{#8
            0:2,1:3,2:2,3:1
        },
        11:{#10
            0:2,1:3,2:2,3:1
        },
        12:{#11
            0:2,1:3,2:3,3:2,4:1
        },
        13:{#11
            0:2,1:3,2:3,3:2,4:1
        },
        14:{#11
            0:1,1:3,2:3,3:2,4:1,5:1
        },
        15:{#11
            0:1,1:2,2:3,3:2,4:1,5:1
        },
        16:{
            #11
            0:1,1:2,2:3,3:2,4:1,5:1
        },
        17:{#11
            0:1,1:2,2:3,3:2,4:2,5:1
        },
        18:{#11
            0:1,1:2,2:2,3:2,4:2,5:1
        },
        19:{#11
            0:1,1:2,2:2,3:2,4:2,5:1,6:1
        },
        20:{#11
            # (0 + 6):1
            0:1,1:2,2:2,3:2,4:2,5:1,6:1
        }
    },
    'blue':{

    }
}

# data_times = {
#     'red':{
#         1:[{0:5},{0:4,1:1}],
#         2:[{0:5},{0:3,1:2},{0:4,1:1},{}],
#         3:[{1:3,0:2},{0:4,1:1},{0:3,1:2}],
#         4:[{0:4,1:1},{0:3,1:2},{1:3,0:2}],
#         5:[{0:2,1:2,2:1},{0:3,1:2},{1:3,0:2},{0:3,2:1,1:1}],
#         6:[{0:2,1:2,2:1},{0:3,1:2},{2:2,1:2,0:1},
#             {0:3,2:1,1:1},{1:3,2:1,0:1},{1:3, 0:2},{0:2,2:2,1:1}],
#         7:[{1: 3, 2: 1, 0: 1},{1: 3, 0: 2},{0: 3, 2: 1, 1: 1},\
#             {2: 2, 1: 2, 0: 1},{0: 2, 1: 2, 2: 1},{2: 2, 0: 2, 1: 1},\
#             {1: 4, 0: 1},{1: 2, 2: 1, 0: 1, 3: 1},{0: 3, 1: 2}],
#         8:[{1: 3, 2: 1, 0: 1},{1: 2, 0: 2, 2: 1},{2: 2, 1: 2, 0: 1},\
#             {1: 2, 2: 1, 3: 1, 0: 1},{0: 3, 2: 1, 1: 1},{0: 2, 1: 1, 3: 1, 2: 1},\
#             {0: 2, 2: 2, 1: 1},{1: 3, 2: 2}],
#         9:[{1: 2, 2: 2, 0: 1},{1: 2, 0: 2, 2: 1},{1: 3, 0: 1, 2: 1},\
#             {1: 2, 2: 1, 0: 1, 3: 1},{2: 2, 0: 2, 1: 1},{0: 2, 3: 1, 2: 1, 1: 1},\
#             {1: 3, 3: 1, 2: 1},{1: 3, 2: 2}],
#         10:[{1: 2, 2: 2, 0: 1},{1: 2, 0: 1, 2: 1, 3: 1},{1: 3, 0: 1, 2: 1},{2: 2, 1: 2, 3: 1},{1: 2, 0: 2, 2: 1},\
#             {2: 2, 3: 1, 1: 1, 0: 1},{2: 2, 0: 2, 1: 1}]

#     }
# }

# data_times = {
#     'red':{
#         1:[{0:4,1:1},{0:5}],
#         2:[{0:4,1:1},{0:3,1:2}],
#         3:[ {0:3,1:2},{1:3,0:2},{0:4,1:1}],
#         4:[{0: 3, 1: 2},{0: 4, 1: 1},{1: 3, 0: 2},\
#             {0: 3, 2: 1, 1: 1},{1: 2, 0: 2, 2: 1}],
#         5:[{1: 3, 0: 2},{0: 3, 2: 1, 1: 1},{1: 2, 0: 2, 2: 1},{0: 3, 1: 2}],
#         6:[{0: 3, 1: 2},{0: 3, 2: 1, 1: 1},{1: 3, 0: 2},{1: 3, 2: 1, 0: 1}],
#         7:[{1: 3, 2: 1, 0: 1},{2: 2, 1: 2, 0: 1},{0: 3, 2: 1, 1: 1},\
#             {1: 3, 0: 2},{2: 2, 0: 2, 1: 1}],
#         8:[{1: 3, 2: 1, 0: 1},{1: 2, 0: 2, 2: 1},{2: 2, 1: 2, 0: 1},{1: 2, 2: 1, 3: 1, 0: 1}],
#         9:[{1: 2, 2: 2, 0: 1},{1: 2, 0: 2, 2: 1},{1: 3, 0: 1, 2: 1},{1: 2, 2: 1, 0: 1, 3: 1}],
#         10:[{1: 2, 2: 2, 0: 1},{1: 2, 0: 1, 2: 1, 3: 1}]
#     },
#     'blue':{
#         1:[{0: 2},{1: 1, 0: 1}],
#         2:[{0: 2},{0: 1, 1: 1}],
#         3:[{0: 1, 1: 1},{0: 2},{1: 2}],
#         4:[{0: 1, 1: 1},{0: 2},{1: 2},{0: 1, 2: 1}],
#         5:[{0: 1, 1: 1},{1: 2},{0: 1, 2: 1},{0: 2}],
#         6:[{0: 1, 1: 1},{0: 1, 2: 1},{2: 1, 1: 1},{1: 2},{0: 2}],
#         7:[{0: 1, 1: 1},{2: 1, 0: 1},{1: 2},{2: 1, 1: 1}],
#         8:[{2: 1, 1: 1},{0: 1, 1: 1},{1: 2},{0: 1, 2: 1},{3: 1, 1: 1}],
#         9:[{2: 1, 1: 1},{0: 1, 1: 1},{1: 2},{2: 1, 0: 1},{3: 1, 1: 1}],
#         10:[{2: 1, 1: 1},{1: 2},{3: 1, 1: 1},{2: 1, 3: 1},{2: 1, 0: 1},{1: 1, 0: 1}]
#     }
# }

data_times = {
    'red':{
        1:[{0: 5}],
        2:[{0: 4, 1: 1}],
        3:[ {0: 4, 1: 1}],
        4:[{0: 4, 1: 1}],
        5:[{0: 4, 1: 1}],
        6:[{0: 4, 1: 1}],
        7:[{0: 3, 1: 2}],
        8:[{1: 3, 0: 2}],
        9:[{1: 4, 0: 1}],
        10:[{1: 3, 0: 1, 2: 1}],
        11:[{1: 3, 0: 2}],
        12:[{1: 3, 0: 2}],
        13:[{1: 3, 0: 2}],
        14:[{1: 3, 0: 2}],
        15:[{1: 3, 0: 2}],
        16:[{1: 3, 0: 2}],
    },
    'blue':{
        1:[{0: 2},{1: 1, 0: 1}],
        2:[{0: 2},{0: 1, 1: 1}],
        3:[{0: 1, 1: 1},{0: 2},{1: 2}],
        4:[{0: 1, 1: 1},{0: 2},{1: 2},{0: 1, 2: 1}],
        5:[{0: 1, 1: 1},{1: 2},{0: 1, 2: 1},{0: 2}],
        6:[{0: 1, 1: 1},{0: 1, 2: 1},{2: 1, 1: 1},{1: 2},{0: 2}],
        7:[{0: 1, 1: 1},{2: 1, 0: 1},{1: 2},{2: 1, 1: 1}],
        8:[{2: 1, 1: 1},{0: 1, 1: 1},{1: 2},{0: 1, 2: 1},{3: 1, 1: 1}],
        9:[{2: 1, 1: 1},{0: 1, 1: 1},{1: 2},{2: 1, 0: 1},{3: 1, 1: 1}],
        10:[{2: 1, 1: 1},{1: 2},{3: 1, 1: 1},{2: 1, 3: 1},{2: 1, 0: 1},{1: 1, 0: 1}],
        11:[{2: 1, 1: 1}],
        12:[{2: 1, 1: 1}],
        13:[{2: 1, 1: 1}],
        14:[{2: 1, 1: 1}],
        15:[{2: 1, 1: 1}],
        16:[{2: 1, 1: 1}],
        
    }
}

# data_times = {
#     'red':{
#         1:[{0:5}],
#         2:[{0:4,1:1}],
#         3:[ {0:3,1:2},{0:4,1:1}],
#         4:[{0: 3, 1: 2},{0: 4, 1: 1}],
#         5:[{1: 3, 0: 2},{0: 3, 2: 1, 1: 1}],
#         6:[{0: 3, 1: 2},{0: 3, 2: 1, 1: 1}],
#         7:[{1: 3, 2: 1, 0: 1},{2: 2, 1: 2, 0: 1}],
#         8:[{1: 3, 2: 1, 0: 1},{1: 2, 0: 2, 2: 1}],
#         9:[{1: 2, 2: 2, 0: 1},{1: 2, 0: 2, 2: 1}],
#         10:[{1: 2, 2: 2, 0: 1},{1: 2, 0: 1, 2: 1, 3: 1}]
#     },
#     'blue':{
#         1:[{0: 2},{1: 1, 0: 1}],
#         2:[{0: 2},{0: 1, 1: 1}],
#         3:[{0: 1, 1: 1},{0: 2},{1: 2}],
#         4:[{0: 1, 1: 1},{0: 2},{1: 2},{0: 1, 2: 1}],
#         5:[{0: 1, 1: 1},{1: 2},{0: 1, 2: 1},{0: 2}],
#         6:[{0: 1, 1: 1},{0: 1, 2: 1},{2: 1, 1: 1},{1: 2},{0: 2}],
#         7:[{0: 1, 1: 1},{2: 1, 0: 1},{1: 2},{2: 1, 1: 1}],
#         8:[{2: 1, 1: 1},{0: 1, 1: 1},{1: 2},{0: 1, 2: 1},{3: 1, 1: 1}],
#         9:[{2: 1, 1: 1},{0: 1, 1: 1},{1: 2},{2: 1, 0: 1},{3: 1, 1: 1}],
#         10:[{2: 1, 1: 1},{1: 2},{3: 1, 1: 1},{2: 1, 3: 1},{2: 1, 0: 1},{1: 1, 0: 1}]
#     }
# }

class DLT(Lottery): 
    def __init__(self): 
        #self.__url = 'http://datachart.500.com/dlt/history/newinc/history.php?start=%s&end=%s' % (start,end)
        self.__red_numbers = []
        self.__blue_numbers = []
        self.__count = 0

    @property
    def Red_Numbers(self): 
        return self.__red_numbers

    @property
    def Blue_Numbers(self): 
        return self.__blue_numbers

    @property
    def Count(self): 
        return self.__count

    def search_data_from_net(self,start,end):
        url = 'http://datachart.500.com/dlt/history/newinc/history.php?start=%s&end=%s' % (start,end)
        r = requests.get(url)                     
        r.encoding='utf-8'
        text=r.text
        soup = BeautifulSoup(text, "html.parser")
        tbody=soup.find('tbody',id="tdata")
        tr=tbody.find_all('tr')
        td=tr[0].find_all('td')
        count = len(tr)
        red_numbers = []
        blue_numbers = []
        for page in range(0,count):
            td=tr[page].find_all('td')
            redNumbers = [int(td[1].text),int(td[2].text),int(td[3].text),int(td[4].text),int(td[5].text)]
            blueNumbers = [int(td[6].text),int(td[7].text)]
            red_numbers.append(redNumbers)
            blue_numbers.append(blueNumbers)
        self.__blue_numbers = blue_numbers
        self.__red_numbers = red_numbers
        self.__count = count

    def search_data_from_csv(self,csv_file):
        with open(csv_file,'r') as csvfile: 
            reader = csv.reader(csvfile)
            print(reader)
            for row in reader: 
                if row and row[0] != '期号':
                    self.__count += 1
                    self.__red_numbers.append([int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5])])
                    self.__blue_numbers.append([int(row[6]),int(row[7])])


    def red_numbers_appear_times(self): 
        dic = {}
        for i in range(1,36): 
            dic[i] = 0
        for numbers in self.__red_numbers: 
            for num in numbers: 
                dic[num] += 1
        return dic

    def blue_numbers_appear_times(self): 
        dic = {}
        for i in range(1,13): 
            dic[i] = 0
        for numbers in self.__blue_numbers: 
            for num in numbers: 
                dic[num] += 1
        return dic

    def numbers_appear_time_in_last_periods(self,index,periods,mode='red'):
        Dic = {}
        if mode == 'red': 
            data = self.__red_numbers[index:index+periods]
            for i in range(1,36): 
                 Dic[i] = 0
        elif mode == 'blue': 
            data = self.__blue_numbers[index:index+periods]
            for i in range(1,13): 
                Dic[i] = 0
        else: 
            raise Exception('Mode error')

        for numbers in data: 
            for num in numbers: 
                Dic[num] += 1
        returnDic = {}
        for key,value in Dic.items(): 
            if value not in returnDic.keys(): 
                returnDic[value] = []
            returnDic[value].append(key)
        return returnDic   
    
    def numbers_appear_time_in_last_periods_for_index(self,index,periods,mode='red'):
        Dic = {}
        if mode == 'red': 
            data = self.__red_numbers[index:index+periods]
            for i in range(1,36): 
                 Dic[i] = 0
        elif mode == 'blue': 
            data = self.__blue_numbers[index:index+periods]
            for i in range(1,13): 
                Dic[i] = 0
        else: 
            raise Exception('Mode error')

        for numbers in data: 
            for num in numbers: 
                Dic[num] += 1
        returnDic = {}
        for key,value in Dic.items(): 
            if value not in returnDic.keys(): 
                returnDic[value] = []
            returnDic[value].append(key)
        return returnDic         

    # 中奖号码，在之前期数中出现的次数频率，
    def numbers_last_appear_times_probability(self,periods,mode='red'):
        returnDic = {}
        if mode == 'red': 
            data = self.__red_numbers
        elif mode == 'blue': 
            data = self.__blue_numbers
        else:
            raise Exception('mode error')
        for index in range(0,len(data)-periods+1): 
            current_red = data[index]
            last_red_numbers = data[index+1:index+periods+1]
            dic = self.__number_last_appaer_time_probability(current_red,last_red_numbers,mode)
            for key,value in dic.items(): 
                if key not in returnDic.keys(): 
                    returnDic[key] = 0
                returnDic[key] += value
        return returnDic

    def search_frency_from_last(self,index,periods,mode='red'):
        beegoFlag = False
        if mode == 'red': 
            current_red = self.__red_numbers[index]
            last_data = self.__red_numbers[index+1:index+periods+1]
        elif mode == 'blue':
            current_red = self.__blue_numbers[index]
            last_data = self.__blue_numbers[index+1:index+periods+1]
        #thoery_data_frency = thoery_data[mode][periods]
        data_time = data_times[mode][periods]
        returnDic = {}
        for num in current_red: 
            returnDic[num] = 0
        for data in last_data: 
            for num in current_red: 
                if num in data: 
                    returnDic[num] += 1
        returnList = []
        for _,value in returnDic.items():
            returnList.append(value)
        counter = Counter(returnList)
        if counter in data_time: 
            beegoFlag = True
        return current_red,sorted(returnList),beegoFlag

    def number_last_appear_theory_times(self,periods,mode='red'): 
        dic = self.numbers_last_appear_times_probability(periods,mode)
        count = self.__count
        returnDic = {}
        for key,value in dic.items(): 
            returnDic[key] = value / count
        return returnDic

    def number_next_appear_all(self,period,mode='red'): 
        data = self.numbers_appear_time_in_last_periods(period,mode)
        data_time = data_times[mode][period]
        nums = []
        for item in data_time: 
            if set(item.keys()).issubset(set(data.keys())): 
                data_list = []
                for key,value in item.items(): 
                    temp_data = list(combinations(data[key],value))
                    data_list.append(temp_data)
                count = len(data_list)
                
                if count == 1: 
                    for d in data_list[0]: 
                        d = tuple(sorted(d))
                        nums.append(d)
                elif count == 2: 
                    for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            d = tuple(sorted(d1+d2))
                            nums.append(d)
                elif count == 3: 
                     for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            for d3 in data_list[2]:
                                d = tuple(sorted(d1+d2+d3))
                                nums.append(d)
                elif count == 4: 
                    for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            for d3 in data_list[2]:
                                for d4 in data_list[3]:
                                    d = tuple(sorted(d1+d2+d3+d4))
                                    nums.append(d)
                elif count == 5: 
                    for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            for d3 in data_list[2]:
                                for d4 in data_list[3]:
                                    for d5 in data_list[4]:
                                        d = tuple(sorted(d1+d2+d3+d4+d5))
                                        nums.append(d)
        return nums 
    
    def number_next_appear_all_real(self,index,period,beego_times,mode='red'): 
        data = self.numbers_appear_time_in_last_periods(index,period,mode)
        data_time = beego_times[period]
        nums = []
        for item in data_time: 
            if set(item.keys()).issubset(set(data.keys())): 
                data_list = []
                for key,value in item.items(): 
                    temp_data = list(combinations(data[key],value))
                    data_list.append(temp_data)
                count = len(data_list)
                
                if count == 1: 
                    for d in data_list[0]: 
                        d = tuple(sorted(d))
                        nums.append(d)
                elif count == 2: 
                    for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            d = tuple(sorted(d1+d2))
                            nums.append(d)
                elif count == 3: 
                     for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            for d3 in data_list[2]:
                                d = tuple(sorted(d1+d2+d3))
                                nums.append(d)
                elif count == 4: 
                    for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            for d3 in data_list[2]:
                                for d4 in data_list[3]:
                                    d = tuple(sorted(d1+d2+d3+d4))
                                    nums.append(d)
                elif count == 5: 
                    for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            for d3 in data_list[2]:
                                for d4 in data_list[3]:
                                    for d5 in data_list[4]:
                                        d = tuple(sorted(d1+d2+d3+d4+d5))
                                        nums.append(d)
        return nums 
    
    def number_next_appear_all_real_for_index(self,index,period,beego_times,mode='red'): 
        data = self.numbers_appear_time_in_last_periods_for_index(index,period,mode)
        data_time = beego_times[period]
        nums = []
        for item in data_time: 
            if set(item.keys()).issubset(set(data.keys())): 
                data_list = []
                for key,value in item.items(): 
                    temp_data = list(combinations(data[key],value))
                    data_list.append(temp_data)
                count = len(data_list)
                
                if count == 1: 
                    for d in data_list[0]: 
                        d = tuple(sorted(d))
                        nums.append(d)
                elif count == 2: 
                    for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            d = tuple(sorted(d1+d2))
                            nums.append(d)
                elif count == 3: 
                     for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            for d3 in data_list[2]:
                                d = tuple(sorted(d1+d2+d3))
                                nums.append(d)
                elif count == 4: 
                    for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            for d3 in data_list[2]:
                                for d4 in data_list[3]:
                                    d = tuple(sorted(d1+d2+d3+d4))
                                    nums.append(d)
                elif count == 5: 
                    for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            for d3 in data_list[2]:
                                for d4 in data_list[3]:
                                    for d5 in data_list[4]:
                                        d = tuple(sorted(d1+d2+d3+d4+d5))
                                        nums.append(d)
        return nums 

            
    def number_section(self,current_num,min_num,max_num): 
        if min(current_num) >= min_num and max(current_num) <= max_num: 
            return True
        else: 
            return False

    def number_section_frency(self,numList):
        temList1 = []
        chazhiList = [] 
        for nums in numList: 
            minNum = min(nums)
            maxNum = max(nums)
            chazhi = maxNum - minNum
            temList1.append('%s_%s' %(minNum,maxNum))
            chazhiList.append(chazhi)
        return Counter(temList1),Counter(chazhiList)

    def number_no_apear_in_periods(self,index,last_periods,mode='red'): 
        if mode == 'red': 
            numbers = self.Red_Numbers
        else: 
            numbers = self.Blue_Numbers
        nums = numbers[index]
        last_nums = numbers[index+1:last_periods+index +1]
        temp_nums = set()
        for last in last_nums: 
            temp_nums = temp_nums.union(set(last))
        numSet = set(nums)
        if len(numSet.intersection(temp_nums)) > 0: 
            return False,len(temp_nums)
        else: 
            return True,len(temp_nums)


    def number_has_in_periods(self,index,start_periods,end_periods,mode='red'): 
        if mode == 'red': 
            numbers = self.Red_Numbers
        else: 
            numbers = self.Blue_Numbers
        nums = numbers[index]
        last_nums = numbers[index+1+start_periods:index+1+end_periods]
        last_set = set()
        for last in last_nums:
            last_set = last_set.union(set(last)) 



    def __number_last_appaer_time_probability(self,current_num,last_numbers,mode='red'):
        dic = {}
        if mode == 'red': 
            if len(current_num) != 5: 
                raise Exception('blue data error')
        elif mode == 'blue': 
            if len(current_num) != 2: 
                raise Exception('blue data error')
        else: 
            raise Exception('mode error')
        for reds in last_numbers: 
            for num in current_num: 
                if num in reds: 
                    if num not in dic.keys(): 
                        dic[num] = 0 
                    dic[num] += 1
                else: 
                    if num not in dic.keys(): 
                        dic[num] = 0 
        returnDic = {}
        for _,value in dic.items():
            if value not in returnDic.keys():
                returnDic[value] = 0
            returnDic[value] +=1
        return returnDic

    


   
