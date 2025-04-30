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
'''
import random
def pick_card():
    deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    pick=random.choice(deck)
    return pick
def calculate_score(deck):
    if len(deck)==2 and sum(deck)==21:
        return 0
    if 11 in deck and sum(deck)>21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)
def compare_score(u_score,c_score):
    if u_score==c_score:
        return "Draw"
    elif c_score==0 or c_score==21 or u_score>21 or u_score<c_score:
        return "You Loss"
    elif u_score==0 or u_score==21 or c_score>21 or u_score>c_score:
        return "You Won"
    else:
        return "Not accepted"

def play_game():
    print(logo)
    player1=[]  #user
    player2=[]  #computer
    game_end=False
    user_score=-1
    computer_score=-1

    for i in range(2):
        player1.append(pick_card())
        player2.append(pick_card())

    while game_end==False:
        print(f'Your cards: {player1}')
        print("Computer's first card: ",player2[0])
        user_score=calculate_score(player1)
        computer_score=calculate_score(player2)
        if user_score==0 or computer_score==0 or user_score>21:
            game_end=True
        else:
            move=input("Type 'y' to get another card, type 'n' to pass: ")
            if move=='y':
                player1.append(pick_card())
            elif move=='n':
                game_end=True

    while computer_score!=0 and computer_score<17:
        player2.append(pick_card())
        computer_score=calculate_score(player2) 
    
    print('Your final hand: ',player1)
    print('Computer\'s final hand: ',player2)
    print(compare_score(user_score,computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")=='y':
            #print('\n'*20) #clear terminal
            play_game()