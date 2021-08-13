# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 13:11:49 2021

@author: Dhaniel Lukman

Ternary Expressions
"""

#ask for two numbers
number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))

check_results = number_1 if number_1 > number_2 else number_2
print(check_results, 'is larger')


my_name = 'Dhaniel'
name_1 = input('Please enter your name:')

check_name = 'Same as me' if my_name.upper() == name_1.upper() else 'Oppps'

print(check_name)