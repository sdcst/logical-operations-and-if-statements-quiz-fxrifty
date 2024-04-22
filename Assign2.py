"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
math.sqrt
x=float(input('Enter a Float Value\n'))
y=float(input('Enter Another Float Value\n'))
z=math.sqrt(x**2+y**2)
z=round(z,1)
print(z,'This is The Length of The Missing Side')