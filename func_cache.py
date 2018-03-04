'''
Cache function values
''' 

from functools import lru_cache

@lru_cache(maxsize=22)
def fib(n):
    if n < 2:
        return n 
    return fib(n-1) + fib(n-2)


fib_no = [ fib(num) for num in range(20) ]

print(fib_no)