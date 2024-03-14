# Approach 1

def calcGCD(n:int, m: int) -> int:
    # Write your code here
    l = []
    r = []
    if n==0:
        return m
    elif m==0:
        return n

    # Populate the arrays with divisors
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)

    for j in range(1, m + 1):
        if m % j == 0:
            r.append(j)

    # Find the greatest common divisor
    for k in range(min(n, m), 0, -1):
        if k in l and k in r:
            return k
print(calcGCD(7,11))

# Time: O(n*(n+m)) Space: O(m+n)

# Approach 2

def GCD(a,b):
    if  a==0:
        return b
    elif b==0:
        return a
    elif a>b:    
        while b>0:
            r=a%b
            a=b
            b=r
        return a
    elif a<b:
        while a>0:
            k=b%a
            b=a
            a=k
        return b     
        
print(GCD(1,5))    

# Time: O(log(n)) where n is the smaller num. Space: O(1)

# Approach 3

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(10,5))
# Time: O(log(n)). Space: O(log(n)) where n is the smaller num. 

