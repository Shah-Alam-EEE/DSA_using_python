# Problem: https://www.codingninjas.com/studio/problems/check-armstrong_589?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *
def is_armstrong(n):
    count=0
    pow_sum=0
    r=n
    con_a=n
    while n>0:
        n=n//10
        count=count+1
    while con_a>0:
        d=con_a%10
        pow_sum=pow_sum + pow(d,count)
        con_a=con_a//10

    if pow_sum==r:
        return "true"
    else:
        return "false"

if __name__=="__main__":
    n=int(input())
    print(is_armstrong(n))

# Time: O(n) where n is the num of digit. Space: O(1)