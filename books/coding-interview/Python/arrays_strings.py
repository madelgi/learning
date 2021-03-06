def all_unique(string):
    """
    Problem 1.1: Implement an algorithm to determine if a string has all
    unique characters
    """
    string_hash = {}
    for i in string:
        if i in string_hash:
            return False
        else:
            string_hash[i] = 1

    return True


def reverse_c_string(c_string):
    """
    Problem 1.2: Reverse a c-style string, where a c-style string is one
    that terminates in a '\0' character.
    """
    return c_string[:-1][::-1] + '\0'


def remove_dups(string):
    """
    Problem 1.3: Write code to remove the duplicate characters in a string
    without using any additional buffer.
    """
    if string is None:
        return string
    str_length = len(string)
    for i in xrange(str_length):
        for j in xrange(i+1, str_length):
            if string[i] == string[j]:
                string


def is_anagram(string1, string2):
    """
    Problem 1.4: Write a method to decide if two strings are anagrams or
    not.
    """
    return sorted(string1) == sorted(string2)


def replace_spaces(string):
    """
    Problem 1.5: Write a method to replace all spaces in a string with
    '%20'.
    """
    def replace(char):
        if char == ' ':
            return '%20'
        else:
            return char

    return ''.join(map(replace, string))


def convert_to_zeros(array):
    """
    Problem 1.7: Write an algorithm such that if an element in an mxn matrix is
    0, the entire row and column is set to zero.
    """


def set_zeros(row, column, array):
    array_copy = list(array)

    array_copy[row] = map(lambda x: 0, array[row])
    for i in range(len(array)):
        array_copy[i][column] = 0

    return array_copy
