# Problem: https://www.codingninjas.com/studio/problems/superior-elements_6783446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM


# Naive approach: Time: O(n^2), Space: O(n)

def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    result=[]
    result.append(a[-1])
    for i in range(len(a)-1):
        flag=1
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                flag=0
                break
        if flag==1 and a[i] not in result:
            result.append(a[i])
   
    result.sort()
                
    return result

# Optimal approach: Time: O(n), Space: O(n)


def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    result=[]
    result.append(a[-1])
    superiore=a[-1]
    for i in range(len(a)-2,-1,-1):
        if a[i]> superiore:
            result.append(a[i])
            superiore=a[i]
    return result



