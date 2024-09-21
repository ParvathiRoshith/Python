print("Welcome to the Tip Calculator!")

#inputs
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
split=int(input("How many people to split the bill? "))

total=((tip/100)*bill)+bill

#splitting the total bill among the friends
splitbill=total/split
roundbill=format(splitbill,".2f")  # we want output always with 2 decimal

print(f"Each person should pay: ${roundbill}")
