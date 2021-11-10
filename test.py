

if __name__ == '__main__': 
    set1 = set([3,4,5])
    set2 = set([1,2,6,7,9])
    set3 = set2.intersection(set1)
    set4 = set1.union(set2)
    print(set4)
    print(set3)
    print(len(set4))
    if set3: 
        print(True)
    else: 
        print(False)