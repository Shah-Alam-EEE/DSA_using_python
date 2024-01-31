# Problem: https://www.codingninjas.com/studio/problems/sum-of-first-n-numbers_8876068?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

sum=0
def sumFirstN(n: int) -> int:
    # Write your code here.
    global sum
    if n==0:
        return sum
    sum+=n 
    return sumFirstN(n-1)