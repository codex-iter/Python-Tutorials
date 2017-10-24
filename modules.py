# Diving into modules

'''
Modules can be imported in the following ways:

1. import module_name
    This will import the mosule but if when you will use the function from the module,
    you have to specify the module_name with the function. e.g: user_module.function1()

2. import module_name as short_name
    This is exactly similar to the previous method. The only difference is that instead
    of writing the module_name again you can use the short_name you gave.
    e.g: import user_module as um
         um.function1() 

3.  from module_name import function
    This will import only the specific function from the given module. You cannot use other
    functions from that module. 
    e.g: from user_module import function1
         function1()

4. from module_name import *
    This will import all the functions from the module. Additionally you will not need to 
    write the module_name anymore for accessing the functons.
    e.g: from user_module import *
         function1()

'''

#import user_module
#import user_module as um
#from user_module import functon1
from user_module import *
import random


functon1()
functon2()


x = random.randrange(1,100) #it will generate a random number within 1 to 100. Function imported from random module.
print(x)

# dir(module_name)
# help(mosule_name)

# The following will show the dir where python search for modules
import sys
print(sys.path)

#sys.path.append("your_module_path")        this will add your own module path to predefines paths od python modules