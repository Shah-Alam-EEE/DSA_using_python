# Problem: https://leetcode.com/problems/4sum/description/

# Naive approach: Time:O(n^4), Space: O(n)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    temp_arr=[]
                    for l in range(k+1,len(nums)):
                        if nums[i]+nums[j]+nums[k]+nums[l]==target:
                            temp_arr.append(nums[i])
                            temp_arr.append(nums[j])
                            temp_arr.append(nums[k])
                            temp_arr.append(nums[l])
                            temp_arr.sort()
                            if temp_arr not in result:
                                result.append(temp_arr)
                            break
        return result
    
# optimal approach: Time:O(n^3), Space: O(n)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if i >0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                left,right=j+1,len(nums)-1
                while left<right:
                    if nums[i]+nums[j]+nums[left]+nums[right]==target:
                        if [nums[i],nums[j],nums[left],nums[right]] not in result:
                            result.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[left-1]:
                            right-=1    
                        left+=1
                        right-=1
                    elif nums[i]+nums[j]+nums[left]+nums[right]<target:
                        left+=1
                    else:
                        right-=1
        return result