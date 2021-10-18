from object.dlt import DLT
from object.ssq import SSQ
from object.pls import PLS
from object.dlt import data_times
from os import path
import csv
from collections import Counter
from bs4 import BeautifulSoup   #引用BeautifulSoup库
import requests                 #引用requests

from itertools import combinations
import time
import pandas


if __name__ == '__main__': 
    ssq = SSQ(end='21118')
    ssq.search_data_from_net()

    for i in range(1,21): 
        print(i,ssq.number_last_appear_theory_times(i))