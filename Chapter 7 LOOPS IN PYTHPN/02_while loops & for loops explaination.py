# WHILE LOOPS 

''' 

while (condition):  # The block keeps executing until the condition is
# true body of the loop

  
  
In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed otherwise not!
If the loop is entered, the process of [condition check & execution] is continued until the condition becomes False.
Quick Quiz: Write a program to print 1 to 50 using a while loop.


      EXAMPLE 
'''  

i = 0 
while i < 5: # print "harry"  -5 time!
    print("harry")
    i = i + 1
    
    '''
Note: If the condition never become false, the loop keeps getting executed.


Quick Quiz: Write a program to print the content of a list 
using while loops.    


'''



# FOR LOOPS

'''

A for loops is used to iterate through a sequence like list
, tuple, or string[iterables]

          Syntax:
'''

l = [1, 7, 8]
for item in l:
    print(item) # prints 1,7 and 8