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

game_on=True
while game_on==True:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess==number:
        print(f"You got it! The answer was {number}")
        break
    elif guess>number:
        print("Too high. \nGuess again.")
    elif guess<number:
        print("Too low. \nGuess again.")

