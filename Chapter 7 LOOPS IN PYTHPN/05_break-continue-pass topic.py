#  THE BREAK STATEMENT

# 'break' is used to come out of the loop when 
# encountered. It instructs the program to exit the loop now.

'''
# EXAMPLE

for i in range (0,80):
    print(i)  # this will print 0,1,2, and 3
    if i==3:
        break
    '''
    
    
'''  THE CONTINUES STATENENT  


'CONTINUE' IS USED TO STOP THE CURRENT ITERATION
OF THE LOOP AND CONTINUE WITH THE NEXT ONE.
IT INSTRUCTS THE PROGRAM TO 'SKIP THIS IRERATION'.

'''    
    
    
# EXAMPLE
'''
for i in range (4):
    print("printing")
    if i==2:   # if i is 2, the iteration is skipped
        continue
    print(i)
'''




''' THE PASS STATEMENT

pass is a null statement in python.
it instructs to "do nothing".

'''


# EXAMPLE


l = [1,7,8]
for item in l:
    pass    # without pass, the program will throw an error.

    
    