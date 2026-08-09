# Creating tuples
empty_tuple = tuple()

brothers_tuple = ("Alice", "Bob", "Charlie")
sisters_tuple = ("Diana", "Eve", "Frank")

siblings_tuple = brothers_tuple + sisters_tuple

print("Number of siblings:", len(siblings_tuple))

# Changing tuples

family_members = siblings_tuple + ("Father", "Mother")

print("Family members:", family_members)

# Unpacking tuples
parents_tuple = family_members[-2:]  # Get the last two elements (Father and Mother)
print("Parents:", parents_tuple)

siblings_tuple = family_members[:-2]  # Get all elements except the last two (siblings)
print("Siblings:", siblings_tuple)

fruits_tuple = ("Apple", "Banana", "Cherry")
vegetables_tuple = ("Carrot", "Broccoli", "Spinach")
animal_products_tuple = ("Milk", "Cheese", "Yogurt")
food_stuff_tp = fruits_tuple + vegetables_tuple + animal_products_tuple

# Tuples vs lists
food_stuff_lt = list(food_stuff_tp)
middle_from_list = food_stuff_lt[1:4]  # Get elements from index 1 to 3
middle_from_tuple = food_stuff_tp[1:4]  # Get elements from index 1 to 3

print("Middle from list:", middle_from_list)
print("Middle from tuple:", middle_from_tuple)

first_three_from_list = food_stuff_lt[:3]  # Get the first three elements
first_three_from_tuple = food_stuff_tp[:3]  # Get the first three elements

print("First three from list:", first_three_from_list)
print("First three from tuple:", first_three_from_tuple)

del food_stuff_tp  # Delete the tuple

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Is Estonia a Nordic country?", 'Estonia' in nordic_countries)
print("Is Iceland a Nordic country?", 'Iceland' in nordic_countries)
