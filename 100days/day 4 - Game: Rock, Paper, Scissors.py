# Heads or Tails
coin=['Head','Tail']
import random
output=random.choice(coin)
print(output)

# Game
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game=[rock,paper,scissors]
player1=int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(game[player1])

print('Computer chose:')
player2=random.randint(0,2)
print(game[player2])

if (player1==0 and player2==2) or (player1==1 and player2==0) or (player1==2 and player2==1):
    print('You Win!')
elif player1==player2:
    print('Draw!')
else:
    print('You Lose.')