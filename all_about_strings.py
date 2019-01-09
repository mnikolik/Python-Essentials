################## All about strings ####################
#########################################################
##
## dir(str)
## help(str)
##
## 
##########################################################



### Operations on one string
def print_string(word):
    '''(str) -> str
    Return the string, character by character in a row
    >>> print_string('abc')
    a
    b
    c
    >>> print_string('Hello')
    H
    e
    l
    l
    o
    >>> print_string('')
    ''
    '''
    for char in word:
        print(char)
        return(char)





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







def has_vowel(word):
    '''(str) -> bool
    Return True if and only if there is at least one vowel
    in word, not including y.
    >>> has_vowel('Hello')
    True
    >>> has_vowel('sqrt')
    False
    >>> has_vowel('gym')
    False
    '''
    
    vowel_found = False
    for char in word:
        if char in 'aeiouAEIOU':  
           vowel_found = True

    return vowel_found





def collect_vowels(word):
    ''' (str) -> str
    Return the vowels from word.
    Do not treat the letter y as a vowel.
    >>> collect_vowels('Hello')
    'eo'
    >>> collect_vowels('sqrt')
    ''
    >>> collect_vowels('gym')
    ''
    '''

    vowels = ''

    for char in word:
        if char in 'aeiouAEIOU':
            vowels = vowels + char

    return vowels





def print_vowels(word):
    ''' (str) -> str
    Return the vowels from the word,
    character by character in a row.
    Do not treat the letetr y as a vowel.
    >>> print_vowels('Hello')
    e
    o
    >>> print_vowels('sqrt')
    
    >>> print_vowels('gym')
    
    '''
    for char in word:
        if char in 'aeiouAEIOU':
            print(char)





def count_vowels(word):   
    ''' (str) -> str
    Return the number of vowels in word.
    Do not treat the letter y as a vowel.
    >>> count_vowels('Hello')
    2
    >>> count_vowels('sqrt')
    0
    >>> count_vowels('gym')
    0
    '''

    num_vowels = 0

    for char in word:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    return num_vowels





def get_length(word):
    ''' (str) -> int
    Return the length of the word, which is
    total number of characters.
    >>> get_length('Hello')
    5
    >>> get_length('Hello world!')
    12
    >>> get_length('')
    0
    '''

    return len(word)






def count_adjacent_repeats(word):
    '''(str) -> int
    Return the number of occurences of a character
    and an adjacent character being the same
    in the given word.
    >>> count_adjacent_repeats('abccdeffggh')
    3
    >>> count_adjacent_repeats('Hello')
    1
    >>> count_adjacent_repeats('abc')
    0
    >>> count_adjacent_repeats('')
    0
    '''

    repeats = 0

    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            repeats = repeats + 1


    return repeats






def count_char_in_word(word, char):
    '''(str, str) -> int
    Return the number of occurences of char in word.
    >>> count_char_in_word('Hello', 'e')
    1
    >>> count_char_in_word('Hello', 'l')
    2
    >>> count_char_in_word('Hello', 'x')
    0
    >>> count_char_in_word('Hello', '')
    6
    '''

    return word.count(char)






### Operations on two strings
def is_longer(word1, word2):
    ''' (str, str) -> bool
    Return True if and only if word1 is longer than word2.
    >>> is_longer('Hello', 'yes')
    True
    >>> is_longer('Hello', 'world')
    False
    >>> is_longer('Hello', 'Hello world!')
    False
    '''

    return get_length(word1) > get_length(word2)






def common_chars(word1, word2):
    '''(str, str) -> str
    Return a new string containing all characters
    from word1 that appear at least once in word2.
    The characters in the result will appear in
    the same order as they appear in word1.
    >>> common_chars('abcd', 'af')
    'a'
    >>> common_chars('a', 'a')
    'a' 
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    >>> common_chars('abc', 'xyz')
    ''
    '''

    common = ''

    for char in word1:
        if char in word2:
            common = common + char

    return common






def count_matches(word1, word2):
    '''(str, str) -> int
    Return the number of positions in word1 that contain
    the same character at the corresponding position
    of word2.
    Precodnition: len(word1) == len(word2)
    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    2
    >>> count_matches('ate', 'tea')
    0
    >>> count_matches('', '')
    ''
    '''

    num_matches = 0

    for i in range(len(word1)):
        if word1[i] == word2[i]:
            num_matches = num_matches + 1

    return num_matches







