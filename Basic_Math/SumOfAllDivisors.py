# Problem: https://www.codingninjas.com/studio/problems/sum-of-all-divisors_8360720?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

# Approach: 1

def sumOfAllDivisors(n: int) -> int:
    sum=0
    for i in range(1,n+1):
      for j in range(1,i+1):  
        if i%j==0:
            sum=sum+j
    return sum
print(sumOfAllDivisors(10))

# Time: O(n^2). Space: O(1)   
     
# Approach: 2

def sumOfAllDivisors(n: int) -> int:
    sum=0
    for i in range(1,n+1):
      for j in range(1,int(pow(i,0.5))+1):  
        if i%j==0:
            sum=sum+j
            if j != i/j:
                sum=sum+(i/j)
      
    return int(sum)
                       
# Time: O(n*sqrt(n)). Space: O(1)                       