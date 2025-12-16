# FUNDAMENTALS
print('Hello World !')
a=10
b=20
print('sum',a+b)

# IDENTIFIERS - class name / module name / variable name

# Reserved words - 35
import keyword
print(keyword.kwlist)

# DATA TYPES - type of data inside a variable
# int, float, complex, bool, bytes, bytearray, memoryview, str, range, list, tuple, set, frozenset, dict, NoneType
print(type(a))
print(id(b))

#Slicing of Strings
s='durga'
print(s[0])
print(s[-1])
print(s[:])  #same as s[::]
print(s[1:3])
print(s[1:])
print(s[:4])
print(s[::-1]) #reverse string
print(s[1:4:2])  #begin:(end-1):step default=1

# TYPE CASTING - convering one type value to another type
'''
int(a) <<-- float, bool, str(integer value), immutable
float(a) <<-- int, bool, str(integer/float value), immutable
complex(a)/complex(a,b) <<-- int, bool, str(integer/float value), immutable
bool() <<-- int, float, complex, str - immutable
str() <<-- int, float, complex, str - immutable
bytes() : values must be btwn (0,2560), immutable
bytearray() : mutable
list()/[] : mutable, ordered, duplicates
tuple/() : immutable, ordered, duplicates
range() : immutable
set() : mutable, not ordered, no duplicates
frozenset({}) : immutable, not ordered, no duplicates
dict()/{} : mutable, not ordered, key-valuepairs (key-no duplicates, value-duplicate)
'''
#Escape charaters - \n, \t, \', \",...

# OPERATIONS
'''
Arithmetic -
    + : add / string concatenation
    - : subtract
    * : multiply / string multiply
    / : divide, always results in float value
    % : modulo, used mainly incase of checking reminders
    // : floor division, results in quotient of the division (if arguments are float value then results in float else int type)
    ** : power / exponent
Relational - >, <, >=, <=, ==, !=
Logical - and, or, not
Bitwise - &, |, ^, ~, <<, >>
Assignment - =, +=, -=, *=, ...
Special operator - 
    Identity operator : is, is not
    Membership operator : in, not in
'''
a='durga'
b='durga'
print(a is b)
print(a is not b)
print('g' in a)
print('s' not in b)

# MATH MODULE
import math
print(math.sqrt(16))
print(math.pi)

# INPUT AND OUTPUT STATEMENTS
#name = input("Enter your name \n")
#number = int(input("Enter your number: ")) 
#a,b = [int(x) for x in input("Enter your number: ").split(',')]  #splitting a comma separated string
print(a,b)

#eval() - takes a string as an argument and evaluates it as a Python expression, returning the result of that expression
#       - recommended to not use in untrusted input from users i.e. eval(input()) should be avoided
number = eval("10+2*3/4")
print(number)

# Command Line Argument - Command line arguments in Python are values passed to a script when it is executed from the terminal or command prompt
from sys import argv
print('The num of Command Line Arguments: ',len(argv))
print('The list of Command Line Arguments: ',argv)

#output statements
print()        #without any argument in () prints a new line
print('hi')
a,b = 10, 30
print(a, b, sep=':')
print('hello', end=' ')   #if we want output in same line
print('world')
print('first num ', a, 'second num ', b)
print(f'The number is {a}')
print('a value is %i and b value is %d' %(a, b))            #formatted string = %i, %d - int : %f - float : %s - string
print("Durga's number is {0}, Software's number is {1}".format(a,b))    #replacement operater{}

# FLOW CONTROL
'''
Conditional statements - if, if-else, if-elif, if-elif-else

Iterative statements 
    - for : execute some action for every element of a sequence
    - while : execute some action iteratively until some condition is false

Transfer statements 
    - break : break execution within that loop
    - continue : skip current iteration and continue next 
    - pass
'''
for i in range(10):
    if i%2==0:
        continue
    print(i)        #print only odd value

#del keyword
s='durga'
del s
#print(s)  del keyword deletes the variable hence error
s=None
print(s)

# STRING DATA TYPE

s = ' Learning Python is very easy '
print(s[:])           #slicing
print(s + '.')        #Arithmetic operator: +, *
print(s*2)
print(s==1)           #Relational operator: for comparison
print(len(s))
print(s.strip())      # remove space from both ends, rstrip/lstrip
print(s.find('Python'))   #finding 1st occurance of a word or letter in a string    #find(string,begin,end)
print(s.index('r'))         #find/index can be used same output but if not found 'VaueError'
print(s.rfind('r'))    #finding 1st occurance from backward direction (ve'r'y)
print(s.count('Python'))    #count(string,begin,end)
print(s.replace('very easy','easy'))    #replace(oldstring,newstring)

# EXCEPTION HANDLING - handle runtime errors



# LOGGING - that stores complete data flow & exceptions info in a file

import logging
logging.basicConfig(filename='log.txt',level=logging.CRITICAL)
logging.critical('this is a critical message')
msg='cannot divie by zero'
logging.exception(msg)

# DEBUGGING - identifying & fixing bugs. Used to alert programmer

def squareIt(x):
    return x**x             #x*x is correct
assert squareIt(3)==9,"The square of 3 should be 9"     #assert condition,message

# OBJECT ORIENTED PROGRAMMING SYSTEM

'''
Class [like the blue print to create something/an object]
*******
self variable --> default variable pointing to the currect object. Access instance variable/method
Constructor --> __init__; will be automatically executed once at the time of object creation, initialize instance variable
Variables 
Method --> a funct. inside a class is called as method. We write the business logic in it.
Object --> physical existence of class, to create object we use reference variable
Reference Variable [like TV remote] --> variable used to refer object; eg: c=ClassName()
'''

