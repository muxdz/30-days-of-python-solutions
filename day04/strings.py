# Concatenation of strings
concat_str = "Thirty " + "Days " + "Of " + "Python"
concat_coding = "Coding " + "For " + "All"

# String interpolation
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())

# Different string methods
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Slicing strings
print(company[7:12])

# Checking if 'Coding' is in the string
print("Is 'Coding' in the string? ", "Coding" in company)

# Replacing words
new_company = company.replace("Coding", "Python")

# Splitting strings
print(company.split(" "))
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))

# String indexing and finding
print(company[0])
last_index = company.rfind("l")
print(company[10])

# Creating acronyms
word = "Python For Everyone"
acronym = "".join([w[0].upper() for w in word.split()])
print(acronym)

word2 = "Coding For All"
acronym2 = "".join([w[0].upper() for w in word2.split()])
print(acronym2)

# Determining position of a substring
print(word2.index("C"))
print(word2.index("F"))
print("Coding For All People".rfind("l"))

# Manipulating longer strings
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))
print(sentence.rfind("because"))
slice_out = sentence[sentence.find("because"):sentence.rfind("because")+len("because")]
print(slice_out)
print(sentence.rindex("because"))

# Checking if a string starts or ends with a specific substring
print(company.startswith("Coding"))
print(company.endswith("All"))

# Removing trailing and leading whitespace
string = "   Coding For All   "
print(string.strip())

# Using isidentifier to check if a string is a valid identifier
word = "30DaysOfPython"
print(word.isidentifier())
word2 = "thirty_days_of_python"
print(word2.isidentifier())

# Joining strings with a separator
libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
joined_libraries = "# ".join(libraries)
print(joined_libraries)

# using line and tab escape sequences
print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\t\tAge\tCountry\tCity\nMuadz\t20\tUK\tCoventry")

# Using string formatting
radius = 10
area = 3.14 * radius ** 2
print("radius = {}".format(radius))
print("area = 3.14 * {} ** 2".format(radius))
print("The area of a circle with radius {} is {}".format(radius, area))

num1 = 8
num2 = 6
print("{} + {} = {}".format(num1, num2, num1 + num2))
print("{} - {} = {}".format(num1, num2, num1 - num2))
print("{} * {} = {}".format(num1, num2, num1 * num2))
print("{} / {} = {}".format(num1, num2, num1 / num2))
print("{} % {} = {}".format(num1, num2, num1 % num2))
print("{} // {} = {}".format(num1, num2, num1 // num2))
print("{} ** {} = {}".format(num1, num2, num1 ** num2))