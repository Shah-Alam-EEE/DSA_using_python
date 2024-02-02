# Problem: https://leetcode.com/problems/fibonacci-number/description/

# Recursive approach:

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)

# Time: O(2^n), Space: O(n)

# Iterative approach:
def fib(n):
    x=0
    y=1
    for i in range(2,n+1):
       z=x+y
       x=y
       y=z  
    return y  
print(fib(5))

# Time: O(n), Space:O(1)    

# Iterative approach with array:

def fib(n):
    a=[0,1]
    for i in range(2,n+1):
       a.append(a[i-1]+a[i-2])
    return a[n] 


# Time: O(n), Space: O(n)

# Fibonacchi solution by formula:

# fn= (1+ 5^.5)^n-(1-5^.5)^n/2^n*5^.5

from math import sqrt 
def nthFib(n):
	res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
	print(int(res),'is',str(n)+'th fibonacci number')
nthFib(12)

# Time: O(1), Space: O(1)