def contain_word2_in_word1(word1, word2):
    '''(str, str) -> bool
    Return True if and only if word2 occurs in word1.
    Notation: It's case sensitive.
    >>> contain_word2_in_word1('Hello', 'Hell')
    True
    >>> contain_word2_in_word1('Hello', 'hell')
    False
    >>> contain_word2_in_word1('Hello', 'oll')
    False
    >>> contain_word2_in_word1('Hello', '')
    True
    '''

    return word1.find(word2) >= 0






def both_start_with(word1, word2, prefix):
    '''(str, str, str) -> bool
    Return True if and only if word1 and word2 both start
    with the same letter in prefix.
    >>> both_start_with('abc', 'antenna', 'a')
    True
    >>> both_start_with('abc', 'antenna', 'b')
    False
    >>> both_start_with('abc', 'banana', 'b')
    False
    >>> both_start_with('abc', 'antenna', 1)
    TypeError
    '''

    return word1.startswith(prefix) and word2.startswith(prefix)








### Operations with strings in list

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







def is_valid_word(wordlist, word):
    ''' (list of str, str) -> bool
    Return True if and only if word is an element of wordlist.
    >>> is_valid_word(['CAT', 'PET', 'BIRD', 'MOUSE'], 'PET')
    True
    >>> is_valid_word(['CAT', 'PET', 'BIRD', 'MOUSE'], 'PAT')
    False
    >>> is_valid_word(['CAT', 'PET', 'BIRD', 'MOUSE'], '')
    False
    '''

    found = False
    
    for i in range(len(wordlist)):
        if wordlist[i] == word:
            found= True

    return found








### Operations with strings in board.

def make_str_from_row(board, row_index):
    ''' (list of list of str, int) -> str
    Return the characters from the row of the board with index row_index
    as a single string.
    >>> make_str_from_row([['C', 'A', 'T'], ['P', 'E', 'T']], 0)
    'CAT'
    >>> make_str_from_row([['C', 'A', 'T'], ['P', 'E', 'T']], 1)
    'PET'
    >>> make_str_from_row([['C', 'A', 'T'], ['P', 'E', 'T']], 2)
    IndexError
    '''

    single_row = ''

    for char in board[row_index]:
        single_row = single_row + char
    
    return single_row







def make_str_from_column(board, column_index):
    ''' (list of list of str, int) -> str
    Return the characters from the column of the board with index column_index
    as a single string.
    >>> make_str_from_column([['C', 'A', 'T'], ['P', 'E', 'T']], 0)
    'CP'
    >>> make_str_from_column([['C', 'A', 'T'], ['P', 'E', 'T']], 1)
    'AE'
    >>> make_str_from_column([['C', 'A', 'T'], ['P', 'E', 'T']], 2)
    'TT'
    >>> make_str_from_column([['C', 'A', 'T'], ['P', 'E', 'T']], 3)
    IndexError
    '''

    single_column = ''

    for char in board:
        single_column = single_column + (char[column_index])

    return single_column







def board_contains_word_in_row(board, word):
    ''' (list of list of str, str) -> bool
    Return True if and only if one or more of the rows of the board
    contains word.
    Precondition: board has at least one row and one column,
    and word is a valid word.
    >>> board_contains_word_in_row([['C', 'A', 'T'], ['P', 'E', 'T']], 'CA')
    True
    >>> board_contains_word_in_row([['C', 'A', 'T'], ['P', 'E', 'T']], 'AC')
    False
    >>> board_contains_word_in_row([['C', 'A', 'T'], ['P', 'E', 'T']], '')
    True
    '''

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False







def board_contains_word_in_column(board, word):
    ''' (list of list of str, str) -> bool
    Return True if and only if one or more of the columns of the board
    contains word.
    Precondition: board has at least one row and one column, and word is a
    valid word.
    >>> board_contains_word_in_column([['C', 'A', 'T'], ['P', 'E', 'T']], 'CP')
    True
    >>> board_contains_word_in_column([['C', 'A', 'T'], ['P', 'E', 'T']], 'CA')
    False
    >>> board_contains_word_in_column([['C', 'A', 'T'], ['P', 'E', 'T']], '')
    True
    '''

    i = 0
    while i < len(board[0]):
        if word in make_str_from_column(board, i):
            return True
        i = i + 1

    return False






