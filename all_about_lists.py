############# All about lists ###################
#################################################
##
##
##  dir(list)
##  help(list)
##
##
#################################################



# Print list
def print_list(L):
    ''' (list) -> list
    Return the items of the list
    >>> print_list([1,2,3])
    1
    2
    3
    >>> print_list([[1,2], [2,3], [3,4]])
    [1,2]
    [2,3]
    [3,4]
    >>> print_list([])
    
    '''
    
    for i in range(0, len(L)):
        print(L[i])

    



# Populating a list by prompt.
def populate_list(prompt):
    '''(str) -> str
    Use prompt to ask the user for a "item".
    Add the items into a list.
    Return list of items. 
    >>> populate_list('Enter one more item. (type return to end): ')
    Enter one more item. (type return to end): blue
    Enter one more item. (type return to end): yellow
    Enter one more item. (type return to end): red
    Enter one more item. (type return to end):
    ['blue', 'yellow', 'red']
    >>> populate_list('Enter one more item. (type return to end): ')
    Enter one more item. (type return to end): 1
    Enter one more item. (type return to end): 2
    Enter one more item. (type return to end): 3
    Enter one more item. (type return to end):
    ['1', '2', '3']
    >>> populate_list('Enter one more item. (type return to end): ')
    Enter one more item. (type return to end):[1]
    Enter one more item. (type return to end):[2]
    Enter one more item. (type return to end):[3]
    Enter one more item. (type return to end):
    ['[1]', '[2]', '[3]']
    '''

    populate_list = []
    prompt = "Enter one more item. (type return to end):"

    item = input(prompt)

    while item != '':
        populate_list.append(item)
        item = input(prompt)

    return populate_list






# Increase values of items in list
def increment_items(L, increment):
    '''(list of numbers, int) -> list
    Returns list of same number of items,
    increased by rate - increment.
    >>> increment_items([1, 2, 3], 2)
    [3, 4, 5]
    >>> increment_items(['a', 'b', 'c'], 'a')
    ['aa', 'ba', 'ca']
    >>> increment_items(['c', 2, 'a'], 0)
    TypeError
    '''

    i = 0
    
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

    return L






# Compressing a list by pairing items.
def compress_list(L):
    ''' (list of str) -> list of str
    Return a new list with adjacent PAIRS of string elements
    from L concatenated together, starting with indices 0 and 1,
    2 and 3,and so on.
    Precondition: len(L) >= 2 and len(L) % 2 == 0
    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    >>> compress_list(['a', 'b', 'c', 'd', 'e'])
    The list contains odd number of items, it cannot be divided into pairs
    >>> compress_list([1, 2, 3, 4])
    [3, 7]
    >>> compress_list([1, 'a', 3, 'a'])
    TypeError
    '''
    
    compressed_list = []
    i = 0

    if len(L) % 2 == 0:
        while i < len(L):
            compressed_list.append(L[i] + L[i + 1])
            i = i + 2

        return compressed_list

    else:
        print('The list contains odd number of items,it cannot be divided into pairs')





# Gather every n-th element of list
def gather_every_nth(L, n):
    '''(list, int) -> list
    Return a new list containing every n'th element in list L,
    starting at index 0.
    Precondition: n >= 1
    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)
    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 0)
    The index value n is not >= 1. 
    '''
    
    if n >= 1:
        result = []
        i = 0
        while i < len(L):
            result.append(L[i])
            i = i + n
        return result
    else:
        print('The index value n is not >= 1. ')






