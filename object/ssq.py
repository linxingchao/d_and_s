from object.lottery import Lottery

from bs4 import BeautifulSoup   #引用BeautifulSoup库
import requests                 #引用requests
import os                       #os
import pandas as pd
import csv
import codecs
import collections
from collections import Counter

from itertools import combinations

data_times = {
    'red':{
        1:[{0: 6},{0: 4, 1: 2},{0: 5, 1: 1}],
        2:[{0: 5, 1: 1},{0: 3, 1: 3},{0: 4, 1: 2},{0: 4, 1: 1, 2: 1},\
            {0: 3, 1: 2, 2: 1},{1: 4, 0: 2}],
        3:[{0: 5, 1: 1},{0: 3, 1: 2, 2: 1},{0: 4, 1: 2},{1: 3, 0: 3},{0: 4, 2: 1, 1: 1},\
            {1: 3, 0: 2, 2: 1},{1: 4, 0: 2}],
        4:[{0: 3, 1: 2, 2: 1},{1: 3, 0: 2, 2: 1},{1: 3, 0: 3},{1: 4, 0: 2},\
            {0: 4, 1: 2},{0: 4, 2: 1, 1: 1}],
        #5:[{1: 3, 0: 2, 2: 1},]
        

    }
}


class SSQ(Lottery): 
    def __init__(self,start='04001',end='21118'): 
        self.__url = 'http://datachart.500.com/ssq/history/newinc/history.php?start=%s&end=%s' % (start,end)
        self.__red_numbers = []
        self.__blue_numbers = []
        self.__count = 0

    @property
    def Red_Numbers(self): 
        return self.__red_numbers

    @property
    def Blue_Numbers(self): 
        return self.__blue_numbers

    def search_data_from_net(self):
        r = requests.get(self.__url)                     
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
            redNumbers = [int(td[1].text),int(td[2].text),int(td[3].text),int(td[4].text),int(td[5].text),int(td[6].text)]
            blueNumbers = [int(td[7].text)]
            red_numbers.append(redNumbers)
            blue_numbers.append(blueNumbers)
        self.__blue_numbers = blue_numbers
        self.__red_numbers = red_numbers
        self.__count = count

    def search_data_from_csv(self):
        pass

    def red_numbers_appear_times(self): 
        dic = {}
        for i in range(1,34): 
            dic[i] = []
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


    def numbers_appear_time_in_last_periods(self,periods,mode='red'):
        Dic = {}
        if mode == 'red': 
            data = self.__red_numbers[0:periods]
            for i in range(1,36): 
                 Dic[i] = 0
        elif mode == 'blue': 
            data = self.__blue_numbers[:periods]
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
        return current_red,returnList,beegoFlag


    def number_last_appear_theory_times(self,periods,mode='red'): 
        dic = self.numbers_last_appear_times_probability(periods,mode)
        count = self.__count
        returnDic = {}
        for key,value in dic.items(): 
            returnDic[key] = value / count
        return returnDic

    def number_next_appear_all(self,period,mode='red'): 
        data = self.numbers_appear_time_in_last_periods(period)
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
                elif count == 5: 
                    for d1 in data_list[0]: 
                        for d2 in data_list[1]: 
                            for d3 in data_list[2]:
                                for d4 in data_list[3]:
                                    for d5 in data_list[4]:
                                        for d6 in data_list[5]:
                                            d = tuple(sorted(d1+d2+d3+d4+d5))
                                            nums.append(d)
        return nums 

            



    def __number_last_appaer_time_probability(self,current_num,last_numbers,mode='red'):
        dic = {}
        if mode == 'red': 
            if len(current_num) != 6: 
                raise Exception('blue data error')
        elif mode == 'blue': 
            if len(current_num) != 1: 
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

    

   
