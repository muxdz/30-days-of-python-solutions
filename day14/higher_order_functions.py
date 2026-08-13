'''
Level 1 Exercises
'''

from functools import reduce
from countries_data import countries_data

'''
Map: Takes a function and iterable, returns a list of the results after applying the function to each item in the iterable.
Filter: Takes a function and iterable, returns a list of items from the iterable for which the function returns True.
Reduce: Takes a function and iterable, returns a single value by iteratively applying the function to the items in the iterable.
'''

'''
Higher order function: A function that can take a function as a variable and also return a function.

Closure: A function that has access to functions within itself.

Decorators: A function that modifies the behavior of another function without changing its source code.
'''

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def cube(num):
    return num ** 3

print(list(map(cube, numbers)))

def even(num):
    return num % 2 == 0

print(filter(even, numbers))

def sum(num1, num2):
    return num1 + num2

print(reduce(sum, numbers))

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

'''
Level 2 Exercises
'''

print(list(map(lambda text: text.upper(), countries)))

print(list(map(lambda text: text.lower(), countries)))

print(list(map(lambda text: text.upper(), names)))


print(list(filter(lambda text: 'land' in text, countries)))

print(list(filter(lambda text: len(text) == 6, countries)))

print(list(filter(lambda text: len(text) >= 6, countries)))

print(list(filter(lambda text: text[0] == 'E', countries)))


print(list(map(lambda text: text.upper(), list(filter(lambda text: 'land' in text, countries)))))

def get_string_lists(strs):
    return list(filter(lambda text: type(text) == str, strs))

print(get_string_lists(numbers))


print(reduce(lambda num1, num2: num1 + num2, numbers))

concat = lambda text1, text2: text1 +", "+ text2
print(reduce(concat, countries[0:len(countries)-1]), "and {} are the north European countires".format(countries[len(countries)-1]))

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
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
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
  'Montenegro',
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
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
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
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
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
  'Zimbabwe'
]

def catogrise_countires(countries, common):
    return list(filter(lambda text: common in text, countries))

print(catogrise_countires(countries, 'land'))

def starting_letter_dict(countries):
    return dict(map(lambda text: (text[0], text), countries))

print(starting_letter_dict(countries))

def get_first_ten_countries(countries):
    return countries[:10]

print(get_first_ten_countries(countries))

def get_last_ten_countries(countries):
    return countries[-10:]

print(get_last_ten_countries(countries))


'''
Level 3 Exercises
'''

def sort_by_name(countries):
    return sorted(countries, key=lambda country: country['name'][0])

print(sort_by_name(countries_data))

def sort_by_population(countries):
    return sorted(countries, key=lambda text: text["population"])

print(sort_by_population(countries_data))

def sort_by_captial(countries):
    return sorted(countries, key=lambda text: text["capital"])

print(sort_by_captial(countries_data))

def top_10_languages(countries):
    return sorted(countries, key=lambda text: len(text["languages"]), reverse=True)[:10]

print(top_10_languages(countries_data))

def top_10_populated_countries(countries):
    return sorted(countries, key=lambda text: text["population"], reverse=True)[:10]

print(top_10_populated_countries(countries_data))