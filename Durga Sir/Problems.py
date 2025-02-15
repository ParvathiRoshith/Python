'''
#find biggest of 2 given nums
nums=[eval(i) for i in input("Enter two comman-separated numbers: ").split(',')]
biggest=max(nums)
print(f"The biggest number is {biggest}")

#find smallest of given 3 numbers
n=[eval(x) for x in input("Enter 3 numbers \n").split()]
if n[0]<n[1] and n[0]<n[2]:
    print("The smallest number is",n[0])
elif n[1]<n[2]:
    print("The smallest number is",n[1])
else:
    print("The smallest number is",n[2])

#Given number is even or odd?
n=eval(input("Enter a number \n"))
if n%2==0:
    print(f"{n} is even")
else:
    print(n,"is odd")

#If a given num is btwn 1 and 100
x=eval(input("Enter a number "))
if 1<=x<=100:
    print(x)
else:
    print("Out of range")
'''
#Print value in english of a digit - Recursion also can be used
x=eval(input("Enter a number between 0-9 "))
digits_in_words={0:"Zero", 1:"One", 2:"two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
print(digits_in_words[x])