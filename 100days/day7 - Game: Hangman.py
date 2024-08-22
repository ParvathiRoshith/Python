#Step-by-step exercises
'''
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list=['ardvark','baboon','camel']
print(word_list)

#STEP 1
#Exercise-1
import random
chosen_word=random.choice(word_list)
#print(chosen_word)
#Exercise-2
#guess=input("Guess a letter: ").lower()
#Exercise-3
'''
for letter in chosen_word:
    if letter==guess:
        print("Right")
    else:
        print("Wrong")
'''

#STEP 2
#Exercise-1
display=[]
for i in range(len(chosen_word)):
    display+='_'
#Exercise-2
'''
for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter==guess:
        display[position]=letter
#Exercise-3
print(display)'''

#STEP 3
end_of_game=False
lives=len(hangmanpics)
while end_of_game!=True:
    guess=input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
            
    if '_' not in display:
        end_of_game=True
        print('You Won!')
    
    if guess not in chosen_word:
        lives-=1
        hangmanpics.sort(reverse=True)
        print(hangmanpics[lives])
        
    if lives==0:
        end_of_game=True
        print('You Lose.')
        
print('Game Over.')
'''


#Final Game
import random
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list=['ardvark','baboon','camel']
chosen_word=random.choice(word_list)

display=[]
for x in range(len(chosen_word)):
    display+='_'
  
game_end=False
lives=len(hangmanpics)

while game_end==False:
    guess=input("Guess a letter:")
    if guess in display:
        print(f"You've already guessed {guess}.")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    print(display)
    if '_' not in display:
        game_end=True
        print('You Won.')
    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        hangmanpics.sort(reverse=True)
        print(hangmanpics[lives])
    if lives==0:
        game_end=True
        print('You Lose.')
print('Game Over.')
