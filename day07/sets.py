# Given sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Length of it_companies:", len(it_companies))
it_companies.add('Twitter')

it_companies.update(['LinkedIn', 'Snapchat'])

it_companies.remove('Facebook')

print("Updated it_companies:", it_companies)

# Difference between remove and discard
it_companies.discard('Oracle')  # This will not raise an error if the element is not found
it_companies.remove('Google')  # This will raise a KeyError if the element is not found

'''
Level 2 Exercises
'''

# Set methods
a_and_b = A.union(B)
print("Union of A and B:", a_and_b)

a_intersection_b = A.intersection(B)
print("Intersection of A and B:", a_intersection_b)

print("Is A a subset of B?", A.issubset(B))

print("Are A and B disjoint sets?", A.isdisjoint(B))

A.update(B)
B.update(A)

joint_ab = A.union(B)
print("Joint set of A and B:", joint_ab)

print("Symmetric difference between A and B:", A.symmetric_difference(B))

del A, B  # Delete sets A and B

'''
Level 3 Exercises
'''

age_set = set(age)
print("Length of age_set:", len(age_set))
print("Length of age list:", len(age))

'''
Difference between string, list, tuple and set

String: Sequence of characters
List: Ordered and mutable collection of elements
Tuple: Ordered and immutable collection of elements
Set: Unordered and mutable collection of unique elements

'''

sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
