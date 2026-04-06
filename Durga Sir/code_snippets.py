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
Equality - ==, !=
Logical - and, or, not
Bitwise - &, |, ^, ~, <<, >>
Assignment - =, +=, -=, *=, ...
Special operator - 
    Identity operator : is, is not    ['is' operation compares addresses while '==' operator compares contents]
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

.
.
.

# EXCEPTION HANDLING - handle runtime errors
try:
    print(10/0)
except:
    print("ZeroDivisionError")
else:                    #executed only if there are no exception thrown
    pass
finally:                    # always runs
    print("finally")

#custom exception
class InvalidAgeError(Exception):        #by inheriting from Exception parent class
    pass
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    return "Eligible"
print(check_age(16))

# LOGGING - that stores complete data flow & exceptions info in a file

import logging
logging.basicConfig(filename='log.txt',level=logging.CRITICAL)
logging.critical('this is a critical message')
msg='cannot divie by zero'
logging.exception(msg)

# DEBUGGING - identifying & fixing bugs. Used to alert programmer
asert 

def squareIt(x):
    return x**x             #x*x is correct
assert squareIt(3)==9,"The square of 3 should be 9"     #assert condition,message

# OBJECT ORIENTED PROGRAMMING SYSTEM - Class, Object, Inheritance, Polymorphisum, Abstraction, Encapsulation

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
Without existing of 1 object if there's no chance of existing another typpe of object then we go for inner classes.
To access method inside inner class - Outer().Inner().m1()
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

1). Composition (Has-A Relation) - by using class name/object we can access members of one class inside another class
                                 - extends the function so as to just use existing function

2). Inheritance (Is-A Relation) - one class inherts/gets variables, methods & constructors available from another class
                                - extends the function so as to extend the existing functionality
--
Aggregation(weak assosiation) v/s Composition(strong assosiation)
eg:    dept,prof                       clg,dept