class Student:
    '''This is a student class.'''
    def __init__(self,x,y,z):
        self.name = x
        self.rollno = y
        self.marks = z
    def display(self):
        print(f"{self.name} having {self.rollno} has scored {self.marks} marks.")
    def method1(self):
        del self.rollno

s=Student('Durga',100,50)
print(s.__doc__)      #documentation string of the class
print(s.__dict__)   #dictionary/to know instance variables
s.display()
s.method1()
print(s.__dict__) 

s1=Student('Suraj',102,49)
print(s1.__dict__)
s1.marks = 46
s1.display()

'''
Variables :
    - Instance variable: value of variable vary object to object. For each object a separate copy will be created
    - Static variable: value of variable do not vary object to object. For total class only 1 copy of static variable created
    - Local variable: variable inside a method in the class. Temprorary. Created at the time of method execution & destroyes once method completes
'''

class Test:
    a = 10                              #static variable
    def __init__(self,default_variable=999):
        self.b = 20                      #instance variable
        self.p = default_variable
    def method(self):
        c = 30                      #local variable
        print(c)

t1=Test()
print(t1.__dict__)
print(t1.a)
t2=Test()
t2.method()

'''
Methods:
    - Instance method: that uses atleast one instance variable inside the method of a class
    - Class method: that uses only class/static variables inside the method of a class
    - Static method: that uses neither instance nor static variable inside the method

We can get and set values of instance variable outside constructor using Getters and Setters Methods
Setters and getters in Python (both explicit and @property versions) are instance methods.

For every class, python virtual machine (PVM) will create internally an object called class level object.
Represented as 'cls'.
It holds class level data i.e. static variable.
Only one just object will be created to hold all the static variable of that class.
'''

class Test:
    a = 10
    def __init__(self):
        self.b = 20    
    @classmethod          #class method, instead of self we use cls
    def method1(cls):
        del Test.a      
        Test.x = 10
        cls.y = 10
    def method2(self):          #instance method, self is the argument
        return self.b*2
    def display(self):          #instance method
        print(f"instance variable b = {self.b}")
    @staticmethod          #static method, no need to use self/cls
    def add(x,y):
        return x+y
    
t3 = Test()
t3.method1()
print(Test.y) 
print(Test().method2())
print(Test().add(2,3))

class Employee:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    
e=Employee()
e.setName('Durga')
print(e.getName())

'''Inner class
Without existing of 1 object if there's no chance of existing another typpe of object then we go for ineer classes.
To acess method inside inner class - Outer().Inner().m1()
'''

# Reference counting & Garbage collection
'''
Q). How Python manages memory?

ans: Python combines reference counting, garbage collection, and internal memory management to handle memory efficiently and safely.
Reference counting - Tracking how many refernces point to an object
Garbage Collection - The reference counting alone cannot handle circular references. 
                     So, python has a cyclic garbage collector to handle it.
                     Garbage collector destroys useless objects.
Memory Allocation - While creating object in Python (eg: list, dict, or custom object), Python allocates memory for it in the heap
--
Destructor -Just before destroying an object, Garbage Collector always calls destructor to perform clean up activities (like closing an opened file).
The destructor method is called __del__(self) 
'''
import sys
my_list = [1,2,3]
print(sys.getrefcount(my_list))

import gc
print(gc.isenabled())
gc.enable()

class Test:
    def __init__(self):
        pass
    def __del__(self):
        print('Performing clean up activities')

'''
Passing members of one class to another class - 

1). Composition - by using class name/object we can access members of one class inside another class
                - extends the function so as to just use existing function

2). Inheritance - one class inherts/gets variables, methods & constructors available from another class
                - extends the function so as to extend the existing functionality
--
Aggregation(weak assosiation) v/s Composition(strong assosiation)
eg:    dept,prof                       clg,dept
'''

#Composition
class Engine:
    a=10
    def __init__(self):
        self.b = 20
    def m1(self):
        print("Engine functionality")
class Car:
    def __init__(self):
        self.engine = Engine()         #accessing using class name
    def m2(self):
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
c = Car()
c.m2()

class Car:
    def __init__(self,name,engine):
        self.name = name
        self.engine = engine
    def display(self):
        print(f'Name: {self.name}, Engine: {self.engine}')
e=Engine()
c1 = Car('Durga',e.b)     #acessing using object name
c1.display()

#Inheritance
class Parent:
    a = 10
    def __init__(self):
        self.b = 20
    def m1(self):
        print('Parent class')
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.d = 30
    def m2(self):
        print('Child class')
c = Child()
c.m1()
c.m2()
print(c.a,c.b,c.d)

'''
Types of Inheritance:
i). Single - 1P to 1C
ii). Multi level - 1P to 1C to 1CC
iii). Hierarchical - 1P to 2C ; equalent to 2 single inheritance
iv). Multiple - 2P to 1C
v). Hybrid combination of above
vi). Cyclic - one class to another in a cyclic way

'''
#Multi level inheritance
class P:
    pass
class C(P):
    pass
class CC(C):
    pass

#Multiple inheritance
class P1:
    pass
class P2:
    pass
class Child(P1,P2):
    pass

#super() Method: It is a bulit-in method to call the super class constructor, variables and methods from child class.
class Person:
    genre = 'human'
    def __init__(self,name):
        self.name = name
    def m1(self):
        print('This is instance method') 
    @classmethod
    def m2(self):
        print('This is class method')
    @staticmethod
    def m3(self):
        print('This is static method')

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def method(self):
        super().m1()
        super().m2()
        super().m3()
        print('Imported methods from super class')
    def variables(self):
            print(super().genre)    #calling class variable from super class
            print(self.name)    #calling class variable from super class


# POLYMORPHISM