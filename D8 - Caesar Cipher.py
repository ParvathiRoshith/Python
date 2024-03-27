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

#direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
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

def decrypt(message,number):
    word2=''
    for letter in message:
        if letter==' ':
            word2+=' '
        elif letter in symbol:
            word2+=letter
        else:
            position=alphabet.index(letter)-number
            position=position%26
            word2+=alphabet[position]
    print("Here's the decoded result:",word2)

again='yes'
while again=='yes':
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction=='encode':
        text=input("Type your message:\n").lower()
        shift=int(input("Type the shift number:\n"))
        encrypt(msg=text,num=shift)
    elif direction == 'decode':
        text=input("Type your message:\n").lower()
        shift=int(input("Type the shift number:\n"))
        decrypt(message=text,number=shift)
    else:
        print('Invalid Input')
    again=input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
