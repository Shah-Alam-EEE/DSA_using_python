# Problem: https://www.codingninjas.com/studio/problems/sorted-array_6613259?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION


# Naive approach:

def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    c=[]
    for i in a:
        if i not in c:
            c.append(i)
    for i in b:
        if i not in c:
            c.append(i)
    c.sort()
    return c

# Time : O(n^2), Space: O(n)

#optimal approach:

def unionArray(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            if len(res) == 0 or res[-1] != a[i]:
                res.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if len(res) == 0 or res[-1] != b[j]:
                res.append(b[j])
            j += 1
        else:  # a[i] == b[j]
            if len(res) == 0 or res[-1] != a[i]:
                res.append(a[i])
            i += 1
            j += 1
    
    # Add remaining elements from array 'a'
    while i < len(a):
        if len(res) == 0 or res[-1] != a[i]:
            res.append(a[i])
        i += 1
    
    # Add remaining elements from array 'b'
    while j < len(b):
        if len(res) == 0 or res[-1] != b[j]:
            res.append(b[j])
        j += 1
    
    return res


# Time: O(n), Space: O(n)