# Declarating different variables
age = 20
height = 1.75
complex_num = 3 + 3j

# Area of triangle calculator
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is ", area)

# Perimeter of triangle calculator
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is: ", perimeter)

# Area and perimeter of a rectangle
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is ", area)
print("The perimeter of the rectangle is ", perimeter)

# Area and circumference of a circle
radius = int(input("Enter radius: "))
area = 3.14 * (radius**2)
circumference = 2 * 3.14 * radius
print("The area of the circle is ", area)
print("The circumference of the circle is ", circumference)

# Slope, x-intercept and y-intercept of y = 2x - 2
print("The slope is 2")
print("The x-intercept is ", 2 / 2)
print("The y-intercept is ", 2 - 2)

# Slope and euclidean distance between (2, 2) and (6, 10)
slope = (6-2)/(10-2)
distance = ((6-2)**2 + (10-2)**2)**0.5
print("The slope is ", slope)
print("The euclidean distance is ", distance)

# Calculating y = x^2 + 6x + 9
x = int(input("Enter x value: "))
y = x**2 + 6*x + 9
print("The value of y is ", y)

# Comparing 'python' and 'dragon'
print("'python' is longer than 'dragon': ", len('python') > len('dragon'))
print("Is 'on' found in both 'python' and 'dragon'? ", ("on" in 'python') and ('on' in 'dragon'))
print("'I hope this course is not full of jargon'. Is 'jargon' in the sentence? ", 'jargon' in 'I hope this course is not full of jargon')
print("There is no 'on' in 'dragon' and 'python. ", 'on' not in 'dragon' and 'on' not in 'python')

# Length of 'python', into float and string
length = len('python')
float_value = float(length)
string_value = str(length)

# Checking if number is even
num = int(input("Enter any number: "))
is_even = num % 2 is 0
print("The number you entered is even? ", is_even)

# Checking different statements
print("Is 7 // 3 equal to 2.7 as an int? ", 7//3 == int(2.7))
print("Is the type of '10' equal to 10? ", type('10') == type(10))
print("Is int('9.8') equal to 10? ", int(9.8) == 10 )

# Calculating weekly earnings
hours = int(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
earnings = hours * rate
print("Your weekly earning is ", earnings)

# Number of seconds a person has lived
years_lived = int(input("Enter number of years you have lived: "))
seconds = years_lived * 365 * 24 * 60 * 60
print("You have lived for ", seconds, " seconds.")

# Printing power tables
for i in range(1,6):
    power_0 = i**0
    power_1 = i**1
    power_2 = i**2
    power_3 = i**3
    print(i, power_0, power_1, power_2, power_3)