# Problem: https://leetcode.com/problems/sort-colors/


# Naive approach: Time: O(n^2), Space: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums    



# Better approach: Time: O(n), Space: O(1)
    
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red=0
        white=0 
        blue=0
        for i in nums:
            if i==0:
                red+=1
            elif i==1:
                white+=1
            else:
                blue+=1
        for i in range(red):
            nums[i]=0
        for j in range(red,red+white):
            nums[j]=1
        for k in range(red+white,len(nums)):
            nums[k]=2
        return nums

# Optimal approach(Dutch National flag algorithm): Time: O(n), Space: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low=mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums