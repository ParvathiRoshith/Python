logo='''                                                      
.------.            _     _            _    _            _    
|A_  _ |           | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\

      |  \/ K|                            _/ |                
      `------'                           |__/                 
'''
print(logo)
import random
game=[11,2,3,4,5,6,7,8,9,10,10,10,10]

gaming=True
while gaming==True:
    player1=random.sample(game,2)
    print(f'Your cards: {list(player1)}')
    player2=random.sample(game,2)
    print("Computer's first card:",player2[0])
    move=input("Type 'y' to get another card, type 'n' to pass: ")
    if move=='y':
        player1=player1+random.sample(game,1)
    elif move=='n':
        player1=player1
    print('Your final hand: ',player1)
    total1=sum(player1)
    print('Computer\'s final hand: ',player2)
    total2=sum(player2)
    if total1>total2 and total1<=21:
        print('You Won')
    elif total1==total2:
        print('Draw')
    else:
        print('You Loss')
    next_game=input("Do you want play again the game of BlackJack? Type 'y' or 'n': ")
    if next_game=='y':
        gaming=True
    else:
        gaming=False
