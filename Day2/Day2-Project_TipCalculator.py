print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

each_person_bill = round((bill / people ) * ((tip_percentage / 100) + 1), 2)
print(f"Each person would pay ${each_person_bill}")