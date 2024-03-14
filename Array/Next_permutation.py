# Problem: https://leetcode.com/problems/next-permutation/description/

# Optimal approach: Time: O(n), Space: O(n)

def next_permutation(nums):
    n = len(nums)
    break_point = -1

    # Step 1: Find the break point:
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            break_point = i
            break

    # If break point does not exist:
    if break_point == -1:
        # Reverse the whole array
        nums.reverse()
        return nums

    # Step 2: Find the next greater element (the elements are in descending
    # order in the right side of the breakpoint) and swap it with
    # nums[break_point]:
    for i in range(n - 1, break_point, -1):
        if nums[i] > nums[break_point]:
            nums[i], nums[break_point] = nums[break_point], nums[i]
            break

    # Step 3: Rearrange the elements in ascending order. As the elements are in descending order, just reverse them:
    nums[break_point + 1:] = nums[break_point + 1:][::-1]

    return nums

# Example usage:
nums = [1, 2, 3]
print(next_permutation(nums))  # Output: [1, 3, 2]


# Approach 2: it is applicable only if the array have unique element

def nextPermutation( nums):
    def permutation(arr, hash_set, temp_arr):
        if len(temp_arr) == len(arr):
            result.append(temp_arr[:])
            return
        for i in arr:
            if i not in hash_set:
                hash_set.add(i)
                temp_arr.append(i)
                permutation(arr, hash_set, temp_arr)
                hash_set.remove(i)
                temp_arr.pop()

    sorted_arr = sorted(nums)
    hash_set = set()
    temp_arr = []
    result = []
    permutation(sorted_arr, hash_set, temp_arr)
    # print(nums)
    # return result
    for res in result:
        if nums == res:
            idx = result.index(nums)
            if idx == len(result) - 1:
                nums=result[0]
                return nums
            else:
                nums=result[idx + 1]
                return nums
print(nextPermutation([2,3,1]))
