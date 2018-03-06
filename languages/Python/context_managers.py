'''
Context managers
Why do we need context managers ?
How context managers works?

Context managers allocate and release resources when you need. 
Basic example of context managers is `with` statement. 
''' 

# Simple example 

with open('hello.txt', 'r') as file_obj:
    data = file_obj.read() 

# The above code is equivalent to 

try:
    file_obj = open('hello.txt', 'r')
    data = file_obj.read() 
finally:
    file_obj.close()

# Implementing context managers. 
# To implement context manager we should have __enter__ and __exit__ method. 
# Let's make our own Filereading context manager. 

class FileParser(object):
    def __init__(self, file, mode):
        self.file = open(file, 'r')
    
    def __enter__(self):
        '''
        This method return the object that can be accessed
        with using `as` keyword
        ''' 
        return self.file 
    
    def __exit__(self, type, value, traceback):
        '''
        The errors are passed to this method
        IF it returned True no exception occours else exception need to handle 
        and return True value
        '''
        self.file.close()

# Now we can use this context manager with `with` statement

with FileParser('context_managers.py', 'r') as obj:
    data = obj.read()
    print(data)

    

'''
Implement context managers as generators,
Instead of using class, use generators
''' 
from contextlib import contextmanager

@contextmanager
def open_socket(sock_obj):
    data = sock_obj.connect() 
    yield data 
    # Closing logic here. 
    sock_obj.close()
