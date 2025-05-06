import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number=random.randint(1,100)
#print(number)
lives=0
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=='easy':
    lives=10
elif difficulty == 'hard':
    lives = 5
else:
    print("Invalid")

game_end=False
while game_end==False:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess==number:
        print(f"You got it! The answer was {number}")
        game_end=True
    elif guess>number:
        print("Too high.")
    elif guess<number:
        print("Too low.")
    lives=lives-1
    if lives==0:
        print("You've run out of guesses, you lose.") 
        game_end=True
    else:
        print("Guess again.")


