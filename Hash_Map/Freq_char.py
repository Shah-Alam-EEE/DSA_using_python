def Check_freq(x):
    frequency_counter={}
    y=""
    for i in x:
        if (97<=ord(i)<=122):
            y+=i
    for i in y:
        if i in frequency_counter:
            frequency_counter[i]+=1
        else:
            frequency_counter[i]=1
    return frequency_counter
    #return sorted(frequency_counter.items()) #fetching and return
print(Check_freq("we the people of usa"))