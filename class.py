# Diving Into Class and Objects
'''
Class:
    A user-defined prototype for an object that defines a set of attributes that 
    characterize any object of the class.

Object:
    A unique instance of a data structure that's defined by its class.
'''

#The following shows how to define a class. Here Employee is the class name.
class Employee:
    'The Documentation of the class that describes the functionality of the class.'
    

    # it is the constructor of the class. Whwnever an object is created the constructor will execute aotumatically.
    def __init__(self, x):
        self.salary = 50000
        self.age = x

    # These are some basic functions. These will not execute unless you call it.
    def details(self,x,n):
        self.name = x
        self.num = n

    def increase_salary(self):
        if self.age > 25:
            self.salary  = self.salary + 50000
    
    def get_details(self):
        print(self.name,"\n",self.age,"\n",self.num,"\n",self.salary)


# Creating an object
obj1 = Employee(30)     # This will create an object obj1
obj2 = Employee(25)     # This will create an object obj2

obj1.details("Sam",88644)    # this will call method details with passing name as "sam" and number as "88644"
obj2.increase_salary()         # this will call the function increase_salary
obj1.increase_salary()
obj2.details("Joe",99854)     # this will call method details with passing name as "Joe" and number as "99854"

obj1.get_details()      # this will print the details of the objects
obj2.get_details()

print(Employee.__doc__)     # this will print the class documentation.