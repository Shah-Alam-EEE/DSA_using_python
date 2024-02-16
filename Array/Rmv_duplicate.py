# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Naive approach:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=[]
        count_unique=0
        for i in nums:
            if i not in k:
                k.append(i)
                count_unique+=1
        nums.clear()
        nums.extend(k)
        return count_unique

# Time: O(n^2), Space: O(n)    

# Optimal approach:
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k
    
# Time: O(n), Space: O(1)