def board_contains_word(board, word):
    '''(list of list of str, str) -> bool
    Return True if and only if word appears in board.
    Precondition: board has at least one row and one column.
    >>> board_contains_word([['C', 'A', 'T'], ['P', 'E', 'T']], 'CP')
    True
    >>> board_contains_word([['C', 'A', 'T'], ['P', 'E', 'T']], 'CAT')
    True
    >>> board_contains_word([['C', 'A', 'T'], ['P', 'E', 'T']], '')
    True
    '''

    word_in_row = board_contains_word_in_row(board, word)
    word_in_column = board_contains_word_in_column(board, word)

    if word_in_row or word_in_column:
        return True
    return False
    





### The following are operations with sequences
# The model sequence in the functions below
# is DNA sequence.
# The DNA sequence contains nucleotides named as
# 'A', 'T', 'C' and 'G'.
# Nucleotides have complements among each other.
# Complement of 'A' is 'T' and vice versa.
# Complement of 'C' is 'G' and vice versa.


def is_valid_sequence(word):
    ''' (str) -> bool
    Return True if and only if the word sequence is valid,
    that is, it contains no characters other than 'A', 'T', 'C' and 'G'.
    Notation: It's a DNA sequence.
    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('ATCGX')
    False
    >>> is_valid_sequence('PQRST')
    False
    '''

    is_valid = 0

    for char in word:
        if char not in 'ATCG':
            is_valid = is_valid + 1

    return is_valid <= 0






def insert_sequence(seq1, seq2, index):
    ''' (str, str, int) -> str
    Return a DNA sequence obtained by inserting
    the second DNA sequence given by seq2 
    into the first DNA sequence given by seq1,
    at the given index.
    Precondition: index <= len(dna_seq1)
    >>> insert_sequence('AATT', 'CG', 2)
    'AACGTT'
    >>> insert_sequence('GTCA', 'AA', 4)
    'GTCAAA'
    >>> insert_sequence('GTCA', '', 2)
    'GTCA'
    >>> insert_sequence('', '', 0)
    ''
    '''

    if is_valid_sequence(seq1):
        if is_valid_sequence(seq2):
            if index <= len(seq1):
                new_sequence = seq1[:index] + seq2[:] + seq1[index:]
                return new_sequence
            elif index > len(seq1):
                print('The index must be  <= length of first sequence')

    else:
        print('The arguments are not valid')






def get_complement(nucleotide):
    ''' (str) -> str
    Return the nucleotide's complement
    The first parameter is a nucleotide ('A', 'T', 'C' or 'G').
    Complement of 'A' is 'T' and vice versa.
    COmplement of 'C' is 'G' and vice versa.
    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('X')
    'The nucleotide is not valid.'
    >>> get_complement('a')
    'The nucleotide is not valid.'
    '''

    complement = ''

    if is_valid_sequence(nucleotide):
        if nucleotide in 'A':
            complement = 'T'
        elif nucleotide in 'T':
            complement = 'A'
        elif nucleotide in 'C':
            complement = 'G'
        elif nucleotide  in 'G':
            complement = 'C'

        return complement

    else:
        print('The nucleotide is not valid')
        




def get_complementary_sequence(dna_seq):
    '''(str) -> str
    Return the DNA sequence that is complementary
    to the given DNA sequence -> dna_seq.
    >>> get_complementary_sequence('ATCG')
    'TAGC'
    >>> get_complementary_sequence('TTTTTTT')
    'AAAAAAA'
    >>> get_complementary_sequence('ABCD')
    'The dna sequence is not valid.'
    >>> get_complementary_sequence('')
    ''
    '''

    complement_sequence = ''

    if is_valid_sequence(dna_seq):
        for char in dna_seq:
            complement_sequence = complement_sequence + get_complement(char)

        return complement_sequence

    else:
        print('The dna sequence is not valid')






