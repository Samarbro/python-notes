""" 1. write a program to store seven fruits in a list entered by the user.
2. write a program to accept marks of 6 students and display them  in a
sorted manner. 
3. Check that a tuple type cannot be changed in python.
4. write a program to sum a list with 4 numbers. 
5. write a program to count the number of zeros in the following tuple:"""


"""
fruites = []

f1 = input(" enter fruite name: ")
fruites.append(f1)
f2 = input(" enter fruite name: ")
fruites.append(f2)
f3 = input(" enter fruite name: ")
fruites.append(f3)
f4 = input(" enter fruite name: ")
fruites.append(f4)
f5 = input(" enter fruite name: ")
fruites.append(f5)

print(fruites)    # this code is for question number 1 
"""

"""
marks = []

f1 = input(" enter student marks: ")
marks.append(f1)
f2 = input(" enter student marks: ")
marks.append(f2)
f3 = input(" enter student marks: ")
marks.append(f3)
f4 = input(" enter student marks: ")
marks.append(f4)
f5 = input(" enter student marks: ")
marks.append(f5)

print(marks)       #  this code for question 2 
"""



"""  question 3 - we need to check tuple are mutable or immutable ??

a = (35, 66, 99, "samar")                           
a[3] = "winter" 


"""                    #here is code after runing this you will see a error
                                                    #   that means tuple are immutable.
                                                    
                                                    
                                                    
                                                    
                                                    
""" quesiton 4 - write a program to sum a list with 4 numbers. """


l = (23, 44, 44, 56, 35, 374673, 73264736, 45, 1)



print(sum(l))  # this code will sum of numbers from the list





# question 5 - write a program to count the number of zeros in the following tuple:


a = (1, 3, 4, 0, 3, 0, 0, 8, 0, 0)


n = a.count(0)


print(n)
        # after runing this code output will tell you how much zeros in this list.