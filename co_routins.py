'''
Simple coroutines examples

Coroutines are similar to generators with a few differences. The main differences are:
generators are data producers
coroutines are data consumers

* non  blocking sockets
* callbacks 
* event loop
* coroutines
''' 

# First let's create a Synchronous GET request using socket and
# Later replace this with async framework. 

import socket
import time 

def get(path):
    sock = socket.socket() # Create default INET TCP socket

    # Connect to socket. 
    sock.connect(('localhost', 8000))
    # Make the socket non blocking
    # sock.setblocking(False)
    request = 'GET {} HTTP/1.0\r\n\r\n'.format(path) 
    sock.send(request.encode()) # Default encoding is utf-8 

    chunks = [] 

    while True:
        chunk = sock.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            body = (b''.join(chunks)).decode()
            print(body)
            return # Exit the loop

# start = time.time()
# get('/')
# print("Total time taken is {}".format(start - time.time()))


# Why async
'''
1. For concurrency
2. To decouple CPU and IO bound task 
3. Decouple from long running tasks. 
4. Fewer processes (less threads)
5. Consise control of context switch 
''' 
