# Problem: https://www.codingninjas.com/studio/problems/check-prime_624934?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

from math import *
from collections import *
from sys import *
from os import *
def is_prime(n):
    if n==1:
        return "NO"
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return "NO"
    return "YES"

if __name__=="__main__":
    n=int(input())
    print(is_prime(n)) 

# Time: O(sqrt(n)). Space: O(1)