import math 


pointA  = int(input("Enter a number for point A: "))

pointB = int(input("Enter a number for point B: "))

difference = pointA - pointB

distance = math.fabs(difference)

print(f"The distance between them is: {distance}")
