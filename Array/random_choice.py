# Approach 1

import random
x=[3,2,4,1,5]
print(random.randint(10,20))


# Approach 2

import time

def custom_random(start, end):
    # Use the current time in milliseconds as a seed
    seed = int(time.time() * 1000)
    
    # Linear Congruential Generator (LCG) algorithm to generate pseudo-random numbers
    # This algorithm generates numbers between 0 and 1, so we scale it to the desired range
    a = 1664525
    c = 1013904223
    m = 2**32
    
    seed = (a * seed + c) % m
    
    # Scale the number to the given range and return
    return start + (seed % (end - start + 1))

# Example usage:
start = 1
end = 10
random_number = custom_random(start, end)
print("Random number between", start, "and", end, ":", random_number)
