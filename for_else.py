'''
Use of for/else in python 
For loops also have an else clause which most of us are unfamiliar with.
The else clause executes when the loop completes normally. 
This means that the loop did not encounter any break
''' 

for i in range(100):
    if i == 50:
        break
    print("This won't execute the else block as loop encounted else block")
else:
    print("Loops exit normally")