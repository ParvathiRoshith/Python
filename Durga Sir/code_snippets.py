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
print(s[:])
print(s[1:3])
print(s[1:])
print(s[:4])
print(s[::-1]) #reverse string

# TYPE CASTING - convering one type value to another type
#int(a) <<-- float, bool, str(integer value), immutable
#float(a) <<-- int, bool, str(integer/float value), immutable
#complex(a)/complex(a,b) <<-- int, bool, str(integer/float value), immutable
#bool() <<-- int, float, complex, str - immutable
#str() <<-- int, float, complex, str - immutable
#bytes() : values must be btwn (0,2560), immutable
#bytearray() : mutable
#list()/[] : mutable, ordered, duplicates
#tuple/() : immutable, ordered, duplicates
#range() : immutable
#set() : mutable, not ordered, no duplicates
#frozenset({}) : immutable, not ordered, no duplicates
#dict()/{} : mutable, not ordered, key-valuepairs (key-no duplicates, value-duplicate)

#Escape charaters - \n, \t, \', \",...

#OPERATIONS