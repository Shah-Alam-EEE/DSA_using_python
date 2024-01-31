# Problem: https://www.codingninjas.com/studio/problems/n-to-1-without-loop_8357243?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

n=[]
def printNos(x: int) -> List[int]:
    if x==0:
        return n 
    n.append(x)
    return printNos(x-1)