
# Problem: https://leetcode.com/problems/merge-sorted-array/description/

# Naive approach: Time: O(n*log(n)), Space: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m,len(nums1)):
            nums1[i]=nums2[m-i]
        nums1.sort()


# Better approach: Time: O(m+n), Space: O(m+n)
        
def merge(nums1,m,nums2,n):
    result=[]
    i=j=0
    while i<m and j<n:
        if nums1[i]>nums2[j]:
            result.append(nums2[j])
            j+=1
        else:
            result.append(nums1[i])
            i+=1
    result+=nums1[i:m]
    result+=nums2[j:]
    return result
print(merge([1,2,3,0,0,0],3,[2,5,6],3))      