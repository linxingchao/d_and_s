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

numbers = {
    'first':{
        1:{
            0:1
        },
        2:{
            0:1,1:1
        },
        3:{
            0:1,1:1
        },
        4:{
            0:1,1:1
        },
        5:{
            0:1,1:1
        },
        6:{
            0:1,1:1,2:1
        },
        7:{
            0:1,1:1,2:1
        },
        8:{
            0:1,1:1,2:1
        },
        9:{
            0:1,1:1,2:1
        },
        10:{
            0:1,1:1,2:1
        },
        11:{
            0:1,1:1,2:1
        },
        12:{
            0:1,1:1,2:1
        },
        13:{
            0:1,1:1,2:1
        },
        14:{
            0:1,1:1,2:1,3:1
        },
        15:{
            0:1,1:1,2:1,3:1
        },
        16:{
            0:1,1:1,2:1,3:1
        },
        17:{
            0:1,1:1,2:1,3:1
        },
        18:{
            0:1,1:1,2:1,3:1
        },
        19:{
            0:1,1:1,2:1,3:1
        },
        20:{
            0:1,1:1,2:1,3:1
        },
    },
    'second':{
        1:{
            0:1
        },
        2:{
            0:1,1:1
        },
        3:{
            0:1,1:1
        },
        4:{
            0:1,1:1
        },
        5:{
            0:1,1:1
        },
        6:{
            0:1,1:1,2:1
        },
        7:{
            0:1,1:1,2:1
        },
        8:{
            0:1,1:1,2:1
        },
        9:{
            0:1,1:1,2:1
        },
        10:{
            0:1,1:1,2:1
        },
        11:{
            0:1,1:1,2:1
        },
        12:{
            0:1,1:1,2:1
        },
        13:{
            0:1,1:1,2:1
        },
        14:{
            0:1,1:1,2:1,3:1
        },
        15:{
            0:1,1:1,2:1,3:1
        },
        16:{
            0:1,1:1,2:1,3:1
        },
        17:{
            0:1,1:1,2:1,3:1
        },
        18:{
            0:1,1:1,2:1,3:1
        },
        19:{
            0:1,1:1,2:1,3:1
        },
        20:{
            0:1,1:1,2:1,3:1
        },
    },
    'third':{
        1:{
            0:1,1:1
        },
        2:{
            0:1,1:1
        },
        3:{
            0:1,1:1
        },
        4:{
            0:1,1:1
        },
        5:{
            0:1,1:1
        },
        6:{
            0:1,1:1,2:1
        },
        7:{
            0:1,1:1,2:1
        },
        8:{
            0:1,1:1,2:1
        },
        9:{
            0:1,1:1,2:1
        },
        10:{
            0:1,1:1,2:1
        },
        11:{
            0:1,1:1,2:1
        },
        12:{
            0:1,1:1,2:1
        },
        13:{
            0:1,1:1,2:1,3:1
        },
        14:{
            0:1,1:1,2:1,3:1
        },
        15:{
            0:1,1:1,2:1,3:1
        },
        16:{
            0:1,1:1,2:1,3:1
        },
        17:{
            0:1,1:1,2:1,3:1
        },
        18:{
            0:1,1:1,2:1,3:1
        },
        19:{
            0:1,1:1,2:1,3:1
        },
        20:{
            0:1,1:1,2:1,3:1
        },
    }

}

