height = input("Enter your height in m: ")
weight = input("Enter your weight in m: ")

BMI = (int(weight) / float(height) ** 2)
print("You have a BMI of " + str(BMI))