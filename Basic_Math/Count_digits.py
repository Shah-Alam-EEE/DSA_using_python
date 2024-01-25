def countDigits(n: int) -> int:
    if type(n)!='int':
       return 0
    count=0
    while(n>0):
        digit=n%10
        if type(n/digit)=='int':
            count=count+1
        n=n//10
    return count    
a=countDigits(35)
print(a)