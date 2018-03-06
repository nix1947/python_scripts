'''
Python decorators:
take a function as an argument 

In python there are two type of decorators. 

a. Function decoratos
b. Class decorators. 
http://scottlobdell.me/2015/04/decorators-arguments-python/
''' 



import time 

def calculate_time(func):
    def wrapper(*args, **kwargs):
        before = time.time() 
        rv = func(*args, **kwargs)
        after = time.time()
        print("The time to execute this function is ", before - after)

        return rv 
    return wrapper 


def add_on_to_result(func):
    """
    This decorator will make an even no if the 
    no returning from function is odd 
    """ 
    def wrap(*args, **kwargs):
        rv = func(*args, **kwargs)
        print("Keys and values padded in kwargs are")
        for key, value in kwargs:
            print(key, value)
        return rv + 1
    
    return wrap
        

@calculate_time
def sum(num):
    sum = 0
    for n in range(num):
        sum = sum + n 
    print("Sum=", sum)


sum(2)
