#Loops
'''
student_scores=[150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]
sum=0
for i in student_scores:
    sum=sum+i
print(sum)

max=0
for score in student_scores:
    if score>max:
        max=score
print(max)
'''
#Password Creation
print('Welcome to the PyPassword Generator!')
import string
letters=list(string.ascii_letters)
symbols=list(string.punctuation)
num=list(string.digits)

#len_letters=int(input('How many letters would you like in your password?\n'))
#len_symbols=int(input('How many symbols would you like?\n'))
#len_num=int(input('How many numbers would you like?\n'))
#print(f"Your password is {output}")