Aggregation: Without existing of container object if there is a chance of the existance of contained object then container and contained objects are weakly associated.
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
    def m2(cls):
        print('This is class method')
    @staticmethod
    def m3(self):
        print('This is static method')

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        super().m1()
        super().m2()
        super().m3()
    def variables(self):
            print(super().genre)    #calling class variable from super class
            print(self.name)    #calling class variable from super class
    def method(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        print('Imported methods from super class')
    @classmethod                
    def child_class_method(cls):
        super().m2()
        super().m3()
        super(Child,cls).__init__(cls)      #parent constructor inside child classmethod
        super(Child,cls).m1(cls)            #parent instancemethod inside child classmethod
    @staticmethod
    def child_static_method():
        super(Child,Child).m1()             #parent methods in child static method
        super(Child,Child).m2()
        super(Child,Child).m3()

c=Child()
c.m1()
c.m2()
c.m3()

'''
POLYMORPHISM
**********
Poly = many; Morph = Forms
Same thing can be used for different purposes

1). Duck Typing Philosophy: Python lang is dynamically typed. No need to mention type explicitly. 
Based on provided value at runtime the type will be considered automatically.

2). Overloading: 
    (i) Operator overloading - using same operator(+/*) having diff purpose
    (ii) Method overloading - 2 methods having same name but diff type of arguments [with default argument]
    (iii) Constructor overloading - [with default argument]

3). Overriding: All members of parent class are by default available to child class through inheritance.
    If child class not satisfied with parent class implementation then child class is allowed to redefind
    that method in the child class.
    (i) Method overriding - 
    (ii) Constructor overriding -
'''

# Abstarct Method - declaring a method without knowing the implementation 

from abc import *
@abstractmethod
def m1(self):
    pass

# Abstract Class - declaring class with partial implementation

from abc import ABC
class Test(ABC):
    pass
t = Test()

# Interface - Abstract class containing only abstract methods

from abc import *
class DBinterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

#we cannot call 't = DBinterface()' since its abstract class with abstract method
class Oracle(DBinterface):
    def connect(self):
        print('connecting to oracle db')
    def disconnect(self):
        print('disconnecting to oracle db')
dbname='Oracle'
classname=globals()[dbname]         #converts string into classname
x = classname()
x.connect()
x.disconnect()

''' Access Modifiers
Access modifiers in Python control which parts of a class can be accessed from outside the class, from within the class, or by subclasses. 
They help keep data and methods safe and organized. 
Types of Access Modifiers in Python - public, private and protected
'''

# Public - bydefault attributes are public. Can be accessed from anywhere in the program
class Employee():
    def __init__(self):
        self.name = 'durga' 

# Protected - can be accessed from anywhere inside the class or subclass not be accessed outside the class
        self._age = 19

# Private - can be accessed only within the class. Direct access from outside will raise AttributeError
        self.__head = 'software'
t=Employee()
print(t._Employee__head)


# REGULAR EXPRESSION
# representing a group of strings in a particular format


# MULTI TASKING

'''
Executing multiple tasks simultaneously.
1). Multi processing - Executing multiple tasks simultaneously where each task is separate independent process

2). Multi threading - Executing multiple tasks simultaneously where each task is separate independent part of the same program.
                    - Each independent part is called as a thread
                    - This can lead to data inconsistency also, hence we need synchronization

'''
import threading
def display():
    for i in range(10):
        print('Child Thread')

t = threading.Thread(target=display)
t.start()                           #child thread starts
for i in range(10):
    print('Main Thread')
t.ident                 #thread id number
threading.current_thread().name()
threading.active_count()        #count of active threads
t.is_alive()        #checking whether a thread is still executing
t.join()            #to make a thread wait, untill completion of another thread [t.join(seconds)]  

# Daemon Thread - The thread that runs in the background. It provides support to the non daemon thread. eg Garbage Collector
threading.current_thread().isDaemon()

'''Synchronization / Race Condition - at a time only one Thread
A race condition occurs when two or more processes or threads access and modify the same data at the same time, and the final result depends on the order in which 
they run. Without proper coordination, this can lead to incorrect or unpredictable results. 
For example, if two people update the same bank account simultaneously without checking each other’s changes, the final balance may be wrong.

If multiple threads are executing simultaneously then there is a chance of data inconsistency problems.
In synchronization the threads will be executed one by one.
Main application areas are Online reservation system, fund transer from joint account

In python we can apply synchronisation in 3 ways:
1) Lock - lock object can be acquired only by one thread at a time
        - even owner thread cannot acquire the lock multiple times
        - most fundamental

2) Rlock - rlock object can be acquired only by one thread at a time
         - owner thread can acquire the lock multiple times
         - suited for recursive and nested cells

3) Semaphore - semaphore object can be acquired by limited number of threads by counter value
             - limiting access to shared resources with limited capacity
             - most advanced synchronisation mechanism
             - we can call release() any number of times

Bounded Semaphore where the number of release() should not exceed the number of acquire()
'''

import threading
l = threading.Lock()
def wish():
    l.acquire()
    print('name')
    l.release()
t = threading.Thread(target=wish)
t.start()

rl = threading.RLock()
def factorial(n):
    rl.acquire()
    if n==0:
        result = 1
    else:
        result = n * factorial(n-1)
    rl.release()
    return result
t = threading.Thread(target=factorial, args=(5,))
t.start()

s = threading.Semaphore(2)
def wish(name):
    s.acquire()
    print(f"his name is {name}")
    s.release()
t1 = threading.Thread(target=wish, args=("Dhoni",))
t2 = threading.Thread(target=wish, args=("Durga",))
t3 = threading.Thread(target=wish, args=("Yuvraj",))
t1.start()
t2.start()
t3.start()

#using with is the best option instead of everytime writing acquire and release

'''Inter thread communication
As a part of programming requirement, sometime threads are required to communicate with eachother.
We can implement this in following ways:

1) Event - one thread sends signal to an event and other thread waits for it.
         - simplest communication mechanism
         - set(), clear(), wait()

2) Condition - threads can wait & threads can be notified once condition happened or another thread
             - [acquire(), release()]/with, wait(), notify()
             - more advanced version of Event

3) Queue - most enhanced mechanism of inter communication
         - it internally has Condition and that condition has Lock, hence its thread-safe
         - q.put(), q.set

'''
event = threading.Event()
def method():
    for i in range(1,11,2):
        event.set()
        event.wait()
        print(i)
        event.clear()

condition = threading.Condition()
def method():
    for i in range(1,11,2):
        with condition:
            while not True:
                condition.wait()
            print(i)
            condition.notify()

import queue
q = queue.Queue()
def method():
    q.put()
    for i in range(1,11,2):
        q.get()

'''
3 types of Queue:

a). FIFO Queue - by default
b). LIFO Queue - removal/getting will happen in the reverse order of insert/putting
c). Priority Queue - elements will be inserted in some priority order
'''
