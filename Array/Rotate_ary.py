# Problem: https://leetcode.com/problems/rotate-array/description/

# Naive approach:

class Solution:
    def reverse(self,nums,s,e):
        while s<e:
            nums[s],nums[e]=nums[e],nums[s]
            s+=1
            e-=1
    def reverse_fun(self,nums,s,e):# Another way to reverse an array with start and end index
        j=0
        for i in range(s,(s+(e-s)//2)+1):
            x=e-j
            nums[i],nums[x]=nums[x],nums[i]
            j+=1
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
        return nums

# Time: O(n), Space: O(1)

# Optimal approach:
    
def test(nums,a):
    k=[]
    for i in range(a+1):
        k=nums[len(nums)-i:]+nums[:len(nums)-i]
    return k

# Time: O(n),Space O(n)