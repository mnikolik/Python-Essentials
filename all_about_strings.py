# Operations with strings
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
    '''

    return word1.find(word2) >= 0







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







# The following are operations with sequences
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






