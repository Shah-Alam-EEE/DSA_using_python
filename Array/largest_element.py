# Problem: https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

def largestElement(arr: [], n: int) -> int:
    max_value=float('-inf')
    # Write your code from here.
    for i in range(n):
        if arr[i]>max_value:
            max_value=arr[i]
    return max_value

# Time: O(n), Space: O(1)