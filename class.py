'''
Defining a Class in Python
Like function definitions begin
with the def keyword in Python,
class definitions begin with a 
class keyword.

The first string inside the class is called
docstring and has a brief description of the class.
Although not mandatory, this is highly recommended.

Here is a simple class definition.'''

class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass
'''A class creates a new local namespace where all its attributes are defined.
Attributes may be data or functions.

There are also special attributes in it that begins with 
double underscores __. For example, __doc__ gives us the
docstring of that class.

As soon as we define a class, 
a new class object is created with the same name. 
This class object allows us to access the different
attributes as well as to instantiate new objects 
of that class.'''

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# Output: 10
print(Person.age)

# Output: <function Person.greet>
print(Person.greet)

# Output: "This is a person class"
print(Person.__doc__)







class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# create a new object of Person class
harry = Person()

# Output: <function Person.greet>
print(Person.greet)

# Output: <bound method Person.greet of <__main__.Person object>>
print(harry.greet)

# Calling object's greet() method
# Output: Hello
harry.greet()