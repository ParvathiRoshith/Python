from IPython.display import clear_output
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

new='yes'
while new=='yes':
    name=input("What is your name?: ")
    bid_amount=int(input("Wat's your bid?: $"))
    new=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear_output(wait=True)