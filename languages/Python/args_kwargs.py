'''
Understanding *args and *kwargs

 - *args and **kwargs allow you to pass a variable number of arguments to a function
 - *args is used to send a non-keyworded variable length argument list to the function

''' 


def test_args(*args):
    '''
    >>> test_args(1,2,3)
    '''
    for variable in args:
        print(variable)

test_args(1,2,3)

def test_kwargs(**kwargs):
    '''
    test_kwargs(a=1, b=2)
    ''' 
    for key, value in kwargs.items():
        print(key,value)

    for key in kwargs.keys():
        print(key)
    
    for value in kwargs.values():
        print(value)
        

# Call 
test_kwargs(a=2, b=3)
test_kwargs(a=2)

person_info = dict(name="manoj", age="27")

# Unpack the person_info and pass to the function 
# print(**person_info) won't work
# print(*person_info) work and it will only print key values    
# print() statement return None like console.log() return undefined in javascript. 
test_kwargs(**person_info)


