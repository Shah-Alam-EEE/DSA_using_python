# problem: https://www.codingninjas.com/studio/problems/reverse-an-array_8365444?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

r=[]
def reverseArray(n: int, nums):
    # Write your code here
    if n==0:
        return r
    r.append(nums[n-1])
    return reverseArray(n-1,nums)
nums=[3,2,4,1,7]
print(reverseArray(len(nums),nums))

# Time: O(n), Space: O(n)