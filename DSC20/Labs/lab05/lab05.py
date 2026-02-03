"""
DSC 20 Spring 2024, Lab 05
Name: Issac Roy
PID: A17787465
Source: N/A
"""

def identity(x):
    return x

def root(x):
    return round(x ** 0.5, 2)

def squared(x):
    return x ** 2

def cubed(x):
    return x ** 3

# Question 1
def update_candy(candy_dict, func):
    """
    Updates candy quantities in a dictionary by applying func using dictionary
    comprehension.

    Args:
        dict: a dictionary where keys are names (strings) and values are lists
        of integers representing how much candy each person collected.
        func: a function to be applied to each person's candy quantities.

    Returns: new dictionary with updated candy quantities.

    >>> candy_dict = {"pat": [10, 17, 24], "andy": [24, 13, 21]}
    >>> update_candy(candy_dict, squared)
    {'pat': [100, 289, 576], 'andy': [576, 169, 441]}

    >>> candy_dict = {"ryan": [5, 10, 15], "derrick": [6], "deandre": [9, 1]}
    >>> update_candy(candy_dict, identity)
    {'ryan': [5, 10, 15], 'derrick': [6], 'deandre': [9, 1]}
    
    >>> candy_dict = {"pj": [], "amari": [8, 13, 1], "nick": [6, 8, 6]}
    >>> update_candy(candy_dict, lambda x: x + 1)
    {'pj': [], 'amari': [9, 14, 2], 'nick': [7, 9, 7]}
    """
    # YOUR CODE GOES HERE #
    return {key:[func(val) for val in vals] \
        for key, vals in candy_dict.items()}

# Question 2
def candy_sum(candy_dict, func1, func2):
    """
    Finds which friend had the greatest sum of candy after functions are
    applied to the quantities using dictionary comprehension.

    Args:
        dict: a dictionary where keys are names (strings) and values are lists
        of integers representing how much candy each person collected.
        func1: a function to be applied to each person's candy quantities
        func2: a function to be applied to the sum of each person's candy

    Returns: a new dictionary with names and candy sums.

    >>> dict = {"dan": [10, 17, 24], "jay": [100, 21, 5]}
    >>> candy_sum(dict, squared, root)
    {'dan': 31.06, 'jay': 102.3}

    >>> dict = {"sam": [16, 25], "terry": [100, 49]}
    >>> candy_sum(dict, root, identity)
    {'sam': 9.0, 'terry': 17.0}

    >>> dict = {"jalen": [4, 7, 1], "jason": [2, 8, 5, 9, 10]}
    >>> candy_sum(dict, identity, squared)
    {'jalen': 144, 'jason': 1156}
    """
    # YOUR CODE GOES HERE #
    return {key:func2(sum([func1(val) for val in vals])) \
        for key, vals in candy_dict.items()}

# Question 3
def candy_counts(candy_list, rare_candy, common_candy, func1, func2, func3):
    """
    Apply different functions to different candies.

    Args:
        dict: a dictionary where keys are names (strings) and values are lists
        of dictionaries where keys are candy types (strings) and values are 
        the quantity of that candy.
        candy1: a stirng representing a type of candy
        candy2: a string representing a type of candy
        func1: a function to be applied to quantities for candy1
        func2: a function to be applied to quantities for candy2
        func3: a function to be applied to other candy quantities

    Returns: a list containing None and/or sign names which include the 
    substring "laser tag".

    >>> candy_list = [{'kitkat': 4, 'hershey': 3, 'm&m': 2}, \
{'hershey': 1, 'm&m': 4}, {'kitkat': 2, 'butterfinger': 4}, \
{'m&m': 3, 'hershey': 1}]

    >>> rare = 'm&m'
    >>> common = 'hershey'
    >>> candy_counts(candy_list, rare, common, squared, root, cubed)
    [{'kitkat': 64, 'hershey': 1.73, 'm&m': 4}, {'hershey': 1.0, 'm&m': 16}, \
{'kitkat': 8, 'butterfinger': 64}, {'m&m': 9, 'hershey': 1.0}]

    >>> rare = 'butterfinger'
    >>> common = 'kitkat'
    >>> candy_counts(candy_list, rare, common, identity, squared, cubed)
    [{'kitkat': 16, 'hershey': 27, 'm&m': 8}, {'hershey': 1, 'm&m': 64}, \
{'kitkat': 4, 'butterfinger': 4}, {'m&m': 27, 'hershey': 1}]

    >>> rare = 'hershey'
    >>> common = 'm&m'
    >>> candy_counts(candy_list, rare, common, squared, root, identity)
    [{'kitkat': 4, 'hershey': 9, 'm&m': 1.41}, {'hershey': 1, 'm&m': 2.0}, \
{'kitkat': 2, 'butterfinger': 4}, {'m&m': 1.73, 'hershey': 1}]
    """
    # YOUR CODE GOES HERE #
    return [{key:(func1(val) if key == rare_candy else func2(val) \
        if key == common_candy else func3(val)) \
            for key, val in dict.items()} for dict in candy_list]

