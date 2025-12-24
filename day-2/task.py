print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip = (tip + 100) / 100
split = (bill / people) * tip
split = round(split, 2)
print(f"You have to split ${split} between {people} people.")