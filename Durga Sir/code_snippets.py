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
    return x**x
assert squareIt(3)==9,"The square of 3 should be 9q "
