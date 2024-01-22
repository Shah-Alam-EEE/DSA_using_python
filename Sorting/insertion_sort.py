def inser_sort(n):
    length=len(n)
    
    for i in range(1,length):
        icnt=i
        for j in range(i-1,-1,-1):
            if n[icnt]<n[j]:
                n[icnt],n[j]=n[j],n[icnt]
                icnt=icnt-1
            else:
                break    
arr = [1, 1, 13, 5, 6]
inser_sort(arr)            
print("Sorted array:", arr)



#it's an in place sorting algorithm
#it's stable
#space complexity is O(1)
#best case time complexity is O(n)
#worst case time complexity is O(n^2)
#average case time complexity is O(n^2)
