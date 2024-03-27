print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')
import string
alphabet=list(string.ascii_lowercase)
symbol=list(string.punctuation)

direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#text=input("Type your message:\n").lower()
#shift=int(input("Type the shift number:\n"))

def encrypt(msg,num):
    word=''
    for letter in msg:
        if letter==' ':
            word+=' '
        elif letter in symbol:
            word+=letter
        else:
            position=alphabet.index(letter)+num
            position=position%26
            word+=alphabet[position]
    print("Here's the encoded result:",word)

if direction=='encode':
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    encrypt(msg=text,num=shift)
elif direction == 'decode':
    print('done')
else:
    print('Invalid Input')
