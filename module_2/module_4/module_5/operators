# Declare your age as integer variable
age = 35

# Declare your height as a float variable
height = float(24.7)

# Declare a variable that store a complex number
myNum = (3+2j)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = int(input("Input the base : "))
h = int(input("Input the height : "))
area = 0.5 * b * h
print("area = ", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)

a = int(input("Enter side a : "))
b = int(input("Enter side b : "))
c = int(input("Enter side c : "))
perimeter = a + b + c
print("Perimeter = ", perimeter)


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)
def calculate_rectangle_area(length, width):
    return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")

perimeter = 2 * (length + width)
print(f"The perimeter of the rectangle is: {perimeter}")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

from math import pi
r = float(input("Input the radius of the circle : "))
area = pi * r ** 2
c = 2 * pi * r
print("The area of the circle with circumference " + str(c) + " is: " + str(area))

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Find the slope
slope = 2

# Find the y-intercept
y_intercept = -2

# Find the x-intercept
x_intercept = 1  # since equation(1) = 0

# Print the results
print("Slope: ", slope)
print("Y-intercept: ", y_intercept)
print("X-intercept: ", x_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Import the math module to use the square root function.
import math

# Define the coordinates of the first point (p1) as a list.
p1 = [2, 2]

# Define the coordinates of the second point (p2) as a list.
p2 = [6, 10]

# Calculate the distance between the two points using the distance formula.
# The formula computes the Euclidean distance in a 2D space.
distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

# Print the calculated distance.
print(distance)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') == len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on in python and dragon', 'on' in 'python', 'on' in 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon in I hope this course is not full of jargon', 'jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
print('on not in dragon and python', 'on' not in 'python', 'on' not in 'dragon')

# Find the length of the text python and convert the value to float and convert it to string
text_length = len("python")
length_as_float = float(text_length)
length_as_string = str(length_as_float)

print("Length as an integer:", text_length)
print("Length as a float:", length_as_float)
print("Length as a string:", length_as_string)

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

    # Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3

converted_value = int(2.7)

if floor_division == converted_value:
    print("The values are equal.")
else:
    print("The values are not equal.")

print("Floor division result:", floor_division)
print("Converted value:", converted_value)

# Check if type of '10' is equal to type of 10

if type('10') == type(10):
    print("The types are equal.")
else:
    print("The types are not equal.")

# Print the types for clarity
print("Type of '10':", type('10'))
print("Type of 10:", type(10))


# Check if int('9.8') is equal to 10

num = int(float('9.8'))  # Convert to float first, then to integer
print("Conversion successful. Result:", num)

if num == 10:
        print("int('9.8') is equal to 10.")
else:
        print("int('9.8') is not equal to 10.")

print("Cannot convert '9.8' to an integer.")

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))

pay = hours * rate_per_hour

print(f"The total pay is: {pay:.2f}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60  # Number of seconds in a year
MAX_LIFE_YEARS = 100  # Maximum years a person can live

years = int(input("Enter the number of years: "))

if years > MAX_LIFE_YEARS:
        print(f"Input exceeds maximum life expectancy of {MAX_LIFE_YEARS} years.")
else:
        seconds_lived = years * SECONDS_IN_A_YEAR

        print(f"In {years} years, you can live approximately {seconds_lived:,} seconds.")

# Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125

# Display the table header
print(f"{'Number':<5}{'1':<5}{'Square':<5}{'Cube':<5}{'Power of 4':<5}")

# Generate and display the rows
for number in range(1, 6):
    square = number ** 2
    cube = number ** 3
    power_of_4 = number ** 4
    print(f"{number:<5}{1:<5}{square:<5}{cube:<5}{power_of_4:<5}")