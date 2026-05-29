import math

try:
    birthYear = int(input("Enter your birthYear: "))
    currentYear = 2026

    if birthYear > currentYear:
        print("Whoa! Don't get cheeky - Enter a year before current year!")

    else:
        result = math.fabs(birthYear - currentYear)
        print(f"You are {int(result)} years old, wow!") #  Perfectly aligned!

except ValueError:
    print("That was not a valid number! Please enter a real birthyear")
