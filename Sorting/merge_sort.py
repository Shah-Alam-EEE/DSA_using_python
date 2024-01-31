def merge(left,right):
    result=[]
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1
    result+=left[i:]
    result+=right[j:]  
    return result      
def merge__sort(n):
    if len(n)<=1:
        return n
    mid=int(len(n)/2)
    left=merge__sort(n[:mid])
    right=merge__sort(n[mid:])
    return merge(left,right)

lst=[1,7,3,58,5,6,1]
x=merge__sort(lst)
print(x)


#space complexity is O(n)
#best time complexity O(n)
#average and worst time complexity is O(n*log(n))
#stable
#not in place


# Python program in-place Merge Sort
# Approach: 2

def merge(arr, start,mid,end):
    start2=mid+1
    if arr[mid]<=arr[start2]:
        return
    while start<=mid and start2<=end:
        if arr[start]<arr[start2]:
            start+=1
        else:
            temp=arr[start2]
            index=start2
            
            while index != start:
                arr[index]=arr[index-1]
                index-=1
                
            arr[start]=temp
            start+=1
            mid+=1
            start2+=1
    
def merge_sort(arr,l,r):
    if l<r:
        mid=l+(r-l)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge(arr,l,mid,r)
        
a=[2,3,1,6,5,7,4]
merge_sort(a,0,len(a)-1)
print(a)
        
# Space: O(1) . Time: O(n^2log(n))   
    
