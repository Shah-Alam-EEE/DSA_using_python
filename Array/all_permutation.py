# Problem: https://leetcode.com/problems/permutations/description/

# Approach 1: Time: O(n*log(n)), Space: O(n*log(n))

def Permutation(arr,temp,set,result):
    if len(temp)==len(arr):
        result.append(temp[:])
        return
    for i in arr:
        if i not in set:
            set.add(i)
            temp.append(i)
            Permutation(arr,temp,set,result)
            temp.pop()
            set.remove(i)
    return result

arr=[1,2,3]
temp=[]
set=set()
result=[]
rslt=Permutation(arr,temp,set,result)
print(rslt)


# approach 2: Time:O(n*n!), Space:O(n*n!)

def permute(nums):
    def permutation(idx):
        if idx == len(nums):
            res.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]  # Swap elements at indices idx and i
            permutation(idx + 1)  # Recursively generate permutations for the remaining elements
            nums[i], nums[idx] = nums[idx], nums[i]  # Restore the array to its original state

    res = []
    permutation(0)
    return res