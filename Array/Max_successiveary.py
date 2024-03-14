# Problem: https://www.codingninjas.com/studio/problems/longest-successive-elements_6811740?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

# Naive approach: Time:O(n^2), Space:O(1)

from typing import *

def longestSuccessiveElements(a : List[int]) -> int:
    a.sort()
    maxlen=1
    # Write your code here.
    for i in range(len(a)):
        currlen=1
        for j in range(i,len(a)-1):
            if a[j]==a[j+1]:
                continue
            elif a[j]==a[j+1]-1:
                currlen=currlen+1
                maxlen=max(currlen,maxlen)
            else:
                break
    return maxlen


# optimal approach: Time: O(nlog(n)), space: O(1)

def longestSuccessiveElements(a : List[int]) -> int:
    a.sort()
    maxlen=1
    currlen=1
   
    for j in range(len(a)-1):
        if a[j]==a[j+1]:
            continue
        elif a[j]==a[j+1]-1:
            currlen=currlen+1
            maxlen=max(currlen,maxlen)
        else:
            currlen=1
        
    return maxlen