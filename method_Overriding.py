'''



Method Overriding in Python
In the above example,
notice that __init__() method 
was defined in both classes, 
Triangle as well Polygon. 
When this happens,
the method in the derived class 
overrides that in the base class.
This is to say, __init__() in Triangle
gets preference over the __init__ in
Polygon.



Generally when overriding a base method,
we tend to extend the definition
rather than simply replace it.
The same is being done by calling 
the method in base class from the one 
in derived class
(calling Polygon.__init__() from __init__() in Triangle).




A better option would be to use the
built-in function super(). 
So, super().__init__(3) is equivalent 
to Polygon.__init__(self,3) and
is preferred. 
To learn more about the super() 
function in Python, 
visit Python super() function.



Two built-in functions isinstance() 
and issubclass() are used to check 
inheritances.

The function isinstance()
returns True if the object is
an instance of the class or
other classes derived from it.
Each and every class
in Python inherits 
from the base class object.

>>> isinstance(t,Triangle)
True

>>> isinstance(t,Polygon)
True

>>> isinstance(t,int)
False

>>> isinstance(t,object)
True



Similarly, issubclass() is used to check for class inheritance.

>>> issubclass(Polygon,Triangle)
False

>>> issubclass(Triangle,Polygon)
True

>>> issubclass(bool,int)
True



'''