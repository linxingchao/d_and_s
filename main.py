from object.dlt import DLT
from object.ssq import SSQ
from os import path

def dlt_theory_appear_times(): 
    dlt = DLT(1,21112)
    dlt.search_data_from_net()
    red_numbers = dlt.Red_Numbers
    blue_numbers = dlt.Blue_Numbers

if __name__ == '__main__': 
    dlt = DLT(1,21112)
    dlt.search_data_from_net()
    print(len(dlt.Blue_Numbers))