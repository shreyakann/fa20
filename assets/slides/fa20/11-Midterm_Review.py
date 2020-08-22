# Fall 2018 Midterm
# This relies on "string slicing", something we haven't talked about this year.
# s[0] is the first item
# s[1:] is the second item until the end
# s[start:end:step] to slice items. End is exclusive.

def match(a, b):
    """Detect a match (a==b). Return 1 on match, otherwise 0
    >>> match("a", "a")
    1
    >>> match("a", "b")
    0
    """
    if a == b:
        return 1
    else:
        return 0

def count_letter(s, c):
    """ Returns the number of times that character c occurs in string s
    >>> count_letter("banana", "a")
    3
    >>> count_letter("banana", "z")
    0
    """
    pass

def count_letter_r(s, c):
    """ Returns the number of times that character c occurs in string s
    >>> count_letter_r("banana", "a")
    3
    >>> count_letter_r("banana", "z")
    0
    """

def match_maker(c):
    """
    >>> func = match_maker("c")
    >>> func("abc")
    1
    >>> func("def")
    0
    """
    return

def count_letter_hof(s, c):
    """ Returns the number of times that character c occurs in string s
    >>> count_letter_hof("banana", "a")
    3
    >>> count_letter_hof("banana", "z")
    0
    """
    return

def factorial(n):
    """
    >>> factorial(0)
    1
    >>> factorial(4)
    24
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
