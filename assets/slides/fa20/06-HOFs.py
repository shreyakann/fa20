berkeley = 'The University of California at Berkeley'
book = 'The Structure and Interpretation of Computer Programs'
copycats = 'The University of California at Los Angeles'

def first_letter(word):
    return word[0]

def long_word(word):
    return len(word) > 3

def combine(s1, s2):
    return s1 + s2

def square(x):
    return x * x

def to_list(sentence):
    return sentence.split(' ')

def capitalize(word):
  return word.capitalize()

def is_big(n):
    return n > 10

def return_false(n):
    return False

##### Some examples:

####
print(list(map(square, range(10))))

## For our words we need to convert them into a list.
print(list(map(first_letter, to_list(berkeley))))

# Big Numbers
print(list(filter(is_big, range(20))))

# Filter Stuff
print(list(filter(return_false, range(100))))

## Filter Small Words Out
print(list(filter(long_word, to_list(berkeley))))

# map and filter are included by defaut.
# Don't be alarmed by the fact that these are "classes".
# This is an optimization, we'll get to this later.
# print(map)
# print(filter)
# reduce is not included by default. :(
from functools import reduce


# Our own definitions
# Each of these functions is built-in to Python!
# But don't let that stop us from building our own.

# def map(function, sequence):
#     print('Called our custom map')
#     return [ function(item) for item in sequence ]

# def filter(function, sequence):
#     return [ item for item in sequence if function(item) ]

# def reduce(function, sequence):
#     # We need to give our result an inital value.
#     result = function(sequence[0], sequence[1])
#     for index in range(2, len(sequence)):
#       result = function(result, sequence[index])
#     return result


#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################

def acronym(sentence):
    return reduce(combine, map(first_letter, filter(long_word, to_list(sentence))))