# List of num and list of str
def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool
    Return True if and only if all the ints in L1
    are the lengths of the strings in L2
    at the corresponding positions.
    Precondition: len(L1) == len(L2)
    >>> are_lengths_of_strs([3, 0, 4], ['abc', '', 'wxyz'])
    True
    >>> are_lengths_of_strs([0, 0, 0], ['', '', ''])
    True
    >>> are_lengths_of_strs([0, 3, 0], ['123', 'abc', 'ppp'])
    False
    >>> are_lengths_of_strs([0, 3, 'a'], ['123', 'abc', 'ppp'])
    False
    '''

    if len(L1) == len(L2):
        result = True
        for i in range(len(L1)):
            if L1[i] != len(L2[i]):
                result = False
        return result
    else:
        print('Number of items in L1 do not match number of items in L2.')





# Merging a list of numbers by factor 3.
def merge(L):
    '''(list of numbers, int) -> list of numbers
    Return a list of numbers, that are merged
    from the initial list, by 3.
    Precondition: len(L) >= n and len(L) % n = 0
    >>> merge([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [6, 15, 24]
    >>> merge(['a', 'b', 'c'])
    ['abc']
    >>> merge([1, 2, 3, 4, 5])
    The list can not be merged by 3 items.
    >>> merge(['a', 'b', 'c', 1, 2, 3])
    ['abc', 6]
    >>> merge(['a', 1, 'b', 2, 'c', 3])
    TypeError
    '''
    
    merged = []

    if len(L) >= 3:
        if len(L) % 3 == 0:
            for i in range(0, len(L), 3):
                merged.append(L[i] + L[i+1] + L[i+2])
            return merged

        else:
            print('The list can not be merged by 3 items.')
    else:
        print('The list has less than 3 items')






# Shifting items in list to the left.
def shift_left(L):
    ''' (list) -> NoneType
    Shift each item in L one position to the left
    and shift the first item to the last position.
    Precondition: len(L) >= 1
    >>> shift_left([1, 2, 3, 4, 5])
    [2, 3, 4, 5, 1]
    >>> shift_left(['a', 'b', 'c', 1, 2])
    ['b', 'c', 1, 2, 'a']
    >>> shift_left([])
    The list is empty
    '''

    if len(L) >= 1:
        first_item = L[0]

        for i in range(1, len(L)):
            L[i-1] = L[i]
        L[-1] = first_item
        print(L)
    else:
        print('The list is empty')







# Shifting items in list to the right. 
def shift_right(L):
    ''' (list) -> NoneType
    Shift each item in L one position to the rightand shift
    the last item to the first position.
    Precondition: len(L) >= 1
    >>> shift_right([1, 2, 3, 4, 5])
    [5, 1, 2, 3, 4]
    >>> shift_right(['a', 'b', 'c', 1, 2])
    [2, 'a', 'b', 'c', 1]
    >>> shift_right([])
    The list is empty
    '''

    if len(L) >= 1:
        last_item = L[-1]

        for i in range(1, len(L)):
            L[len(L) - i] = L[len(L) - i - 1]
        L[0] = last_item
        print(L)
    else:
        print('The list is empty')





def sum_items(list1, list2):
    ''' (list of num/str, list of num/str) -> list of num/str
    Return a new list in which each item is the sum of the
    items at the corresponding position of list1 and list 2.
    Precondition1: ValueType(list1) = ValueType(list2)
    Precodnition2: len(list1) == len(list2)
    >>> sum_items([1, 2, 3], [2, 4, 2])
    [3,6,5]
    >>> sum_items(['a', 'b', 'c'], ['a', 'b', 'c'])
    ['aa', 'bb', 'cc']
    >>> sum_items([1, 2, 3], ['a', 'b', 'c'])
    TypeError
    >>> sum_items([[1, 2], [1, 2]], [[5, 5], [10, 10]])
    [[1, 2, 5, 5], [1, 2, 10, 10]]
    '''

    if len(list1) == len(list2):
        sum_list = []
        for i in range(len(list1)):
            sum_list.append(list1[i] +list2[i])
        return sum_list
    else:
        print('The lists do not have same number of items.')





# Average of sublists in a list.
def averages(numbers):
    '''(list of list of number) -> list of float
    Return a new list in which each item is the average
    of the items in the inner list at the corresponding
    position of items.
    >>> averages([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    [20.0, 50.0, 80.0]
    >>> averages([[10, 20], [40, 50, 60], [70]])
    [15.0, 50.0, 70.0]
    >>> averages([[10, 20], [40, 50, 60], ['a']])
    TypeError
    >>> 
    '''

    averages = []

    for numbers_list in numbers:
        total = 0
        for mark in numbers_list:
            total = total + mark
        averages.append(total / len(numbers_list))

    return averages


    



# Check if list is reverse to itself.
def reverse_list(s):
    ''' (num/str) -> bool
    Return True if and only if list s is equal to
    reverse of list s. The parameters can be numbers
    and/or strings.
    >>> reverse_list([1,2,3,2,1])
    True
    >>> reverse_list([1,2,3,4,5])
    False
    >>> reverse_list(['a', 'b', 'a'])
    True
    >>> reverse_list(['a', 'b', 1, 'b', 'a'])
    True
    '''
    
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)






# Limit repetition of word occurences in a list of str
def word_in_list_repetition(L, word):
    '''(list of str, str) -> NoneType
    Make sure there are no more than 3 occurrences
    of word in list of words.
    Precondition: len(L) > 0
    >>> word_in_list_repetition(['apple', 'banana', 'apple', 'banana', 'apple', 'apple'], 'apple')
    ['banana', 'apple', 'banana', 'apple', 'apple']
    >>> word_in_list_repetition(['apple', 'banana', 'apple', 'banana', 'apple', 'apple'], 'banana')
    ['apple', 'banana', 'apple', 'banana', 'apple', 'apple']
    >>> word_in_list_repetition(['apple', 'banana', 'apple', 'banana', 'apple', 'apple'], 'xyz')
    The word has not been found in this list
    '''
    
    if len(L) > 0:
        for item in L:
            if item.find(word) != -1:
                while L.count(word) > 3:
                    L.pop(L.index(word))
                return L
            else:
                print('The word has not been found in this list')
    else:
        print('The list is empty')





# Extract elements of lists in list
def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)
    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.
    >>> get_diagonal_and_non_diagonal([[1,  2,  3], [4,  5,  6], [7,  8,  9]])
    ([1, 5, 9], [2, 3, 4, 6, 7, 8])
    >>> get_diagonal_and_non_diagonal([[1, 2], [3, 4]])
    ([1, 4], [2, 3])
    >>> get_diagonal_and_non_diagonal([[1]])
    ([1], [])
    >>> get_diagonal_and_non_diagonal([[]])
    IndexError
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):
            if row == col:
                diagonal.append(L[row][col])
            else:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)
