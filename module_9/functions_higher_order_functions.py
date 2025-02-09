# Module 9: 

# Exercises: Level 1 (Higher Order Functions)

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explain the difference between map, filter, and reduce.
'''
Map ,filter and reduce bring some form of functional programming to python. 
All three functions take a function as the first argument and an iterable as the second argument of the function.
map and filter return an iterable, eg a list , though it actually returns a map object that can be cast into a list. 
map calls the function in the first argument and returns the result of the function for each of the elements in the iterable.
Filter on the other hand, only returns elements that satisfies the condition in the function argument. 
reduce is a bit different as it returns a single answer i.e. it reduces the iterable to a single answer.
It should be noted that map and filter functions return map objects and filter objects respectively.
Printing map and filter objects without casting to a list will give the memory location of the object.
'''
# Explain the difference between higher order function, closure and decorator
'''
A higher order function is a function that either takes in a function as a parameter or returns a function or both.
Decorators and closures are all higher order functions. 
Decorators return a closure and A closure is what is returned by a decorator.
Closures are used to preserve outer scope inside an inner scope,making variables act like they are private. 
Decorators are convenient ways to make changes to the functionality of code without making changes to the code. 
A decorator is written as a function closure
and implemented by giving the @ operator on top of the function.
'''
# Define a call function before map, filter or reduce, see examples.
# From my understanding, 
# I defined a function that will be called in the map function

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)


# Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# Use for to print each name in the names list.
for name in names:
    print(name)

# Use for to print each number in the numbers list.
for number in numbers:
    print(number)



# Exercises: Level 2

# Use map to create a new list by changing each country to uppercase in the countries list
upper_case_countries = list(map(lambda x:x.upper(),countries))
print(f'countries in upper case: {upper_case_countries} ')
# Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = list(map(lambda x:x**2,numbers))
print(f'The square of the numbers: {squared_numbers} ')
# Use map to change each name to uppercase in the names list
upper_case_names = list(map(lambda x:x.upper(),names))
print(f'Uppercase of the names: {upper_case_names} ')


# Use filter to filter out countries containing 'land'.
contains_land = list(filter(lambda x:'land' in x,countries))
print(f' The countries with land in their name: {contains_land}')

# Use filter to filter out countries having exactly six characters.
six_chars = list(filter(lambda x:len(x)==6,countries))
print(f'The countries with six characters: {six_chars} ')

# Use filter to filter out countries containing six letters and more in the country list.
six_or_more_chars = list(filter(lambda x:len(x) >= 6,countries))
print(f'Countries with six or more characters in their names: {six_or_more_chars} ')


# Use filter to filter out countries starting with an 'E'
starting_with_e = list(filter(lambda x:x.startswith('E'),countries))
print(f' Countries starting with E in the list are: {starting_with_e}')


# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

numbers = [3, 5, 8, 2, 14]
squared_even_numbers_sum = reduce(lambda x, y: x + y, 
                                   list(filter(lambda x: x % 2 == 0, 
                                                map(lambda x: x**2, numbers))))
print(squared_even_numbers_sum)

'''
Here, I start by using the map() function to square each element of the numbers list. The output of map(lambda x: x**2, numbers) is then passed as an argument to filter(), which filters out the elements that are not even. Finally, the output of filter() is passed as an argument to reduce(), which adds up all the elements in the list to get the sum.
As many list iterators can be chained, as long as each one produces an iterable that can be passed as an argument to the next function.
'''


# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(list):
    return [str(item) for item in list]

str_nums = get_string_lists(numbers)


# Use reduce to sum all the numbers in the numbers list.
from functools import reduce
def add(x,y):
    return x + y
sum_all = reduce(add,numbers)
print(f'The sum of {numbers} is {sum_all}')

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# work in progress
concat = reduce(lambda x,y:x + ',' + ' '+ y,countries[:-1])
print(f'{concat} and {countries[-1]} are North European countries ')


# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
# Declare a function called categorize_countries that returns a list of countries with some common pattern 
# (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(pattern):
    list_countries = []
    for country in countries:
        if pattern.lower() in country:
            list_countries.append(country)
    return list_countries

print(f'Countries with "pattern": ',categorize_countries('stan'))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def countries_dict():
    dict_countries = {}
    for country in countries:
        dict_countries[country[0]] = dict_countries.get(country[0],0) + 1
    return dict_countries
print(f' Dictionary of number of countries per letter: {countries_dict()}')


# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
    return countries[:10]

print(f' First ten countries in the countries list: {get_first_ten_countries()}')

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return countries[-10:]

print(f'The last ten countries in the countries list: {get_last_ten_countries()}')

# Exercises level 3 using list from a separate file (country_data.py)
'''Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
Sort countries by name, by capital, by population
Sort out the ten most spoken languages by location.
Sort out the ten most populated countries.'''


from country_data import countries_data


# Sorting list by name, by capital and by population
# by name
sorted_list_name = sorted(countries_data,key=lambda d: d['name'])
sorted_list_name[-11:] # checking a subset as the list is too large

# by capital
sorted_list_cap = sorted(countries_data,key=lambda d:d['capital'])
sorted_list_cap[-5:]  # checking subset

# by population
sorted_list_pop = sorted(countries_data,key=lambda d:d['population'])
sorted_list_pop[-5:]

'''ten most spoken languages by location: hmmm
I can get most spoken languages by number of countries the language is spoken in, 
but I dont understand what is meant by by location'''
lang_dict = dict()
for i in range(len(countries_data)):
    for language in countries_data[i]['languages']:
        lang_dict[language] = lang_dict.get(language,0) + 1
lang_tpl = sorted(lang_dict.items(),key= lambda x:x[1],reverse=True)
lang_tpl[:10]
# [('English', 91), ('French', 45), ('Arabic', 25), ('Spanish', 24), ('Portuguese', 9), ('Russian', 9), ('Dutch', 8), ('German', 7), ('Chinese', 5), ('Serbian', 4)]
# most spoken languages by the number of countries that language is spoken in

# ten most populated countries = sorted_list_pop in descending order, getting a new list
pop = sorted(countries_data,key= lambda d:d['population'],reverse=True)
top_ten =  pop[:10]
top_ten
# getting the countries from the top ten
top_pop_countries = []
for i in range(len(top_ten)):
    top_pop_countries.append(top_ten[i]['name'])
top_pop_countries
