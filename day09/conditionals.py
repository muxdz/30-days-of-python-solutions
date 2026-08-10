'''
Level 1 Exercises
'''

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
elif 0 <= age < 18:
    print("You are not old enough to drive yet. Wait for {} more years.".format(18 - age))


my_age = 20
your_age = int(input("Enter your age: "))
if my_age == your_age:
    print("We are the same age.")
elif my_age > your_age:
    print("I am {} years older than you.".format(my_age - your_age))
else:
    print("You are {} years older than me.".format(your_age-my_age))


num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))
if num1 > num2:
    print("{} is larger than {}".format(num1, num2))
elif num2 > num1:
    print("{} is larger than {}".format(num2, num1))
else:
    print("The numbers are equal")


'''
Level 2 Exercises
'''

score = int(input("Enter your score (0-100): "))
if 90 <= score <= 100:
    print("You got an A!")
elif 80 <= score <= 89:
    print("You got a B!")
elif 70 <= score <= 79:
    print("You got a C.")
elif 60 <= score <= 69:
    print("You got a D.")
else: 
    print("You got an F :(")


month = input("Enter a month: ")
if month in ['September', 'October', ' November']:
    print("The season is autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is winter.")
elif month in ['March', 'April', 'May']:
    print("The season is spring.")
elif month in ['June', 'July', 'August']:
    print("The season is summer.")
else:
    print("You have not entered a valid month.")


fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input('Enter a fruit: ')
if user_fruit.lower() in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(user_fruit)

'''
Level 3 Exercises
'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

skills = person.get('skills')
if skills is None:
    print("There is no skills")
else:
    print("The middle skill is:",skills[int(len(skills)/2)])
    print("Does the person have Python skills?", 'Python' in skills)

if 'React' in skills:
    if ['Node', 'Python', 'MongoDB'] in skills:
        print('He is a fullstack developer')
    if 'javaScript' in skills:
        print('He is a front end developer.')
elif ['Node', 'Python', 'MongoDB'] in skills:
    print('He is a backend developer')
else:
    print('Unknown title')

if person['is_married'] and person['country'] == 'Finland':
    print("{} {} lives in {}. He is married".format(person['first_name'],person['last_name'],person['country']))