#Module 9: Functions

#Exercises Level 1 (List comprehension)

"""1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
"""

def add_two_numbers(a,b):
  sum = a + b
  return sum

print(f'The sum of 3 and 5 is {add_two_numbers(3,5)}')

"""2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle"""

def area_of_circle(r):
  import math
  area = math.pi * r **2
  return area

print(f'The area of a circle of radius 7cm is {area_of_circle(7)} cm2')

"""3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback."""

def add_all_nums(*x):
  sum = 0
  for num in x:
    if type(num)==int or type(num)==float:
      sum +=num
    else:
      sum = 'Please enter a whole number'
  return sum
print(f'The sum of 2,3 and 5 is {add_all_nums(2,3,5)}')

"""4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit."""

def convert_celsius_to_fahrenheit(x):
  F = x * (9/5) + 32
  return F
print(f'32 degrees celsius is {convert_celsius_to_fahrenheit(32)} in Fahrenheits')

"""5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer"""

def check_season(month):
  if month in ['September','October','November']:
    season = 'Autumn or Fall'
  elif month in ['December','January','February']:
    season = 'Winter'
  elif month in ['March','April','May']:
    season = 'Spring'
  else: 
    season = 'Summer'
  return season

print('March is in: ',check_season('March'))

"""6. Write a function called calculate_slope which return the slope of a linear equation"""

def calculate_slope(y,m,c):
  return m

"""7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn."""

def solve_quadratic_eqn(a,b,c):
  x1 = (-b + (b**2 - 4 *a*c)**2)/ (2*a)
  x2 = (-b - (b**2 - 4 *a*c)**2)/ (2*a)
  return x1,x2
print(f'The solution set of x2 - 6x + 9 is {solve_quadratic_eqn(1,-6,9)}')

"""8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list"""

def print_list(y):
  for i in y:
    print(i)
print_list(['yam','mango','guava'])

"""9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)."""

def reverse_list(list):
  rev_list = []
  for i in range(len(list)-1,-1,-1):
    rev_list.append(list[i])
  return(rev_list)

reverse_list([1,2,3,4,5])

"""10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items"""

def capitalize_list_items(list):
  cap_list = []
  for i in range(len(list)):
    cap_list.append(list[i].upper())
  return cap_list

capitalize_list_items(['orange','mango','guava'])

"""11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

```
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
```
"""

def add_item(list,item):
  list.append(item)
  return list
print(add_item(['Facebook','Google'],'Apple'))

"""12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.


```
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
```


"""

def remove_item(list,item):
  if item in list:
    list.remove(item)
  return list
print(remove_item(['Facebook','Google'],'Google'))

"""13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

```
# print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050

```


"""

def sum_of_numbers(num):
  sum = 0
  for i in range(num+1):
    sum += i
  return sum
print(f' The sum of numbers upto 5 is {sum_of_numbers(5)}')

"""14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range."""

def sum_of_odds(num):
  sum = 0
  for i in range(num+1):
    if i % 2 ==1:
      sum += i
  return sum

print(f'The sum of odd numbers upto 7 is {sum_of_odds(7)} ')

"""15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range."""

def sum_of_evens(num):
  sum = 0
  for i in range(num+1):
    if i % 2 == 0:
      sum +=i
  return sum
print(f'The sum of even numbers upto 10 is {sum_of_evens(10)} ')

"""## <div align='center'>**Exercises: level 2**

1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
"""

# Here, the assumption is that zero is not a number
def evens_and_odds(int):
  num_even = 0
  num_odd = 0
  for i in range(int +1):
    if i % 2 == 0:
      num_even += 1
    else: 
      num_odd +=1
  return f'The number of odd are: {num_odd} \nThe number of even are: {num_even}'
print(f'For 100, {evens_and_odds(100)}')

"""2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number"""

def factorial(x):
  fact = 1
  for i in range(1,x+1):
    fact *= i
  return fact
print(f'The factorial of 6 is {factorial(6)} ')

"""3. Call your function is_empty, it takes a parameter and it checks if it is empty or not"""

def is_empty(x):
  if len(x) == 0:
    state = 'Empty'
  else:
    state = 'Not empty'
  return state
print(is_empty(()))

"""4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation)."""

def calculate_mean(list):
  sum = 0
  for i in range(len(list)):
    sum += list[i]
  mean = sum / len(list)
  return mean
print(f'The mean of [1,2,3,4,5]: {calculate_mean([1,2,3,4,5])}')

