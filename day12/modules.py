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

'''
Level 2 Exercises
'''

hex_char = string.hexdigits

def list_of_hexa_colors(num_of_colors):
    return [ '#' + ''.join( hex_char[randint(0, len(hex_char) - 1)] for _ in range(6)) for _ in range(num_of_colors)]

print(list_of_hexa_colors(5))

def list_of_rgb_colors(num_of_colors):
    return [rgb_color_gen() for _ in range(num_of_colors)]

print(list_of_rgb_colors(5))

def generate_colours(type, num_of_colors):
    if type == 'hex':
        return list_of_hexa_colors(num_of_colors)
    elif type == 'rgb':
        return list_of_rgb_colors(num_of_colors)
    else:
        return None

print(generate_colours('hex', 5))
print(generate_colours('rgb', 5))

'''
Level 3 Exercises
'''

from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

print(shuffle_list([1, 2, 3, 4, 5]))

def random_array():
    new_set = set()
    while len(new_set) < 7:
        new_set.add(randint(0, 9))
    return list(new_set)

print(random_array())