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

#Print value in english of a digit - Recursion also can be used
x=eval(input("Enter a number between 0-9 "))
digits_in_words={0:"Zero", 1:"One", 2:"two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
print(digits_in_words[x])

#print character present in string index wise
for position,value in enumerate('Hello World!'):
    print(position,value)

#print 'hello' 10 times using for loop
for i in range(10):
    print("Hello")

#print odd numbers btwn 0-20
for i in range(21):
    if i%2!=0:
        print(i)

#print 10 to 1 in desc order
for i in range(10,0,-1):
    print(i)

#print sum of numbers inside the list
l=[1,2,3,4,5]
print(sum(l))

#print numbers using while loop
num=0
while num<=10:
    print(num)
    num+=1

#print sum of 1st n numbers
n=eval(input("Enter a max number: "))
sum=0
num=1
while num<=n:
    sum+=num
    num=num+1
print(f"The sum of 1 to {n} is {sum}")

#input names untill "Durga"
name=""
while name!="Durga":
    name=input("Enter a name: ")
    print(name)

#Nested Loop
#Form a right angled triangle with *
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()                  #or print(end='\n') meaning : start a newline by default

for i in range(1,6):
    print("* " * i)

for i in range(1,6):
    print(' '*(6-i),end='')
    print('* ' * i)

#print +ve and -ve index
word=input("Enter a name: ")
for position,letter in enumerate(word):
    neg=position - len(word)
    print(position, letter, neg)

#reversing letter
word="durga"
print(word[::-1])  #or below use one
print(''.join(reversed(word))) 

#removing space from begining and ending
word=" TCR BLR "
no_space_ends=word.strip()
print(no_space_ends)

#find first postion of a letter, count or occurance of a letter
name="Parvathi"
print(name.find('h'))
print(name.find('a',2))
print(name.count('a'))

#replacing a word with another
string='Python is easy'
new_string=string.replace('easy', 'very easy')
print(new_string)
print(id(string))
print(id(new_string))

#splitting a string and joining back
string='I had an apple yesterday.'
list=string.split()
print(list)
back_to_string=' '.join(list)
print(back_to_string)

sentence="learning Python is very Easy."
print(sentence.lower())
print(sentence.upper())
print(sentence.capitalize())
print(sentence.title())

print(sentence.startswith('learning'))
print(sentence.endswith('Easy')) #False as the sentence ends with 'Easy.' or '.'

#reversing
sentence="Durga Sir teaches Python"
print(sentence[::-1])  #1st type of reverse- reversing everything
list=sentence.split()
reversed_list=list[::-1]
reversed_sentence=' '.join(reversed_list)
print(reversed_sentence)  #2nd type of reverse- reversing sentence keeping words as it is
new_list=[]
for word in list:
    reversed_word=word[::-1]
    new_list.append(reversed_word)
new_sentence=' '.join(new_list)
print(new_sentence)    #3rd type of reverse- reversing each word keeping sentence as it is

#merge 2 strings by having letters alternatively
s1="ravi"
s2="reja"
i,j=0,0
result=''
while i<len(s1) or j<len(s2):
    if i<len(s1):
        result=result+s1[i]
        i=i+1
    if j<len(s2):
        result=result+s2[j]
        j=j+1
print(result)

input='B4A1D3'
x1=''
x2=''
for i in input:
    if i.isalpha():
        x1=x1+i
    if i.isdigit():
        x2=x2+i
#print(x1+x2)
final=sorted(x1)+sorted(x2)
print(''.join(final))

input='a4b3c2'  ###expected output=aaaabbbcc
output=''
for i in input:
    if i.isalpha():
        output=output+i
        previous=i
    else:
        output=output+previous*(int(i)-1)
print(output)
'''