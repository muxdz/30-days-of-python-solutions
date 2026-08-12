'''
Level 1 Exercises
'''

# Creating simple functions

def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(3,4))

def area_of_circle(radius):
    return 3.14 * radius * radius

print(area_of_circle(5))

def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add_all_nums(3,4,5))

def convert_celsius_to_fahrenheit(cel):
    return (cel * 9/5) + 32

print(convert_celsius_to_fahrenheit(30))

def check_season(month):
    if month in ['March', 'April', 'May']:
        return "Spring"
    elif month in ['June', 'July', 'August']:
        return "Summer"
    elif month in ['September', 'October', 'November']:
        return "Autumn"
    elif month in ['December', 'January', 'February']:
        return "Winter"
    else:
        return "Invalid month"

print(check_season("January"))

def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

print(calculate_slope(3, 3, 10, 10))

def solve_quadratic_eqn(a,b,c):
    sol1 = (-b + (b**2-4*a*c)**0.5) / 2*a
    sol2 = (-b - (b**2-4*a*c)**0.5) / 2*a
    return sol1, sol2

print(solve_quadratic_eqn(1,6,9))

def print_list(list):
    for element in list:
        print(element)

print_list(['December', 'January', 'February', 'September', 'October', 'November'])

def reverse_list(list):
    rev_list = []
    for i in range(len(list)-1,-1,-1):
        rev_list.append(list[i])
    return rev_list

print(reverse_list(['December', 'January', 'February', 'September', 'October', 'November']))

def captialize_list_items(list):
    new_list = []
    for element in list:
        new_list.append(element.capitalize())
    return new_list

print(captialize_list_items(["apple", "pear", "banana"]))

def add_item(list, item):
    return list.append(item)

fruits = ["apple", "pear", "banana"]
print(add_item(fruits, "tomato"))

def sum_of_numbers(num):
    return (num * (num+1)) / 2

print(sum_of_numbers(100))

def sum_of_odds(num):
    total = 0
    for i in range(num):
        if (i%2 == 1):
            total += i
    return total

print(sum_of_odds(100))

def sum_of_evens(num):
    total = 0
    for i in range(num):
        if (i%2 == 0):
            total += i
    return total

print(sum_of_evens(100))

'''
Level 2 Exercises
'''

def evens_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num):
        if (i%2 == 0):
            evens += 1
        else:
            odds += 1
    return evens, odds

print(evens_and_odds(100))