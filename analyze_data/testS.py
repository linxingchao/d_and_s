from bs4 import BeautifulSoup   #引用BeautifulSoup库
import requests                 #引用requests
import os                       #os
import pandas as pd
import csv
import codecs


def last_appear(pointNumbers,last_numbers): 
    dicCount = {}
    for num in pointNumbers: 
        dicCount[num] = 0
    for points in last_numbers:
        for key,_ in dicCount.items(): 
            if key in points: 
                dicCount[key] += 1
    return dicCount

def search_last_frequency(data,period,count): 
    dic = {}
    for index in range(period + 1,count): 
        last_points = [data[x] for x in range(index-period,index)]
        returnDic = last_appear(data[index],last_points)
        for _,value in returnDic.items(): 
            if value not in dic.keys(): 
                dic[value] = 0
            dic[value] += 1
    return dic


def search_last_appear_frequency(data): 
    frenDic = {}
    for i in range(1,36): 
        frenDic[i] = 0
    for key,value in data.items(): 
        for item in value: 
            frenDic[item] += 1
    return frenDic

def search_last_appear_times(data): 
    times = {0:[]}
    points = {}
    for i in range(1,36): 
        points[i] = 0
    fenndic = search_last_appear_frequency(data)
    for key,value in fenndic.items():
        if value not in times.keys(): 
            times[value] = []
        times[value].append(key)
        points[key] = 1
    for key,value in points.items(): 
        if value == 0: 
            times[0].append(key)
    return times



if __name__ == '__main__':
    lst=[]
    start = 21111-20
    start1 = '03001'
    #url='http://datachart.500.com/dlt/history/newinc/history.php?start=%s&end=21110' % start
    url = 'http://datachart.500.com/ssq/history/newinc/history.php?start=%s&end=21111' % (start) 
    r = requests.get(url)                     
    r.encoding='utf-8'
    text=r.text
    soup = BeautifulSoup(text, "html.parser")
    tbody=soup.find('tbody',id="tdata")
    tr=tbody.find_all('tr')
    td=tr[0].find_all('td')
    count = len(tr)

    for page in range(0,count):
        td=tr[page].find_all('td')
        redNumbers = [int(td[1].text),int(td[2].text),int(td[3].text),int(td[4].text),int(td[5].text),int(td[6].text)]
        blueNumber = [int(td(7).text)]   
    print(redNumbers) 