# Question 4
def costume_rating(costume_color, bling_value):
    """
    Returns a function that calculates the number of candies to return based on
    the costume color, bling value, and phrase length.

    Args:
        costume_color (str): The color of your costume. Must be one of 'blue',
        'red', 'green', 'yellow', 'purple', or 'orange'.
        bling_value (int): Represents how shiny your costume is. Must be a
        positive integer.

    Returns:
        A function that takes in one parameter:
            phrase (str): The phrase said by the trick-or-treater.

    >>> costume_rater = costume_rating('blue', 5)
    >>> costume_rater('19 Character Phrase')
    85
    >>> costume_rater('e')
    0
    >>> costume_rater('seven c')
    1

    >>> costume_rater = costume_rating('orange', 8)
    >>> costume_rater('hello i want candy')
    14

    >>> costume_rater = costume_rating('yellow', 5)
    >>> costume_rater('please give me candy i really need candy')
    0
    """
    # YOUR CODE GOES HERE #
    colors = {'blue': 7, 'red': 3, 'green': 9, \
        'yellow': 0, 'purple': 5, 'orange': 2}
    def inner(phrase):
        return int((colors[costume_color]*bling_value)**(len(phrase)/10)//10)
    return inner

# Question 5
def encoder_generator(key, start_idx, reverse):
    """
    Returns an encoder function that implements encoding based on the provided
    parameters.

    Args:
        key (dict): A dictionary of character pairs that represents a key used
        for character substitution during encoding.
        start_idx (int): The position to start encoding at. Must be greater or
        equal to 0.
        reverse (bool): When True, reverses the encoded text

    Returns:
        A function that takes in one parameter:
            text_input (str): The text input to encode.
            Returns the encoded message

    >>> key = {'e': 'x',\
               'b': 'y'}
    >>> encoder = encoder_generator(key, 1, False)
    >>> encoder('Hello')
    'xllo'
    >>> encoder('arbys')
    'ryys'

    >>> key = {'a': 'b',\
               'b': 'c'}
    >>> encoder = encoder_generator(key, 0, True)
    >>> encoder('black')
    'kcblc'
    """ 
    # YOUR CODE GOES HERE #
    def inner(input):
        return ''.join([key[input[i]] if input[i] in key else input[i] \
            for i in range(start_idx, len(input))])[::reverse*-2+1]
    return inner

# Question 6
def candy_toss(gravity, time, initial_pos):
    """
    Returns two functions that calculate the final position of the candy based
    on the given parameters.

    Args
        gravity (float): The value of gravity on your planet. Must be a
        positive number.
        time (float): The time in the air. Must be a positive number.
        initial_pos (tuple[float, float]): A 2-tuple of numbers representing
        the initial position of the candy in x,y format.

    Returns:
        1st function:
            x_velocity (float): The velocity of the candy in the x direction.
            Returns the final X position of the candy
        2nd function:
            y_velocity (float): The velocity of the candy in the y direction.
            Returns the final Y position of the candy

    >>> x_pos_calc, y_pos_calc = candy_toss(9.8, 5, (0,0))
    >>> x_pos_calc(10)
    50
    >>> y_pos_calc(50)
    127.5
    >>> x_pos_calc, y_pos_calc = candy_toss(1, 7.5, (15,15))
    >>> x_pos_calc(10)
    90.0
    >>> y_pos_calc(0.1)
    -12.38
    """
    # YOUR CODE GOES HERE #
    def find_x(x_velocity):
        return round(initial_pos[0] + x_velocity*time, 2)
    
    def find_y(y_velocity):
        return round(initial_pos[1] + y_velocity*time - 0.5*gravity*time**2, 2)
    return find_x, find_y