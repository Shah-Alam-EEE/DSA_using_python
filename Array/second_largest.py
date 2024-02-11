# Problem:https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    max_num=float('-inf')
    max_num1=float('-inf')
    min_num=float('inf')
    min_num1=float('inf')
    for i in a:
        if i<min_num:
            min_num1=min_num
            min_num=i
        elif i<min_num1 and i!=min_num:
            min_num1=i
        if i>max_num:
            max_num1=max_num
            max_num=i
        elif i>max_num1 and i!=max_num:
            max_num1=i
    return [max_num1,min_num1]

# Time: O(n), Space: O(1)