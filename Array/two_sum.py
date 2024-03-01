# Problem: https://leetcode.com/problems/two-sum/description/

# Naive approach: Time: O(n^2), Space: O(1).

class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_lst=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    indices_lst.append(i)
                    indices_lst.append(j)
                    return indices_lst


# Better approach: Time: O(n), Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        indices_lst=[]
        for i in range(len(nums)):
                map[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in map and map[target-nums[i]]!= i:
                indices_lst.append(i)
                indices_lst.append(map[target-nums[i]])
                return indices_lst


# Optimal approach: Time: O(n), Space: O(1)

# This algorithm is applicable only when the array is a sorted.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]+nums[right]>target:
                right-=1
            elif nums[left]+nums[right]<target:
                left+=1
            else:
                return [left,right]
            
            