import os
logo='''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''
print(logo)
print("Welcome to the secret auction program!")

dict={}

new='yes'
while new=='yes':
  name=input("What is your name?: ")
  bid_amount=int(input("Wat's your bid?: $"))
  dict[name]=bid_amount
  #print(dict)
  new=input("Are there any other bidders? Type yes or no. \n")
  #clear()
  if new=='no':
    amount=list(dict.values())
    highest=max(amount)
    winner=list(dict.keys())[list(dict.values()).index(highest)]
print(f"The winner is {winner} who bid with ${highest}.")