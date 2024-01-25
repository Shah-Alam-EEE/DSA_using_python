# Approach 1:
# Time: O(nlogn)
# Space: O(n)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    
    pivot = arr[0]
    left, right, equal = [], [], []

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            right.append(element)

    return quick_sort(left) + equal + quick_sort(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)

# Approach 2
# Space: O(log(n)), Time: O(nlogn)


def partition(nums,low,high):
    
    i=low-1
    pivot=high
    for j in range(low,high):
        if nums[j]<nums[pivot]:
            i=i+1
            nums[i],nums[j]=nums[j],nums[i]
        
    nums[pivot],nums[i+1]=nums[i+1],nums[pivot]
    return i+1    

def quick_sort(nums,low,high):
    if low<high:
       pivot= partition(nums,low,high)
       quick_sort(nums,low,pivot-1)
       quick_sort(nums,pivot+1,high)
   
   
r=[3,2,1,4,6,5]
quick_sort(r,0,len(r)-1)
print(r)

# Approach 3
def quickSort(arr, low, high):
    pivot = arr[(low + high) // 2]
    left, right = low, high

    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    if low < right:
        quickSort(arr, low, right)
    if left < high:
        quickSort(arr, left, high)
my_list = [7, 29, 15, 36, 24, 20, 18, 30, 12]
quickSort(my_list, 0, len(my_list) - 1)
print(my_list)
        
"""
Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element 
from the array and partitioning the other elements into two sub-arrays, according to 
whether they are less than or greater than the pivot."""
# The main steps of the quicksort algorithm are as follows:

# Choose a pivot element from the array.
# Partition the array into two subarrays: elements less than the pivot and elements greater than the pivot.
# Recursively sort the two subarrays.
# Combine the sorted subarrays to produce the final sorted array.
"""""
The code you provided is an implementation of the quicksort algorithm. This implementation has a time complexity of O(n^2) in
the worst case and an average-case time complexity of O(n log n). Let's break down the time complexity of this code:

The base case checks if the length of the array arr is less than or equal to 1, and if so, it returns the array itself.
This part takes O(1) time.

The pivot element is selected by taking the element at the middle index, which takes O(1) time.

The code then iterates through the array and categorizes each element into one of three lists: left, equal, or right. 
This loop iterates over all elements in the input array, so it takes O(n) time.

The code recursively calls quick_sort on the left and right subarrays and then concatenates the 
results with the equal array using the + operator. The time complexity of this part depends on the depth of the 
recursion and the size of the input arrays. In the worst case, if the pivot selection consistently results in highly unbalanced 
partitions, it can lead to a time complexity of O(n^2). However, on average, quicksort has a time complexity of O(n log n).

So, the overall time complexity of this code is O(n^2) in the worst case and O(n log n) on average, which is the expected 
performance of the quicksort algorithm. Keep in mind that the choice of the pivot element can influence the actual performance, and
certain pivot selection strategies can improve the worst-case behavior."""
#it is not stable
#it is not in place
#best and average time complexity is O(nlogn)
#worst is O(n^2)
