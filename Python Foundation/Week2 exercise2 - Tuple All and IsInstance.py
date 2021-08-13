# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:44:07 2021

@author: Dhaniel Lukman

Loops and Input
Tuple, all and isintance
"""

user_no = eval(input('Input 5 numbers separated by comma:'))
while len(user_no) < 5:
    user_no = eval(input('Input 5 numbers separated by comma:'))

sum_no = 0 
for i in (user_no):
    sum_no += i
    print(sum_no)
    


# Understanding all
a = 'A'
all(a)

# one false value
mylist = [0, 1, 1]
x = all(mylist)
print(x)

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))


# checking if all in the tuple is a number
all(isinstance(x, int) for x in user_no)



# solution 
nums = eval(input('Please enter at least 5 numbers each separated by comma: '))
print('The numbers entered are ', nums)

# Check whether we have enough numbers
while len(nums) < 5:
    print('You need to enter at least 5 numbers!')
    nums = eval(input('Please enter at least 5 numbers each separated by comma: '))
    print('The numbers entered are ', nums)

numsum = 0
count = 0

#if all numbers are integers, add them up
if all(isinstance(i, int) for i in nums):
    numsum = sum(nums)
else:
    for i in range(len(nums)):
        numsum,count = (numsum+nums[i],count) if (type(nums[i]) == int) else (numsum, count+1)

print('The total of the numbers entered %d with %d NaNs ' % (numsum, count))
