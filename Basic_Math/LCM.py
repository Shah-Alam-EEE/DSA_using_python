# Approach: 1

def lcm(x,y):
    l=1
    for i in range(2,x+1 and y+1):
        if x%i==0 and y%i==0:
            x/=i
            y/=i
            l*=i
    l=l*x*y
    return int(l)
print(lcm(10,5))

# Space: O(1) Time: O(x) here x is the smaller number

# Approach: 2


def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
    
def lcm(a,b):
    return ((a*b)//gcd(a,b))
    
print(lcm(1,5))
    
# Time: O(log(n)) Space: O(log(n)) , where n is the smaller number   

