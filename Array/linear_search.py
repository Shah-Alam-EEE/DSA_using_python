# Peoblem: https://www.codingninjas.com/studio/problems/linear-search_6922070?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION


# Approach 1:

def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1

# Time O(n), Space: O(1)