data_times = {
    1:[{0:1}],
    2:[{0:1}],
    3:[{0:1}],
    4:[{0:1}],
    5:[{0:1}],
    6:[{0:1}],
    7:[{0:1},{2:1}],
    8:[{0:1},{1:1}],
    9:[{0:1},{1:1}],
    10:[{0:1},{1:1}],
    11:[{0:1},{1:1}],
    12:[{0:1},{1:1}],
    13:[{0:1},{1:1}],
    14:[{0:1},{1:1},{2:1}],
    15:[{0:1},{1:1},{2:1}],
    16:[{1:1},{2:1},],
    17:[{1:1},{2:1}],
    18:[{1:1},{2:1}],
    19:[{1:1},{2:1}],
    20:[{1:1},{2:1}],

}
class PLS: 
    def __init__(self,limit=100): 
        self.__limit=limit
        self.firstNumbers = []
        self.secondNumbers = []
        self.thirdNumbers = []
        self.countValue = []
        self.count = 0

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
            self.firstNumbers.append(int(numbers[0]))
            self.secondNumbers.append(int(numbers[1]))
            self.thirdNumbers.append(int(numbers[2]))
            self.countValue.append(int(tds[2].text))
        self.count = count - 2

    def numbers_appear_times(self,mode='first'):
        if mode == 'first': 
            data = self.firstNumbers
        elif mode == 'second': 
            data = self.secondNumbers
        elif mode == 'third': 
            data = self.thirdNumbers
        else: 
            raise Exception('mode error')
            
        counter = Counter(data)
        returnDic = {}
        for key,value in counter.items(): 
            returnDic[key] = value
        return returnDic
        
    def numbers_appear_time_in_last_periods(self,periods,mode='first'):
        returnDic = {}
        if mode == 'first': 
            data = self.firstNumbers[0:periods] 
        elif mode == 'second': 
           data = self.secondNumbers[0:periods]
        elif mode == 'third': 
           data = self.thirdNumbers[0:periods]
        else: 
            raise Exception('Mode error')
        returnDic = {0:[]}
        for num in range(0,10): 
            if num not in data: 
                returnDic[0].append(num)
        counter = Counter(data)
        for key,value in counter.items():
            if value not in returnDic.keys(): 
                returnDic[value] = []
            returnDic[value].append(key)
        return returnDic           

    # 中奖号码，在之前期数中出现的次数频率，
    def numbers_last_appear_times_probability(self,periods,mode='first'):
        returnDic = {}
        if mode == 'first': 
            data = self.firstNumbers
        elif mode == 'second': 
            data = self.secondNumbers
        elif mode == 'third': 
            data = self.thirdNumbers
        else:
            raise Exception('mode error')
        counts = []
        for index in range(0,len(data)-periods): 
            current_red = data[index]
            last_red_numbers = data[index+1:index+periods+1]
            count = self.__number_last_appaer_time_probability(current_red,last_red_numbers,mode)
            counts.append(count)
        return counts

    def number_last_appear_theory_times(self,periods,mode='first'): 
        counts = self.numbers_last_appear_times_probability(periods,mode)
        counter = Counter(counts)
        returnDic = {}
        for key,value in counter.items(): 
            returnDic[key] = value / self.count
        return returnDic

    def search_frency_from_last(self,index,periods,mode='first'):
        beegoFlag = False
        if mode == 'first': 
            current_red = [self.firstNumbers[index]]
            last_data = self.firstNumbers[index+1:index+periods+1]
        elif mode == 'second':
            current_red = [self.secondNumbers[index]]
            last_data = self.secondNumbers[index+1:index+periods+1]
        elif mode == 'third':
            current_red = [self.thirdNumbers[index]]
            last_data = self.thirdNumbers[index+1:index+periods+1]
        thoery_data_frency = numbers[mode][periods]
        returnDic = {}
        for num in current_red: 
            returnDic[num] = 0
        for data in last_data: 
            for num in current_red: 
                if num == data: 
                    returnDic[num] += 1
        returnList = []
        for _,value in returnDic.items():
            returnList.append(value)
        counter = Counter(returnList)
        if counter in data_times[periods]: 
            beegoFlag = True
        
        return current_red,returnList,beegoFlag

    def number_next_appear_all(self,period,mode='first'):
        data = self.numbers_appear_time_in_last_periods(period,mode)
        data_time = data_times[period]
        nums = []
        for item in data_time: 
            if set(item.keys()).issubset(set(data.keys())): 
                #data_list = []
                for key,value in item.items(): 
                    temp_data = combinations(data[key],value)
                    for t_d in temp_data:
                        nums.append(t_d)
                #ount = len(data_list)

        return nums


    def __number_last_appaer_time_probability(self,current_num,last_numbers,mode='first'):
        dic = {}
        count = 0
        for num in last_numbers: 
            if num == current_num: 
                count += 1
        return count
            

