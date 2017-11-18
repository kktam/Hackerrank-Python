#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

sum_h1 = sum(h1)
sum_h2 = sum(h2)
sum_h3 = sum(h3)

while not (sum_h1 == sum_h2 and sum_h2 == sum_h3):
    if sum_h1 > sum_h2 or sum_h1 > sum_h3:
        t = h1.pop(0)
        sum_h1 -= t
    if sum_h2 > sum_h1 or sum_h2 > sum_h3:
        t = h2.pop(0)
        sum_h2 -= t
    if sum_h3 > sum_h1 or sum_h3 > sum_h2:
        t = h3.pop(0)
        sum_h3 -= t
        
print (sum_h1)