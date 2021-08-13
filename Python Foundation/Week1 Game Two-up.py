# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 13:26:09 2021

@author: Dhaniel Lukman
"""

import random as r

# Translate 1 as Heads and 2 as Tails
coin_1 = 'Heads' if r.randint(1, 2) == 1 else 'Tails'
coin_2 = 'Heads' if r.randint(1, 2) == 1 else 'Tails'


print('Coin 1: ',coin_1)
print('Coin 2: ',coin_2)


# Check the logic
if coin_1 == coin_2 == 'Heads':
    print('Spinner Wins! Two heads!')
elif coin_1 == coin_2 == 'Tails':
    print('Spinner Loses! Two tails!')
else:
    print('Throw again')

print('Thanks for playing')