# Problem: https://www.codingninjas.com/studio/problems/longest-subarray-with-zero-sum_6783450?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

# Naive approach: Time:O(n^2), Space: O(1)

def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:
    maxlen=0
    for i in range(len(arr)):
        currlen=0
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            currlen+=1
            if sum==0:
                maxlen=max(currlen,maxlen)
    return maxlen

# Better approach: Time:O(n), Space: O(n)

def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:
    n = len(arr)
    prefix_sum = 0
    max_length = 0
    sum_index_map = {}
    
    for i in range(n):
        prefix_sum += arr[i]
        
        # If prefix_sum is 0, it means the subarray from index 0 to i has a sum of 0
        if prefix_sum == 0:
            max_length = i + 1
        
        # If prefix_sum is already in the map, it means there exists a subarray with sum 0
        elif prefix_sum in sum_index_map:
            max_length = max(max_length, i - sum_index_map[prefix_sum])
        
        # If prefix_sum is not in the map, store it along with its index
        else:
            sum_index_map[prefix_sum] = i
    
    return max_length