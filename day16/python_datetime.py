from datetime import datetime, date

print(datetime.now())
print(date.today())

formatted = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print(formatted)

string = "Today is 5 December, 2019"
print(datetime.strptime(string, "%d %B, %Y"))

newyear = date(2026, 1, 1)
print(newyear - date.today())

old = (1970, 1, 1)
print(old - date.today())

'''
Date and time is useful for all sorts of tasks.
Examples:
- scheduling tasks
- website statistics
- logging, etc.
'''