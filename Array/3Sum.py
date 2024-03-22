# Problem: https://leetcode.com/problems/3sum/description/

# Naive approach: Time:O(n^3), Space: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp_arr=[]
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp_arr.append(nums[i])
                        temp_arr.append(nums[j])
                        temp_arr.append(nums[k])
                        temp_arr.sort()
                        if temp_arr not in result:
                            result.append(temp_arr)
                        break
        return result
            
# Optimal approach: Time:O(n^2), Space: O(n)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result