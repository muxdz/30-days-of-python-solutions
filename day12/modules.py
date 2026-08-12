'''
Level 1 Exercises
'''

from random import randint
import string

def random_user_id():
    possible_chars = string.ascii_letters + string.digits
    return ''.join(possible_chars[randint(0, len(possible_chars) - 1)] for _ in range(6))

print(random_user_id())

def user_id_gen_by_user():
    num_of_characters = int(input("Enter number of characters: "))
    num_of_ids = int(input("Enter number of ids: "))
    possible_chars = string.ascii_letters + string.digits
    return [ ''.join(possible_chars[randint(0, len(possible_chars) - 1)] for _ in range(num_of_characters)) for _ in range(num_of_ids)]

print(user_id_gen_by_user())

def rgb_color_gen():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

print(rgb_color_gen())

