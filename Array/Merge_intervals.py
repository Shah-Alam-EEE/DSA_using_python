# Problem: https://leetcode.com/problems/merge-intervals/description/

# Approach 1: Time:O(), Space:O()

def merge( intervals):
    result=[]
    result.append(intervals[0])
    for i in range(1,len(intervals)):
        [pf,pl]=result[-1]
        cf=intervals[i][0]
        cl=intervals[i][1]
        if cf<=pl:
            mf=pf
            ml=max(pl,cl)
            result[-1]=[mf,ml]
        else:
            result.append(intervals[i])
    return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))