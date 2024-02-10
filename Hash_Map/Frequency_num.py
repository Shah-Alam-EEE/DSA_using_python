# Problem: https://www.codingninjas.com/studio/problems/count-frequency-in-a-range_8365446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

def freq_num(n):
    d={}
    for i in n:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
print(freq_num([3,2,5,3,1,1]))

# Time: O(n),Space: O(n)