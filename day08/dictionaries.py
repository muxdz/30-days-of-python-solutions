# Creating and editing dictionaries
dog = {}
dog['name'] = 'Fido'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 20,
    'is_married': False,
    'skills': ['Python', 'JavaScript', 'SQL'],
    'country': 'USA',
    'city': 'New York',
    'address': {
        'street': '123 Main St',
        'zipcode': '10001'
    }
}

print("Length of student dictionary:", len(student))
print("Student skills:", student['skills'])
print("Skills data type:", type(student['skills']))

student['skills'].append('HTML')
print("Updated student skills:", student['skills'])

# Methods with dictionaries
dog_keys = dog.keys()
dog_values = dog.values()
print("Dog keys:", dog_keys)
print("Dog values:", dog_values)

student_items = student.items()
print("Student items:", student_items)

student.pop('is_married')
del dog

