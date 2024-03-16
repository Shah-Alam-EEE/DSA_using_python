# Problem: https://leetcode.com/problems/majority-element-ii/description/

# Naive approach: Time : O(n^2), Space: O(num of n/3 element max(2) min 1)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        for i in range(n):
            count=1
            for j in range(i+1,n):
                if nums[j]==nums[i]:
                    count+=1
            if count>n/3 and nums[i] not in result:
                result.append(nums[i])
        return result
    
# Better approach: Time : O(n), Space: O(n)
    
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        map={}
        for i in range(n):
            if nums[i] not in map:
                map[nums[i]]=1
            else:
                map[nums[i]]=map[nums[i]]+1
        for key,value in map.items():
            if value>n/3:
                result.append(key)
        return result
    
# Optimal approach:  Time : O(n), Space: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        candidate1,candidate2,count1,count2=None,None,0,0
        for i in range(len(nums)):
            if candidate1==nums[i]:
                count1+=1
            elif candidate2==nums[i]:
                count2+=1
            elif count1==0:
                candidate1=nums[i]
                count1+=1
            elif count2==0:
                candidate2=nums[i]
                count2+=1
            else:
                count2-=1
                count1-=1
        count1,count2=0,0
        for num in nums:
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1
        result=[]
        if count1> n//3:
            result.append(candidate1)
        if count2>n//3:
            result.append(candidate2)
        return result

