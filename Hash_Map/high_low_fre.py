# Problem: https://www.codingninjas.com/studio/problems/count-frequency-in-a-range_8365446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

def getFrequencies(v): 
    # Write your code here
    fre_counter={}
    for i in v:
        if i in fre_counter:
            fre_counter[i]+=1
        else:
            fre_counter[i]=1
    sorted_counter = sorted(fre_counter.items())
    p= min(sorted_counter, key=lambda item: item[1])
    q = max(sorted_counter, key=lambda item: item[1])
    return q[0],p[0]

# Time:O(n), Space: O(n)
