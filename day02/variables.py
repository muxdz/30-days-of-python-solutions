# Day 2: 30 days of python programming

# Declaring different types of variables
first_name = 'Muadz'
last_name = 'Nizam'
full_name = first_name + ' ' + last_name
country = 'United Kingdom'
city = 'Coventry'
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = False
middle_name, is_student, height = 'Bin', True, 1.75

# Checking types of variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(middle_name))
print(type(is_student))
print(type(height))

# Length of variables
print(len(first_name))
print(len(last_name))

# Arithmetic operations with variables
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

# Taking inputs from users
rad_input = input("Enter radius: ")
area_of_circle = 3.14 * int(rad_input) ** 2
print("Area of circle:", area_of_circle)
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

help('keywords')
