# Problem: https://leetcode.com/problems/permutations-ii/description/

# Recursive approach: Time: O(n*n!), Space: O(n*n!)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permutation(tii):
            if tii==len(nums):
                result.append(nums[:])
                return
            test_set=set()
            for i in range(tii,len(nums)):
                if nums[i] in test_set:
                    continue
                test_set.add(nums[i])
                nums[i],nums[tii]=nums[tii],nums[i]
                permutation(tii+1)
                nums[tii],nums[i]=nums[i],nums[tii]
        result=[]
        permutation(0)
        return result