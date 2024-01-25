# Problem: https://leetcode.com/problems/reverse-integer/

def reverse(x: int) -> int:
    sign=1
    if x<0:
        sign=-1
        x=abs(x)
    rev=0
    while x>0:
        rev=(rev*10)+x%10
        x=x//10
    if sign==-1:
        rev=rev*-1
    if pow(-2,31) <=rev and pow(2,31) -1>=rev:
        return rev
    return 0

# Time:O(n) where n is the length of the num; Space: O(1)

print(reverse(35))
         