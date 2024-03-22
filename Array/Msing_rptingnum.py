# Problem: https://www.codingninjas.com/studio/problems/missing-and-repeating-numbers_6828164?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Approach 1: Time: O(3n), Space:O(n)

def findMissingRepeatingNumbers(a):
    N =len(a)
    map={}
    p=q=0
    for i in range(1,N+1):
        map[i]=0
    for j in a:
        map[j]+=1
    for key,value in map.items():
        if value==2:
            p=key
        if value==0:
            q=key
    return [p,q]
# Approach 2: Time: O(2n), Space:O(n)

def findMissingRepeatingNumbers(a):
    N =len(a)
    map={}
    p=q=0
    for j in a:
        if j not in map:
            map[j]=1
        else:
            map[j]+=1
    for i in range(1,N+1):
        if i in map:
         if map[i]==2:
            p=i
        else:
            q=i
    return [p,q]

# Approach 3: Time: O(n), Space:O(1)

def findMissingRepeatingNumbers(a):
    N=len(a)
    total_sum = N * (N + 1) // 2
    total_square_sum = N * (N + 1) * (2 * N + 1) // 6
    
    array_sum = sum(a)
    array_square_sum = sum(x * x for x in a)
    
    diff = array_sum - total_sum
    diff_square = array_square_sum - total_square_sum
    
    # P - Q = diff
    # P^2 - Q^2 = diff_square
    
    # Using the identity (P + Q) * (P - Q) = P^2 - Q^2
    # So, P + Q = diff_square / diff
    # Solving the above two equations will give us P and Q
    
    P_plus_Q = diff_square // diff
    P = (P_plus_Q + diff) // 2
    Q = P_plus_Q - P
    
    return [P, Q]



