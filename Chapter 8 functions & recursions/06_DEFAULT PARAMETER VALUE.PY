"""  DEFAULT PARAMETER VALUE 

We can have a value as default as default argument in a function.

If we specify name = "stranger" in the line containing def, 
this value is used when no argument is passed.


"""

def greet(name = "stranger"):
    # function body
    print(f"Hello {name}")
greet("harry") # name will be "harry" in function body (passed)
    