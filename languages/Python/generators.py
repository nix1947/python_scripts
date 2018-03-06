'''
Generators example
Generators are used to list the value without storing all of them at once in memory. 

'''

def not_a_generator():
    '''
    This will save all the computed value in memory 
    ''' 
    even_no = [] 
    for no in range(200):
        if no % 2 == 0:
            even_no.append(no)
    return even_no 


def this_is_a_generator():
    '''
    This won't store result in memory, rather it return 
    the iterator which generate the value in the fly, do don't 
    consume memory
    ''' 
    for no in range(200):
        if no % 2 == 0:
            yield no 


# yield from keyword.

def generator2():
    for i in range(10):
        yield i

def generator3():
    for j in range(10, 20):
        yield j 

def yield_from():
    '''
    yield from keyword is used to return the generators from multiple generator
    yield from example
    http://www.cosc.canterbury.ac.nz/greg.ewing/python/yield-from/yf_current/Examples/binary_tree.py
    http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html
    ''' 
    yield from this_is_a_generator()
    yield from generator2()
    yield from generator3()