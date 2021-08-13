# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:56:09 2021

@author: Dhaniel Lukman

mean dataset
"""

w3_tuple = (1,2,3,'4',False,4,5,'X',6,6,23,'A')

if all(isinstance(i, int) for i in w3_tuple):
    mr_mean = sum(w3_tuple) / len(w3_tuple)
    print(mr_mean)
else:
    w3_num = 0
    w3_count = 0
    w3_nan = 0
    
    for i in range(len(w3_tuple)):
        if type(w3_tuple[i]) == int:
            w3_num, w3_count = (w3_num+w3_tuple[i], w3_count + 1)
        else:
            print(w3_tuple[i], 'is not a number')
            (w3_num, w3_nan + 1)
    
mr_mean = w3_num / w3_count

print('Original tuple: ',w3_tuple)
print('Mean is:' , mr_mean)
print('Valid numbers in tuple: ',w3_count)