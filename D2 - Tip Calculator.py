print("Welcome to the Tip Calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
split=int(input("How many peoplw to split the bill? "))
total=((tip/100)*bill)+bill
splitbill=format((total/split),".2f")
print(f"Each person should pay: ${splitbill}")