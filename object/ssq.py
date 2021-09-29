from lottery import Lottery

from bs4 import BeautifulSoup   #引用BeautifulSoup库
import requests                 #引用requests
import os                       #os
import pandas as pd
import csv
import codecs
import collections

class SSQ(Lottery): 
    def __init__(self,start,end): 
        self.__url = 'http://datachart.500.com/ssq/history/newinc/history.php?start=%s&end=%s' % (start,end)
        self.__red_numbers = []
        self.__blue_numbers = []

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
            redNumbers = [int(td[1].text),int(td[2].text),int(td[3].text),int(td[4].text),int(td[5].text)]
            blueNumbers = [int(td[6].text),int(td[7].text)]
            red_numbers.append(redNumbers)
            blue_numbers.append(blueNumbers)
        self.__blue_numbers = blue_numbers
        self.__red_numbers = red_numbers

    def search_data_from_csv(self):
        pass

    def red_numbers_appear_times(self): 
        dic = {}
        for i in range(1,37): 
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

    

   
