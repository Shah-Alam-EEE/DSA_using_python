# problem: https://leetcode.com/problems/single-number/

# Naive approach 1:

def once(nums):
    if(len(nums)==1): return nums[0]
    for i in range(0,len(nums)):
        notFound = True
        for j in range(0,len(nums)):
            if(i!=j):
                if(nums[i]==nums[j]):
                    notFound = False
                    break
        if(notFound): 
            return nums[i]
    if(not notFound): 
        return None
nums = [2,2,1,1]      
print(once(nums))


# Naive approach 2:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
                return nums[i]
        

# Both have O(n^2) time complexity