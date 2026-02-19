'''  FUNCTION WITH ARGUMENTS

A function can accept some value it can work with. We can put
these values in the parentheses.

A function can also return value as shown below:


'''


def greet(name):
    gr = "hello " + name
    return gr


a = greet("harry")
# a will now contain "hello harry"
print(a)


# this is for argument

def mogger(name):
    print("Mogger number 1 ," + name )
    
  
mogger("samar")
mogger("harry")

# this for ending argument

def mogger(name, ending):
    print("Mogger number 1 ," + name + ending)
    
  
mogger("samar", " from india")
mogger("harry", " from england")



# this for return value


def greet(name):
    print("hello " + name)
    return "done"
    
a = greet("harry ")
print(a)    
    