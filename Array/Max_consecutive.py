# Problem: https://leetcode.com/problems/max-consecutive-ones/


# Naive approach:


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        for i in range(len(nums)):
            if(nums[i]==0): continue
            currCount = 0
            for j in range(i,len(nums)):
                if(nums[j]==1):
                    currCount += 1
                    maxCount = max(maxCount,currCount)
                else: break    
        return maxCount
    
# Time: O(n^2), Space: O(1)
    
# Optimal approach:
    
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive =0
        present_consecutive =0
        for i in nums:
            if i==1:
                present_consecutive +=1
                max_consecutive=max(max_consecutive, present_consecutive)
            else:
                present_consecutive=0
        return max_consecutive


# Time: O(n), space: O(1)