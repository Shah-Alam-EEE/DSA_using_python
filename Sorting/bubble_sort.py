def Bubble_sort(k):
    n=len(k)
    is_sorted=1
    for i in range(n-1):
        for j in range(n-1-i):
            if k[j]>k[j+1]:    
                k[j],k[j+1]=k[j+1],k[j]
                is_sorted=0

        if is_sorted==1:
            break

f = [3, 2, 4, 1]
Bubble_sort(f)
print(f)


