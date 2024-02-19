# Problem: https://leetcode.com/problems/move-zeroes/description/

# Optimal approach:
class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        k=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[i],arr[k]=arr[k],arr[i]
                k+=1
        return arr
    
# time: O(n) , Space: O(1)
    
# Naive approach:
    
class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        if len(arr)==1:
            return arr
        for i in range(len(arr)-1):
            for j in range(len(arr)-1-i):
                if arr[j]==0:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    
# Time: O(n^2), Space: O(1)