# Problem: https://www.codingninjas.com/studio/problems/print-1-to-n_628290?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

from typing import List
a=[]
def printNos(x: int) -> List[int]: 
    # Write your code here
    a.append(x)
    if x==1:
        return a[::-1]
    return printNos(x-1)