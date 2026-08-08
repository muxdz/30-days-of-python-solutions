# Declaring lists
empty = []
fruits = ["apple", "banana", "orange", "kiwi", "mango", "grape", "pineapple"]

# Accessing list elements
print("Length of the fruits list:", len(fruits))
print("First fruit:", fruits[0])
print("Middle fruit:", fruits[len(fruits) // 2])
print("Last fruit:", fruits[-1])

# Different lists
mixed_data_types = ["Muadz", 20, 1.75, True, None]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(mixed_data_types)
print(it_companies)

print("Number of IT companies:", len(it_companies))
print("First IT company:", it_companies[0])
print("Middle IT company:", it_companies[len(it_companies) // 2])
print("Last IT company:", it_companies[-1])

# Modyfying lists
it_companies[0] = "Meta"
print("Modified IT companies list:", it_companies)

# Editing elements in a list
it_companies.append("Tesla")

it_companies.insert(3, "Netflix")

it_companies[3] = it_companies[3].capitalize()

joined_companies = "#; ".join(it_companies)
print("Joined IT companies:", joined_companies)

print("Is Tesla in the list of IT companies?", "Tesla" in it_companies)

# Sorting and reversing lists
sorted_companies = sorted(it_companies)
print("Sorted IT companies list:", sorted_companies)

reversed_companies = it_companies[::-1]
print("Reversed IT companies list:", reversed_companies)

# Slicing lists
first_3_companies = it_companies[:3]
print("First 3 IT companies:", first_3_companies)

last_3_companies = it_companies[-3:]
print("Last 3 IT companies:", last_3_companies)

middle_companies = it_companies[len(it_companies) // 2 - 1]
print("Middle IT company:", middle_companies)

# Removing elements from a list
it_companies.remove(it_companies[0])
print("IT companies list after removing the first company:", it_companies)

it_companies.remove(it_companies[len(it_companies) // 2])
print("IT companies list after removing the middle company:", it_companies)

it_companies.remove(it_companies[-1])
print("IT companies list after removing the last company:", it_companies)

it_companies.clear()
print("IT companies list after clearing all elements:", it_companies)

del it_companies

# Joining lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print("Full stack development technologies:", full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print("Full stack development technologies after adding Python and SQL:", full_stack)


'''
Level 2 Exercises
'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sorted_ages = sorted(ages)

print("Minimum age:", sorted_ages[0])
print("Maximum age:", sorted_ages[-1])

print("Median age:", sorted_ages[len(sorted_ages) // 2])

print("Average age:", sum(sorted_ages) / len(sorted_ages))
print("Range of ages:", sorted_ages[-1] - sorted_ages[0])

print("min - average value: ", abs(sorted_ages[0] - (sum(sorted_ages) / len(sorted_ages))))
print("max - average value: ", abs(sorted_ages[-1] - (sum(sorted_ages) / len(sorted_ages))))

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
];

first_half_countries = countries[:len(countries) // 2]
second_half_countries = countries[len(countries) // 2:]

small_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_three = small_countries[:3]
scandic_countries = small_countries[3:]
print("First three countries:", first_three)
print("Scandic countries:", scandic_countries)