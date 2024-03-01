# Problem: https://leetcode.com/problems/majority-element/description/

# Better approach: Time: O(n), Space: O(n)
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        n=len(nums)
        majority_condition=n//2
        for i in range(n):
            if nums[i] not in map:
                map[nums[i]]=0
            map[nums[i]]+=1
            
        for key,value in map.items():
            if value> majority_condition:
                return key

# Optimal approach(Moore's Voting algorithm): Time: O(n), Space(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if count==0:
                element=nums[i]
            if element==nums[i]:
                count+=1
            else:
                count-=1
        return element
    
