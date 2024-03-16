# Problem: https://leetcode.com/problems/maximum-subarray/description/

# Optimal approach: Time: O(n), Space: O(1) Kadane's alogrithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lsum = float('-inf')
        sum = 0
        for num in nums:
            sum = max(num, sum+num)
            lsum = max(lsum, sum)
        return lsum
    
# Better approach: Time: O(n), Space: O(1)

def maxSubArray(nums):
    lsum = float('-inf')
    sum = 0
    start = -1
    end = -1
    for i in range(len(nums)):
        sum += nums[i]
        if(nums[i]>sum):
            start=i
            sum = nums[i]
        if(sum>lsum):
            end = i
            lsum = sum
    return [start,end,lsum]


# Divide and conquer approach: Time: O(nlog(n)), Space: O(log(n))

def totalSum(nums, l, m, r):
    leftSum = float('-inf')
    sum = 0
    for i in range(m, l - 1, -1):
        sum += nums[i]
        leftSum = max(leftSum, sum)
    
    rightSum = float('-inf')
    sum = 0
    for i in range(m + 1, r + 1):
        sum+= nums[i]
        rightSum = max(rightSum, sum)
    
    return leftSum + rightSum

def maxSum(nums, left, right):
    if left == right:
        return nums[right]
    
    mid = left + (right - left) // 2
    leftSide = maxSum(nums, left, mid)
    rightSide = maxSum(nums, mid + 1, right)
    subArray = totalSum(nums, left, mid, right)
    
    return max(leftSide, rightSide, subArray)

