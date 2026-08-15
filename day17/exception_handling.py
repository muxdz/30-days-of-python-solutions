# We can use try and except to handle exceptions

try:
    print(1/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Use else and finally to run code when there is no exception

try:
    print(1/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("There is no exception")
finally:
    print("The try/except is finished")


# Now unpacking and packing

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries , es, ru = names

print(nordic_countries)
print(es)
print(ru)
