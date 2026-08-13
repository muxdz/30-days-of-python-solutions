# Comprehension for list
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

only_neg = [num for num in numbers if num <= 0]
print(only_neg)

ls_of_tuples = [(num, num**0, num**1, num**2, num**3, num**4, num**5) for num in range(11)]
print(ls_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]

print(output)

dictionary = [{'country': country[0][0], 'city': country[0][1]} for country in countries]
print(dictionary)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
joined_names = [name[0][0] + ' ' + name[0][1] for name in names]
print(joined_names)

# Lambda function
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

print(slope(3, 2, 8, 10))
