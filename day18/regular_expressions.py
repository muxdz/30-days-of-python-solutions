'''
Level 1 Exercises
'''

import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

word_count = []

words = re.split(" ", paragraph)
for word in set(words):
    all = re.findall(word, paragraph, re.I)
    word_count.append((word, len(all)))

sorted_word_count = sorted(word_count, key=lambda x: x[1], reverse=True)
print(sorted_word_count)


points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points = sorted(points, key=lambda x: int(x))
sorted_points = [int(x) for x in sorted_points]

range = sorted_points[-1] - sorted_points[0]
print(range)


'''
Level 2 Exercises
'''

def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, variable) != None

print(is_valid_variable('name'))
print(is_valid_variable('2name'))

'''
Level 3 Exercises
'''

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_sentence = re.sub(r'[^\w\s,.]', '', sentence)
print(cleaned_sentence)

def most_frequent_words(sentence):
    words = re.split(" ", sentence)
    word_count = []
    for word in set(words):
        all = re.findall(word, sentence, re.I)
        word_count.append((word, len(all)))
    sorted_word_count = sorted(word_count, key=lambda x: x[1], reverse=True)
    return sorted_word_count

print(most_frequent_words(cleaned_sentence))