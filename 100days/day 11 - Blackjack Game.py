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

game=[11,2,3,4,5,6,7,8,9,10,10,10,10]
import random
player1=random.sample(game,2)
print(f'Your cards: {list(player1)}')

player2=random.sample(game,2)
print("Computer's first card:",player2[0])