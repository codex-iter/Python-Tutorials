# Diving into functions

""" 1. A function is defined by the keyword def. The syntax of function is:
            def function_name( parameters ):
                executable statements
                return
    
    2. A function is called by simply writing the function name followed by parenthesis. Syntax:
            function_name (passed_arguments)
"""


# A Basic Function Example

# A simple function catching a string and printing it
def printing(name):
    print("The name is ",name,"\tCodex",name)
printing("ITER")


# A simple add function that takes two variables x and y and returns the summation of x and y
def add(x,y):
    return (x+y)
ans = add(2,3)
print(" 2 + 3 =",ans)


# A function that can catch unknown number of arguments and store it in form of a tuple
def many_args(*args):
    for i in args:
        print(i)
many_args(1,2,"codex",40.76)



# function with default value
def example (name = "codex"):
    print(name)
example("ITER") # here the value of name will be changed to ITER
example()       # here as no value is passed the default value will be the output ,i.e, codex


# function with keyword argument
def example2 ( name, year ):
    print("Name is: ",name)
    print ("Year is: ",year)
example2( year=2017,name="CODEX")   # here the arguments are passed out of order but still it will catch perfectly as keywords are used
