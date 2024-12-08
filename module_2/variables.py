## Exercises: Level 1

#### Write a python comment saying 'Day 2: 30 Days of python programming'
print("Day 2: 30 Days of python programming")

#### Declare a first name variable and assign a value to it
first_name = 'Sani'

#### Declare a last name variable and assign a value to it
last_name = 'Bala'

#### Declare a full name variable and assign a value to it
full_name = f"{first_name}, {last_name}"

#### Declare a country variable and assign a value to it
country = 'Nigeria'

#### Declare a city variable and assign a value to it
city = 'Kano'

#### Declare an age variable and assign a value to it
age = 35

#### Declare a year variable and assign a value to it
year = 1987

#### Declare a variable is_married and assign a value to it
is_married = True

#### Declare a variable is_true and assign a value to it
is_true = 'first'

#### Declare a variable is_light_on and assign a value to it
is_light_on = 'yes'

#### Declare multiple variable on one line
first_name, last_name, country, age, is_married = 'Nura', 'Salim', 'Kano', 30, True

## Exercises: Level 2

#### Check the data type of all your variables using type() built-in function
first_name = 'Sani'
print(type(first_name));

last_name = 'Bala'
print(type(last_name));

full_name = (first_name, last_name)
print(type(full_name));

city ='Kano'
print(type(city));

country = 'Nigeria'
print(type(country));

age = 35
print(type(age));

year = 1987
print(type(age));

is_married = 'True'
print(type(is_married));

is_true = 'first'
print(type(is_true));

is_light_on = 'yes'
print(type(is_light_on));

#### Using the len() built-in function, find the length of your first name
first_name = 'Bala'
print(len(first_name));

last_name = 'Saminu'
print(len(last_name));

first_name, last_name = "Bala", "Saminu"
print(len(first_name), len(last_name))

#### Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4

#### Add num_one and num_two and assign the value to a variable total
total = (5 + 4)

#### Subtract num_two from num_one and assign the value to a variable diff
diff = (4 - 5)

#### Multiply num_two and num_one and assign the value to a variable product
product = (5 * 4)

#### Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
reminder = (4 % 5)

#### Calculate num_one to the power of num_two and assign the value to a variable exp
exp = (4**5)

#### Find floor division of num_one by num_two and assign the value to a variable floor_division
num_one = 5
num_two = 4
floor_division = (num_one//num_two)
print(floor_division)

#### Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math
diameter = float(30)
area_of_circle = math.pi*((diameter*diameter)/4)
print("area of a circle is:", area_of_circle,)

#### Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
import math
radius = float(10)
circum_of_circle = 2*math.pi*radius
print("circumference of a circle is:", circum_of_circle,)

#### Take radius as user input and calculate the area.
import math
radius = float(input("enter the radius of the circle:"))
area = 3.14*radius*radius
print("area of circle is:", area,)
