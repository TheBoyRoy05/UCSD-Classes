"""
DSC 20 Winter 2024 Homework 09
Name: Issac Roy
PID: A17787465
Source: https://www.programiz.com/python-programming/methods/built-in/ord
"""

# Question 1
def q1_tf_answers():
    """
    Write your answers to the True/False questions in this function.
    True if a method mutates an object and False otherwise.
    """
    # YOUR CODE GOES HERE #
    return [False, True, False, False, True, False, False, True, False, True]

# Question 2
def q2_tf_answers():
    """
    Write your answers to the True/False questions in this function.
    True if the algorithm is in-place and False otherwise.
    """
    # YOUR CODE GOES HERE #
    return [True, False, True, False, False]

# Question 3
def reverse_list(lst):
    """
    Reverses a given list in place

    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1]
    >>> reverse_list(x)
    >>> x
    [1]

    # Add your own doctests below
    >>> x = [[0], [1, 2]]
    >>> reverse_list(x)
    >>> x
    [[1, 2], [0]]
    >>> x = [[0]]
    >>> reverse_list(x)
    >>> x
    [[0]]
    >>> x = [[]]
    >>> reverse_list(x)
    >>> x
    [[]]
    """
    # YOUR CODE GOES HERE #
    if len(lst) <= 1: return
    divide_len_by_2 = 2
    for i in range(len(lst) // divide_len_by_2):
        lst[i], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[i]
    return None

# Question 4
def swap_lists(list_1, list_2):
    """
    Swaps the elements of two lists of the same size in place

    >>> list_1 = [1, 2]
    >>> list_2 = [3, 4]
    >>> swap_lists(list_1, list_2)
    >>> print(list_1)
    [3, 4]
    >>> print(list_2)
    [1, 2]

    >>> list_3 = [4, 2, 6, 8, 90, 45]
    >>> list_4 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list_3, list_4)
    >>> print(list_3)
    [30, 41, 65, 43, 4, 17]
    >>> print(list_4)
    [4, 2, 6, 8, 90, 45]

    # Add your own doctests below
    >>> lst_1 = []
    >>> lst_2 = []
    >>> swap_lists(lst_1, lst_2)
    >>> print(lst_1)
    []
    >>> print(lst_2)
    []
    >>> lst_3 = [0]
    >>> lst_4 = [1]
    >>> swap_lists(lst_3, lst_4)
    >>> print(lst_3)
    [1]
    >>> print(lst_4)
    [0]
    >>> lst_5 = [[0, 1]]
    >>> lst_6 = [[2, 3]]
    >>> swap_lists(lst_5, lst_6)
    >>> print(lst_5)
    [[2, 3]]
    >>> print(lst_6)
    [[0, 1]]
    """
    # YOUR CODE GOES HERE #
    for i in range(len(list_1)):
        list_1[i], list_2[i] = list_2[i], list_1[i]
    return None

# Question 5
def decode_password(hint):
    """
    Takes a list of strings representing a password hint and decodes the hint \
into a list of numbers by mutating the original list

    >>> hint = ["Pythonia", "is", "an", "excellent", "Place"]
    >>> decode_password(hint)
    >>> print(hint)
    [6, 3, 1, 2, 6]

    >>> hint = ["great", "to", "SEE", "U", "!", "Goodbye", "."]
    >>> decode_password(hint)
    >>> print(hint)
    [3, 7, 7, 7, 0, 3, 0]

    # Add your own doctests below
    >>> hint = []
    >>> decode_password(hint)
    >>> print(hint)
    []
    
    >>> hint = ["#", "@", "$", "%"]
    >>> decode_password(hint)
    >>> print(hint)
    [0, 0, 0, 0]
    
    >>> hint = ["Bye", "bye", "Pythonia", "!"]
    >>> decode_password(hint)
    >>> print(hint)
    [1, 1, 6, 0]
    """
    # YOUR CODE GOES HERE #
    letters_per_num = 3
    alpha_start = 94
    for i, word in enumerate(hint):
        if word[0].isalpha():
            hint[i] = (ord(word[0].lower()) - alpha_start) // letters_per_num
        else:
            hint[i] = 0
    return None

# Question 6 (Extra Credit)
def move_non_wishes(seq):
    """
    >>> lst1 = [0, 1, 0, 3, 12]
    >>> move_non_wishes(lst1)
    >>> lst1
    [1, 3, 12, 0, 0]

    >>> lst2 = [0, 0, 0]
    >>> move_non_wishes(lst2)
    >>> lst2
    [0, 0, 0]

    >>> lst3 = []
    >>> move_non_wishes(lst3)
    >>> lst3
    []

    >>> lst4 = [1, 2, 3]
    >>> move_non_wishes(lst4)
    >>> lst4
    [1, 2, 3]
    
    >>> lst5 = [0, 0, 0, 1]
    >>> move_non_wishes(lst5)
    >>> lst5
    [1, 0, 0, 0]
    """
    # YOUR CODE GOES HERE #
    for _ in range(len(seq)):
        for i, v in enumerate(seq):
            if v == 0 and i != len(seq) - 1:
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return None