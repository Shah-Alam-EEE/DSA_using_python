
# Problem: https://leetcode.com/problems/palindrome-number/

def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    rev=0
    num=x
    while x>0:
        rev=(rev*10)+x%10
        x=x//10

    if rev==num:
        if pow(-2,31)<=rev<=pow(2,31)-1:
            return True
        else:
            return False
    else:
        return False

# Time: O(n) where n is the num of digit . Space: O(1)    