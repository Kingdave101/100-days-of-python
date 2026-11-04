age = int(input("What is your current age: "))

days_lived = age * 365
weeks_lived = age * 52
months_lived = age * 12

#If user was to live up to 90 years old
days_left = (90 * 365) - days_lived
weeks_left = (90 * 365) - weeks_lived
months_left = (90 * 12) - months_lived

print(f"you have {days_left} days, {weeks_left} weeks, {months_left} months before turning 90")