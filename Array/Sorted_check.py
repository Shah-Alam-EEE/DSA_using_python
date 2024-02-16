# Problem: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
# Approach 1: Brute force
def check(self, arr: List[int]) -> bool:
        sorted=0
        if len(arr)==1:
            return True
        for i in range(len(arr)):
            new_arr=arr[len(arr)-i:]+arr[0:len(arr)-i]
            for j in range(len(new_arr)-1):
                if new_arr[j]<=new_arr[j+1]:
                    sorted=1
                else:
                    sorted=0
                    break
            if sorted==1:
                return True
        return False 


# Time: O(n^2), Space: O(n)


# Approach 2: Optimal

class Solution:
    def check(self, nums: List[int]) -> bool:
        pivot = self.findRotationPosition(nums)
        if pivot == 0:
            return True
        else:
            if nums[0] < nums[len(nums)-1]:
                return False
            rightIsSorted = self.isSorted(nums, pivot, len(nums))
            return rightIsSorted 

    def isSorted(self, nums, start, end):
        for i in range(start, end-1):
            if nums[i+1] < nums[i]:
                return False
        return True

    def findRotationPosition(self, nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i+1
        return 0
    

# Time:O(n), Space: O(1)