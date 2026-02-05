"""
DSC 20 Winter 2024 Lab 01
Name: Issac Roy
PID: A17787465
Source: https://www.w3schools.com/python/ref_string_split.asp, 
https://www.w3schools.com/python/ref_list_count.asp

****************************** Example ******************************
DSC 20 Winter 2024 Lab 01
Name: Marina Langlois
PID: A12345678
Source: Lecture 1 Slides, https://www.w3schools.com/python/ref_string_join.asp
"""
# Question 1
def direction(choice):
    """
    Outputs a direction messsage according to the input integer value.

    Args:
        choice: an integer that is used to determine the output message.

    Returns:
        'going east' if choice is positive and even;
        'going south' if choice is negative and even;
        'going west' if choice is positive and odd;
        'going north' if choice is negative and odd;
        'staying' otherwise.

    >>> direction(10)
    'going east'
    >>> direction(-10)
    'going south'
    >>> direction(5)
    'going west'
    >>> direction(-7)
    'going north'
    >>> direction(0)
    'staying'
    """
    result = 'going '
    
    if choice == 0: return 'staying'
    elif choice > 0 and choice%2 == 0: result += 'east'
    elif choice < 0 and choice%2 == 0: result += 'south'
    elif choice > 0 and choice%2 == 1: result += 'west'
    elif choice < 0 and choice%2 == 1: result += 'north'
    
    return result
# Question 2
def steps(lst, target):
    """
    Outputs the number of occurrences of the target in a given list.

    Args:
        lst: a list of positive integers.
        target: a positive integer to be counted.

    Returns:
        the number of occurrences of the integer in the input list.

    >>> steps([1, 2, 3], 2)
    1
    >>> steps([1, 2, 1, 3, 1, 4], 1)
    3
    >>> steps([1, 2, 1], 1)
    2
    """
    return lst.count(target)

# Question 3
def same_ends(lst):
    """
    Checks whether the first and the last elements in the list are the same.

    Args:
        lst: a non-empty list that

    Returns:
        True/False boolean regarding whether the first element in the list is the
        same as the last element.

    >>> same_ends([1, 3, 1])
    True
    >>> same_ends([4, 7, 4.0])
    True
    >>> same_ends([1, 5, 4, 5])
    False
    >>> same_ends([1])
    True
    >>> same_ends(["search", "search", "Search"])
    False
    """
    return lst[0] == lst[-1]

# Question 4
def quantity_of_same_ends(lsts):
    """
    Iterate through a list of non-empty lists and count how many lists inside that
    have the same first and last elements.

    Args:
        lsts: a list of non-empty lists

    Returns:
        the number of lists that have the same first and last elements.

    >>> quantity_of_same_ends([[1, 3, 1],[1, 3, 12]])
    1
    >>> quantity_of_same_ends([[1, 3, 1],[4, 7, 4.0]])
    2
    >>> quantity_of_same_ends([[1, 3, 1],[4, 7, 4.0], [1], [3,4]])
    3
    """
    return sum([lst[0] == lst[-1] for lst in lsts])

# Question 5
def message(name, choice):
    """
    Outputs a message to friend according to the input integer.

    Args:
        name: friend's name, possibly empty.
        choice: an integer that is used to determine the output message.

    Returns:
        a message to friend according to the input name and integer.

    >>> message("Marina", 5)
    'Dear Marina, I am going west.'
    >>> message("Anna", -5)
    'Dear Anna, I am going north.'
    >>> message("Rain", 0)
    'Dear Rain, I am staying.'
    """
    return f'Dear {name}, I am {direction(choice)}.'


# Question 6
def steps_unfold(steps):
    """
    Outputs a list of integers from 1 up to steps.

    Args:
        steps: a non-negative integer.

    Returns:
        a list of integers from 1 up to steps.

    >>> steps_unfold(5)
    [1, 2, 3, 4, 5]
    >>> steps_unfold(1)
    [1]
    >>> steps_unfold(0)
    []
    """
    return [i+1 for i in range(steps)]

# Question 7
def message_to_all(names, choice):
    """
    Outputs a list of strings with messages to friends.

    Args:
        names: a list of friend names
        choice: an integer that is used to determine the output message.

    Returns:
        a list of strings with messages to friends;
        empty list if names list is empty.

    >>> names = ["Marina", "Ben", "Bryce"]
    >>> message_to_all(names, 5)
    ['Dear Marina, I am going west.', \
'Dear Ben, I am going west.', \
'Dear Bryce, I am going west.']

    >>> names = ["Anastasya", "Teresa"]
    >>> message_to_all(names, 0)
    ['Dear Anastasya, I am staying.', \
'Dear Teresa, I am staying.']

    >>> names = []
    >>> message_to_all(names, 314)
    []
    """
    return [message(name, choice) for name in names]

# Question 8.1
def combine_words_no_separator(words):
    """
    Concatenates words in the input list without separator in between.

    Args:
        words: a list of words to be concatenated

    Returns:
        a string with all words in the input list joined together.

    >>> combine_words_no_separator(["Very", "close"])
    'Veryclose'
    >>> combine_words_no_separator(["What", "is", "your", "name?"])
    'Whatisyourname?'
    >>> combine_words_no_separator(["We", "need", "to",  "talk"])
    'Weneedtotalk'
    """
    res = ''
    for word in words:
        res += word
    return res

# Question 8.2
def combine_words_with_separator(words, separator):
    """
    Concatenates words in the input list with the given separator.

    Args:
        words: a list of words to be concatenated
        separator: a (sequence) of characters to be used to separate words

    Returns:
        a string with all words in the input list joined together by the given separator.

    >>> combine_words_with_separator(["Very", "close"], "***")
    'Very***close'
    >>> combine_words_with_separator(["No", "need", "to", "go"], "-")
    'No-need-to-go'
    >>> combine_words_with_separator(["Find", "another", "message"], " ")
    'Find another message'
    """
    res = ''
    for word in words:
        res += separator + word
    return res[len(separator):]

# Question 9
def getting_hint(message):
    """
    Outputs the sum of the lengths of the first and last words in the input string.
    Return 0 if string is empty.

    Args:
        message: a string containing message pinned on the tree

    Returns:
        a number representing the sum of the first and the last words in the message.

    >>> getting_hint("Run away from here")
    7
    >>> getting_hint("DANGER!!")
    16
    >>> getting_hint("")
    0
    >>> getting_hint("number of steps")
    11
    """
    if len(message) == 0:
        return 0
    else:
        return len(message.split()[0]) + len(message.split()[-1])

# Question 10
def digging(steps_left, steps_forward,  message):
    """
    Compares the sum of steps moving left and moving forward to the sum of length
    to the first and the last words in the input message. Outputs a message according
    to the comparison result.

    Args:
        steps_left: the number of steps to move left, represented as a string.
        steps_forward: the number of steps to move forward, represented as a string.
        message: the message pinned on the tree, represented as a string.

    Returns:
        a message according to the numerical comparison between the sum of length of
        the first and the last words in the message and the sum of steps to move.
 
    >>> digging("5", "6", "no dig")
    'Too far'
    >>> digging("1", "4", "run away now!")
    'Too close'
    >>> digging("1", "8", "right here")
    'Dig here!'
    """
    diff = int(steps_forward) + int(steps_left) - getting_hint(message)
    return 'Dig here!' if diff == 0 else 'Too far' if diff > 0 else 'Too close'