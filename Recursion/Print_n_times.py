# Problem: https://www.codingninjas.com/studio/problems/-print-n-times_8380707?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

def printNtimes(n: int) -> List[str]:
    if n==0:
        return
    print("Coding Ninjas",end=" ")
    printNtimes(n-1)
printNtimes(5)