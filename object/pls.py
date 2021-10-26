from itertools import count
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

data_times = {
    'com_6':{
        1:[{0: 2, 1: 1},{0: 3},{1: 2, 0: 1}],
        2:[{1: 2, 0: 1},{0: 2, 1: 1},{2: 1, 1: 1, 0: 1},{0: 2, 2: 1},{0: 3}],
        3:[{1: 2, 0: 1},{1: 2, 2: 1},{2: 1, 1: 1, 0: 1},{0: 2, 1: 1},{1: 3},{0: 2, 2: 1}],
        4:[{1: 2, 2: 1},{1: 2, 0: 1},{2: 1, 1: 1, 0: 1},{2: 2, 1: 1},{2: 2, 0: 1},{3: 1, 0: 1, 1: 1}],
        5:[{1: 2, 2: 1},{2: 2, 1: 1},{2: 1, 0: 1, 1: 1},{3: 1, 1: 1, 2: 1},{3: 1, 1: 1, 0: 1},{1: 2, 3: 1}],
        6:[{2: 2, 1: 1},{1: 1, 2: 1, 3: 1},{1: 2, 2: 1},{2: 2, 3: 1},{1: 2, 3: 1},{2: 1, 0: 1, 1: 1}],
        7:[],
        8:[],
        9:[],
        10:[]
    }
}

class PLS: 
    def __init__(self,limit=100): 
        self.__limit=limit
        self.numbers = []
        self.count = 0
        self.complex_num_3 = []
        self.complex_num_6 = []

    def search_data_from_net(self): 
        url = 'https://datachart.500.com/pls/history/inc/history.php?limit=%s' % self.__limit
        r = requests.get(url)                     
        r.encoding='utf-8'
        text=r.text
        soup = BeautifulSoup(text, "html.parser")
        table=soup.find('table',id="tablelist")
        trs = table.find_all('tr')
        print('hhhh ')
        count = len(trs)
        for index in range(2,count): 
            tds = trs[index].find_all('td')
            numbers = tds[1].text.split(' ')
            temp_nums = sorted([int(numbers[0]),int(numbers[1]),int(numbers[2])])
            self.numbers.append(temp_nums)
            tem_counter = Counter(temp_nums)
            if len(tem_counter.keys()) == 3: 
                self.complex_num_6.append(temp_nums)
            else: 
                self.complex_num_3.append(temp_nums)
        self.count = count - 2

    def red_numbers_appear_times(self): 
        dic = {}
        for i in range(0,9): 
            dic[i] = 0
        for numbers in self.complex_num_6: 
            for num in numbers: 
                dic[num] += 1
        return dic

    def numbers_appear_time_in_last_periods(self,periods):
        Dic = {}
        data = self.complex_num_6[:periods]
        for i in range(0,9): 
            Dic[i] = 0
        for numbers in data: 
            tem_counter = Counter(numbers)
            if len(tem_counter.keys()) == 3:
                for num in numbers: 
                    Dic[num] += 1
        returnDic = {}
        for key,value in Dic.items(): 
            if value not in returnDic.keys(): 
                returnDic[value] = []
            returnDic[value].append(key)
        return returnDic           

    # 中奖号码，在之前期数中出现的次数频率，
    def numbers_last_appear_times_probability(self,periods):
        returnDic = {}
        data = self.complex_num_6
       
        for index in range(0,len(data)-periods+1): 
            current_red = data[index]
            last_red_numbers = data[index+1:index+periods+1]
            dic = self.__number_last_appaer_time_probability(current_red,last_red_numbers)
            for key,value in dic.items(): 
                if key not in returnDic.keys(): 
                    returnDic[key] = 0
                returnDic[key] += value
        return returnDic

    def search_frency_from_last(self,index,periods):
        beegoFlag = False
        current_red = self.complex_num_6[index]
        last_data = self.complex_num_6[index+1:index+periods+1]
        #thoery_data_frency = thoery_data[mode][periods]
        #data_time = data_times[mode][periods]
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
        if counter in data_times['com_6'][periods]: 
            beegoFlag = True
        return current_red,returnList,beegoFlag


    def number_last_appear_theory_times(self,periods): 
        dic = self.numbers_last_appear_times_probability(periods)
        count = self.count
        returnDic = {}
        for key,value in dic.items(): 
            returnDic[key] = value / count
        return returnDic

    def number_next_appear_all(self,period): 
        data = self.numbers_appear_time_in_last_periods(period)
        #data_time = data_times[mode][period]
        nums = []
        for item in data_times['com_6'][period]: 
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
        return nums 

            



    def __number_last_appaer_time_probability(self,current_num,last_numbers):
        dic = {}
        
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

