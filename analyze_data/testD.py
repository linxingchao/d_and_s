from bs4 import BeautifulSoup   #引用BeautifulSoup库
import requests                 #引用requests
import os                       #os
import pandas as pd
import csv
import codecs
import collections
from collections import Counter
#最新的号码再过去出现的频率，pointNumbers 过去的号码 last_numbers 最新的号码
def last_appear_red(pointNumbers,last_numbers): 
    dicCount = {}
    for num in pointNumbers: 
        dicCount[num] = 0
    for points in last_numbers:
        for key,_ in dicCount.items(): 
            if key in points: 
                dicCount[key] += 1
    return dicCount

def last_appear_blue(blueNumbers,lastBlueNumbers): 
    dicCount = {}
    for num in blueNumbers: 
        dicCount[num] = 0
    for nums in lastBlueNumbers: 
        for key,_ in dicCount.items(): 
            if key in nums: 
                dicCount[key]+=1
    return dicCount

# 号码最近出现的频次 ，data 一期或多期数据，period 过去的期数
def search_last_frequency_red(data,period): 
    dic = {}
    count = len(data) + 1
    for index in range(period + 1,count): 
        last_points = [data[x] for x in range(index-period,index)]
        returnDic = last_appear_red(data[index],last_points)
        for _,value in returnDic.items(): 
            if value not in dic.keys(): 
                dic[value] = 0
            dic[value] += 1
    return dic

def search_last_frequency_blue(data,period):
    dic = {}
    count = len(data)+1
    for index in range(period + 1, count): 
        last_blue = [data[x] for x in range(index-period,index)]
        returnDic = last_appear_blue(data[index],last_blue)
        for _,value in returnDic.items(): 
            if value not in dic.keys(): 
                dic[value] = 0
            dic[value] += 1
    return dic



def search_last_theory_frequency_red(data,count,period): 
    dicData = search_last_frequency_red(data,period)
    dic = {}
    for key,value in dicData.items(): 
        dic[key] = value / count * 5
    return dic

def search_last_theory_frequency_blue(data,count,period): 
    dicData = search_last_frequency_red(data,period)
    dic = {}
    for key,value in dicData.items(): 
        dic[key] = value / count * 2
    return dic


def search_last_appear_frequency_red(data): 
    frenDic = {}
    for i in range(1,36): 
        frenDic[i] = 0
    for key,value in data.items(): 
        for item in value: 
            frenDic[item] += 1
    return frenDic

def search_last_appear_times_red(data): 
    times = {0:[]}
    points = {}
    for i in range(1,36): 
        points[i] = 0
    fenndic = search_last_appear_frequency_red(data)
    for key,value in fenndic.items():
        if value not in times.keys(): 
            times[value] = []
        times[value].append(key)
        points[key] = 1
    for key,value in points.items(): 
        if value == 0: 
            times[0].append(key)
    return times

def search_data(start=7001,end=21111): 
    url='http://datachart.500.com/dlt/history/newinc/history.php?start=%s&end=%s' % (start,end)
    r = requests.get(url)                     
    r.encoding='utf-8'
    text=r.text
    soup = BeautifulSoup(text, "html.parser")
    tbody=soup.find('tbody',id="tdata")
    tr=tbody.find_all('tr')
    td=tr[0].find_all('td')
    count = len(tr)
    points_red = {}
    points_blue = {}
    for page in range(0,count):
        td=tr[page].find_all('td')
        redNumbers = [int(td[1].text),int(td[2].text),int(td[3].text),int(td[4].text),int(td[5].text)]
        blueNumbers = [int(td[6].text),int(td[7].text)]
        points_red[count-page] = redNumbers
        points_blue[count-page] = blueNumbers
    return points_red,points_blue,count * 5

if __name__ == '__main__':
    # Points = search_data()
    # points_red = Points[0]
    # count = Points[2]
    #dic = search_last_frequency(frontPoints,3,count+1)
    end = 21112
   

    currentRed = search_data(end-3,end-3)[0]
    data = search_data(end-99,end)[1]
    
    #print(search_last_appear_times_red(data))
    #currentRed = search_data(end-,end-1)[0]
    # datalist = []
    for i in range(100): 
        start = end - i
        currentRed = search_data(start,start)[1][1]
        data = search_data(start-1,start-1)[1]
        dic = search_last_appear_times_red(data)
        returnDic = {'data':[]}
        for item in currentRed: 
            for key,value in dic.items():
                if item in value:
                    str = '%s出现得次数' % item
                    returnDic['data'].append(key)
        print(i,returnDic)
    
        #datalist.append(returnDic)

    
   