def calculate_median(list):
  list_length = len(list)
  list.sort()
  if list_length % 2 == 0:
    median = (list[list_length//2] + list[list_length//2 - 1])/2
  else:
    median = list[list_length//2]
  return median

print(f'The median of [1,3,4,5,2]: {calculate_median([1,3,4,5,2])}')
print(f'The median of [1,4,3,2]: {calculate_median([1,4,3,2])}')

def calculate_mode(list):
  dic = {}
  for item in list:
      dic[item] = dic.get(item,0) + 1
  return [i for  i,j in dic.items() if j == max(dic.values()) ]
    
print(f'The mode of [1,1,1,3,4,5,6,6,6,8,8,1,1]: {calculate_mode([1,1,1,3,4,5,6,6,6,8,8,1,1])}')

def calculate_range(list):
  list.sort()
  range = list[len(list)-1] - list[0]
  return range
print(f'The range of [10,90,5,3,6,7]: {calculate_range([10,90,5,3,6,7])}')

def calculate_variance(list):
  sum = 0
  sum_of_diffs = 0
  for i in range(len(list)):
    sum += list[i]
  mean = sum / len(list)
  for i in range(len(list)):
    sum_of_diffs +=  (list[i] - mean ) ** 2
  variance = sum_of_diffs/(len(list) - 1)
  return variance

print(f'The variance of [1,2,4,5,6,7,8]: {calculate_variance([1,2,4,5,6,7,8])}')

def calculate_std(list):
  sum = 0
  sum_of_diffs = 0
  for i in range(len(list)):
    sum += list[i]
  mean = sum / len(list)
  for i in range(len(list)):
    sum_of_diffs +=  ((list[i] - mean ) ** 2)
  sd = (sum_of_diffs/(len(list)-1)) ** (1/2)
  return sd

print(f'The sd of [1,2,4,5,6,7,8] : {calculate_std([1,2,4,5,6,7,8])}')
# Exercises: level 3

"""1. Write a function called is_prime, which checks if a number is prime.
"""

def is_prime(x):
  div = []
  for i in range(2,x):
     if  x % i == 0:
       div.append(i)
  if len(div) == 0:
    prime = 'Prime'
  else:
    prime = 'Not Prime'
  return prime

print(f'24: {is_prime(24)}')


"""2. Write a functions which checks if all items are unique in the list.

"""

def check_unique(list):
  if len(list) == len(set(list)):
    result = 'All items are unique'
  else:
    result = 'Some items are duplicated'
  return result
print(f'are items in [1,2,3,4,5] unique? : {check_unique([1,2,3,4,5])}')


"""3. Write a function which checks if all the items of the list are of the same data type."""

def same_data_type(list):
  types = []
  for i in range(len(list)):
    types.append(type(list[i]))
  types_set = set(types)
  if len(types_set) == 1:
    data = "All items in the list are of the same data type"
  else:
    data = "Items in the list are not of the same data type"
  return data
print(same_data_type(['friends','foes']))


"""4. Write a function which check if provided variable is a valid python variable,  the conditions are:



*   A variable name cannot start with a number

*   A variable name must start with a letter or the underscore character and can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )



"""

def is_python_variable(name):
    if name[0] not in ['0','1','2','3','4','5','6','7','8','9'] and ' ' not in name:
       result = 'A valid variable name'
    else:
      result = 'Not a valid variable name'
    return result

is_python_variable('c_m ')



"""5. Go to the data folder and access the countries-data.py file.
Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order.
Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

"""
# importing the countries_data list from the country_data.py file
from country_data import countries_data
def most_spoken_languages():

    # looping to get dict of languages
    languages = []
    for i in range(len(countries_data)):
      languages.extend(countries_data[i]['languages'])

    lang = {}
    for language in languages:
        lang[language] = lang.get(language,0) + 1

# sorting the list of the tuples to get the most spoken languages
    sorted_lang = sorted(lang.items(), key= lambda x:x[1],reverse=True)
    sorted_lang # contains the languages arranged based on values
    # for the top ten, another loop
    top_ten = []
    for i in range(10):
        top_ten.append(sorted_lang[i])
    return top_ten

print(f'most spoken languages:  {most_spoken_languages()}')




def most_populated_countries():
    population = {}
    for i in range(len(countries_data)):
        keys = countries_data[i]['name']
        values = countries_data[i]['population']
        population[keys] = values
# sorting the list of the tuples to get the most spoken languages
    sorted_pop = sorted(population.items(), key= lambda x:x[1],reverse=True)
 # contains the languages arranged based on values
# for the top ten, another loop
    most_pop = []
    for i in range(10):
        most_pop.append(sorted_pop[i][0])

    return most_pop

print(f'most populated countries: {most_populated_countries()}')

