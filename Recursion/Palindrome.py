# Problem: https://leetcode.com/problems/valid-palindrome/description/
# Recursive approach:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        f=""
        for i in s:
            if i.isalnum():
                f+=i 
        return self.helper(f)
    def helper(self,s):
        if len(s)<1:
            return True
        elif s[0]!=s[-1]:
            return False
        return self.helper(s[1:-1])
    
# Time: O(n), Space: O(n)

# Iterative approach:
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        f=""
        for i in s:
            if i.isalnum():
                f+=i 
        j=len(f)-1
        for i in range(len(f)//2):
            if f[i]!=f[j-i]:
                return False
        return True

# Time: O(n), Space: O(n)

# Two pointer approach:

def isPalindrome(s):
    i, j = 0, len(s) - 1

    while i <= j:
        if not s[i].isalnum():
            i += 1
            continue

        if not s[j].isalnum():
            j -= 1
            continue

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True

# Time: O(n), Space: O(1)