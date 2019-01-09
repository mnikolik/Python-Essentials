#################### All about dictionaries ##############################
##########################################################################
##
##      dict { key : value }
## 
##  dir(dict)
##  help(dict)
##
## Dictionaries are mutable
## Dictionaries are unordered
## Keys must be unique, they can only appear once in dictionary
## Values can be duplicated, they can appear multiple times in dictionary.
## Lists are mutable, so they can NOT be keys in dictionary
## Tuples are immutable, they can be keys in dictionary
##
#########################################################################


# Create dictionary from a list
def list_into_dict(list1):
    '''(list of lists) -> dictionary(key,value)
    Populates dictionary d where each key is the first item
    of each inner list list1 and each value is the second item
    of that inner list.
    >>> list_into_dict([['apple', 3], ['pear', 2], ['banana', 3]])
    {'apple': 3, 'pear': 2, 'banana': 3}
    >>> list_into_dict([[1, 10], [2, 20], [3, 30]])
    {1: 10, 2: 20, 3: 30}
    >>> list_into_dict([[1], [2], [3]])
    IndexError
    '''
    
    d = {}
    for item in list1:
        d[item[0]] = item[1]
    return d






# Create dictionary of chars in word
def count_chars(word):
    '''(str) -> dict of {str: int}
    Return a dictionary d where the keys are the characters
    in word and the values are how many times those characters
    appear in word.
    >>> count_chars('abracadabra')
    {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
    >>> count_chars('AbracadaBrA')
    {'A': 2, 'b': 1, 'r': 2, 'a': 3, 'c': 1, 'd': 1, 'B': 1}
    >>> count_chars('AbracadaBrA1234')
    {'A': 2, 'b': 1, 'r': 2, 'a': 3, 'c': 1, 'd': 1, 'B': 1, '1': 1, '2': 1, '3': 1, '4': 1}
    >>> count_chars('')
    {}
    '''
    
    dictionary = {}   
    for i in word:
        if not (i in dictionary):
            dictionary[i] = 1
        else:
            dictionary[i] = dictionary[i] + 1
    return dictionary






# Display keys and values of dictionary
def print_key_value_dict(dict1):
    '''(dict) -> NoneType
    Print each value and key from dictionary dict1.
    Notation: Keys must be immutable.
    >>> print_key_value_dict({'A1': 10, 'A2': 20})
    A1 10
    A2 20
    >>> print_key_value_dict({10: 'a', 20: 'b'})
    10 'a'
    20 'b'
    >>> print_key_value_dict({(2,2) : 20, (1, 2) : 10})
    (2, 2) 20
    (1, 2) 10
    >>> print_key_value_dict({[2,2] : 20, [1, 2] : 10})
    TypeError
    '''

    for i in dict1:
        print(i, dict1[i])






# Get keys of dictionary
def print_key_dict(dict1):
    '''(dict) -> NoneType
    Print each key of the dictionary dict1.
    Notation: Keys must be immutable.
    >>> print_key_dict({'A1': 10, 'A2': 20})
    A1
    A2
    >>> print_key_dict({10: 'a', 20: 'b'})
    10
    20
    >>> print_key_dict({(2,2) : 20, (1, 2) : 10})
    (2, 2)
    (1, 2)
    >>> print_key_dict({[2,2] : 20, [1, 2] : 10})
    TypeError
    '''

    for i in dict1:
        print(i)






# Print values of dictionary
def print_value_dict(dict1):
    '''(dict) -> NoneType
    Print values of keys of dictionary
    Notation: Values can be mutable.
    >>> print_value_dict({'A1': 10, 'A2': 20})
    10
    20
    >>> print_value_dict({10: 'a', 20: 'b'})
    'a'
    'b'
    >>> print_value_dict({1 : [10, 20], 2 : [30, 40]})
    [10, 20]
    [30, 40]
    >>> print_value_dict({1 : (10, 20), 2 : (30, 40)})
    (10, 20)
    (30, 40)
    '''

    for i in dict1:
        print(dict1[i])







# Change values / Increase values in dictionary
def increment_values(dict1):
    '''(dict) -> NoneType
    Increase each value in dictionary dict1 by 1.
    Notation1: Keys must be immutable.
    Notation2: Values must be numbers.
    >>> increment_values({'A1': 10, 'A2': 20})
    {'A1': 11, 'A2': 21}
    >>> increment_values({10: 'a', 20: 'b'})
    TypeError
    >>> increment_values({1 : [10, 20], 2 : [30, 40]})
    TypeError
    >>> increment_values({1 : (10, 20), 2 : (30, 40)})
    TypeError
    '''

    for i in dict1:
        dict1[i] = dict1[i] + 1

    return dict1







# Contains value in dictionary
def contains(v, dict1):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in d.
    >>> contains('bee', {1: [10, 'bee'], 2: [3.14, 'bear', 100]})
    True
    >>> contains('bee', {'bee': [3.14, 'frog', 100], 2: [10, 10, 10]})
    False
    >>> contains('', {'bee': [3.14, 'frog', 100], 2: [10, 10, 10]})
    False
    '''
    found = False
    for k in dict1:
        for i in range(len(dict1[k])):
            if dict1[k][i] == v:
                found = True
    return found







# Contains keys in dict
def get_keys(L, dict1):
    '''(list, dict) -> list
    Return a new list containing all the items in list L that are keys in d.
    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    ['a', 1]
    >>> get_keys([1, 2, 3], {'a': 1, 'b': 2, 'c': 3})
    []
    >>> get_keys([1, 2, 3], {1: 'a', 2: 'b', 3: 'c'})
    [1, 2, 3]
    >>> get_keys([], {1: 'a', 2: 'b', 3: 'c'})
    []
    >>> get_keys([1, 2, 3], {})
    []
    '''

    result = []
    for k in dict1:
        if k in L:
            result.append(k)

    return result






# Invert dictionary. Keys become values. Values become keys.
def invert_dictionary(dict1):
    '''(dictionary) -> dictionary
    Return a new dictionary where the keys in the new
    dictionary are the values from dict1, and the values
    are lists of the keys associated with those values
    from dict1.
    PRECONDITION: Keys must be unique.
    PRECONDITION: dict1's values must be IMMUTABLE
    >>> invert_dictionary({'cherry': 'red', 'apple': 'red', 'blueberry' : 'blue'})
    red ['cherry', 'apple']
    blue ['blueberry']
    >>> invert_dictionary({1: 'red', 2: 'blue', 3 : 'green', 4: 'red', 5: 'green'})
    red [1, 4]
    blue [2]
    green [3, 5]
    >>> invert_dictionary({'red': 1, 'blue': 1, 'green' : 1, 'yellow': 1, 'pink': 2})
    1 ['red', 'blue', 'green', 'yellow']
    2 ['pink']
    >>> invert_dictionary({'red': 1, 'blue': 2, 'green' : 3, 'red': 4, 'green': 5})
    4 ['red']
    2 ['blue']
    5 ['green']
    >>> invert_dictionary({'red': [1,2], 'blue': 2, 'green' : 3})
    TypeError
    '''

    inverted_d = {}

    for key in dict1:
        value = dict1[key]

        if not (value in inverted_d):
            inverted_d[value] = [key]
        else:
            inverted_d[value].append(key)

    for i in inverted_d:
         print(i, inverted_d[i])








