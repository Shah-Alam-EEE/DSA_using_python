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

