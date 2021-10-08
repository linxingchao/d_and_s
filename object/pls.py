from typing import Counter
from object.lottery import Lottery

from bs4 import BeautifulSoup   #引用BeautifulSoup库
import requests                 #引用requests
import os                       #os
import pandas as pd
import csv
import codecs
import collections


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

    # def search_frency_from_last(self,index,periods,mode='red'):
    #     beegoFlag = False
    #     if mode == 'red': 
    #         current_red = self.__red_numbers[index]
    #         last_data = self.__red_numbers[index+1:index+periods+1]
    #     elif mode == 'blue':
    #         current_red = self.__blue_numbers[index]
    #         last_data = self.__blue_numbers[index+1:index+periods+1]
    #     thoery_data_frency = thoery_data[mode][periods]
    #     returnDic = {}
    #     for num in current_red: 
    #         returnDic[num] = 0
    #     for data in last_data: 
    #         for num in current_red: 
    #             if num in data: 
    #                 returnDic[num] += 1
    #     returnList = []
    #     for _,value in returnDic.items():
    #         returnList.append(value)
    #     counter = Counter(returnList)
    #     beegoFlag = True
    #     for key,value in counter.items(): 
    #         if key in thoery_data_frency.keys() and value <= thoery_data_frency[key]:
    #             pass
    #         else: 
    #             beegoFlag = False
    #             break
    #     return current_red,returnList,beegoFlag

    
    def number_last_appear_theory_times(self,periods,mode='first'): 
        counts = self.numbers_last_appear_times_probability(periods,mode)
        counter = Counter(counts)
        returnDic = {}
        for key,value in counter.items(): 
            returnDic[key] = value / self.count
        return returnDic


    def __number_last_appaer_time_probability(self,current_num,last_numbers,mode='first'):
        dic = {}
        count = 0
        for num in last_numbers: 
            if num == current_num: 
                count += 1
        return count
            

