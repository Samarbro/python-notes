''' 
Recursion is a function which calls itself.

It is used to directly use a mathematical formula as function.


EXAMPLE


factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 * 1
factorial(3) = 3 * 2 * 1
factorial(4) = 4 * 3 * 2 * 1
factorial(5) = 5 * 4 * 3 * 2 * 1





factorial(n) = n * factorial(n-1)




'''


# This function can be defind as follows:

def factorial(n):
    if n == 0 or n == 1:  # base condition which doesn't call the function any further
        return 1
    else:
        return n*factorial(n-1) # function calling itself
    
    
n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")    