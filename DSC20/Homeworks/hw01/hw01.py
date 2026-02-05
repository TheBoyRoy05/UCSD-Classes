"""
DSC 20 Winter 2024 Homework 01
Name: Issac Roy
PID: A17787465
Source: https://www.w3schools.com/python/ref_string_split.asp,
https://www.w3schools.com/python/ref_keyword_assert.asp
"""
# Question 1.1
def helper_distance(coord1, coord2):
    """
    Outputs the distance of two input coordinates

    >>> helper_distance(['1', '2'], ['4', '6'])
    5.0
    >>> round(helper_distance(['3', '2'], ['40', '6']), 3)
    37.216

    # Add your own doctests below
    >>> helper_distance(['0', '0'], ['0', '0'])
    0.0
    >>> helper_distance(['-1000', '0'], ['1000', '0'])
    2000.0
    >>> round(helper_distance(['-1', '-1'], ['-2', '-2']), 3)
    1.414
    """
    # YOUR CODE GOES HERE #
    x1, x2 = float(coord1[0]), float(coord2[0])
    y1, y2 = float(coord1[1]), float(coord2[1])
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

# Question 1.2
def safe_location(your_loc, safe_loc, jump_length):
    """
    Determines whether a jump length can take you to a safe location
    
    Args:
        your_loc: your location coords seperated by a comma and space (string)
        safe_loc: safe location coords spereated by a comma and space (string)
        jump_length: a non-negative number for how far you jump (float/int)

    >>> your_loc = "1, 2"
    >>> safe_loc = "4, 6"
    >>> ans = safe_location(your_loc, safe_loc, 10)
    >>> print(ans)
    Nice jump!
    You are safe to continue.

    >>> your_loc = "3, 2"
    >>> safe_loc = "40, 6"
    >>> safe_location(your_loc, safe_loc, 15)
    'You are sent back home.'
    
    # Add your own doctests below
    >>> safe_location("203, 201", "5, 0", -10)
    Traceback (most recent call last):
    ...
    AssertionError: Jump length must be non-negative
    
    >>> ans = safe_location("0, 0", "0, 0", 0)
    >>> print(ans)
    Nice jump!
    You are safe to continue.
    
    >>> safe_location("0, 1000", "1000, 0", 1000)
    'You are sent back home.'
    
    >>> safe_location("0, 1.5", "1, 0", 1.5)
    'You are sent back home.'
    """
    # YOUR CODE GOES HERE #
    assert jump_length >= 0, "Jump length must be non-negative"
    your_coords = your_loc.split(', ')
    safe_coords = safe_loc.split(', ')
    distance = helper_distance(your_coords, safe_coords)
    if jump_length >= distance:
        return "Nice jump!\nYou are safe to continue."
    else:
        return "You are sent back home."

# Question 2.1
def first_pattern(repeat, symbol):
    """
    Returns a string of symbol duplicated repeat amount of times

    >>> first_pattern(3, '*')
    '***'
    >>> first_pattern(6, '$')
    '$$$$$$'

    # Add your own doctests below
    >>> first_pattern(0, '>')
    ''
    >>> first_pattern(-2, '?')
    Traceback (most recent call last):
    ...
    AssertionError: repeat must be non-negative
    >>> first_pattern(50, '!')
    '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    """
    # YOUR CODE GOES HERE #
    assert repeat >= 0, "repeat must be non-negative"
    return symbol * repeat

# Question 2.2
def second_pattern(repeat, symbol, word, repeat_again):
    """
    Returns word samdwiched in between repeat amount of symbols and
    repeat_again amount of symbols, all in reverse

    >>> second_pattern(3, '*', 'pattern', 2)
    '**nrettap***'
    >>> second_pattern(6, '$', 'journey', 3)
    '$$$yenruoj$$$$$$'
    >>> second_pattern(3, '', '', 2)
    ''

    # Add your own doctests below
    >>> second_pattern(3, '>', 'epba', -1)
    Traceback (most recent call last):
    ...
    AssertionError: repeats must be positive
    >>> second_pattern(20, '!', 'nohtyp', 20)
    '!!!!!!!!!!!!!!!!!!!!python!!!!!!!!!!!!!!!!!!!!'
    >>> second_pattern(1, '!', 'zyxwvutsrqponmlkjihgfedcba', 1)
    '!abcdefghijklmnopqrstuvwxyz!'
    """
    # YOUR CODE GOES HERE #
    assert repeat > 0 and repeat_again > 0, "repeats must be positive"
    return (symbol * repeat + word + symbol * repeat_again)[::-1]

# Question 2.3
def third_pattern(word, switch):
    """
    Triples the word and capitilizes the second copy if switch is false
    and capitilizes the first and third copy if switch is true

    >>> third_pattern("trip", True)
    'TRIPtripTRIP'
    >>> third_pattern("dangerous", False)
    'dangerousDANGEROUSdangerous'

    # Add your own doctests below
    >>> third_pattern("", False)
    ''
    >>> third_pattern("SpoOkIe", True)
    'SPOOKIEspookieSPOOKIE'
    >>> third_pattern("He", False)
    'heHEhe'
    """
    # YOUR CODE GOES HERE #
    upper = word.upper()
    lower = word.lower()
    return upper + lower + upper if switch else lower + upper + lower
    
# Question 2.4
def fourth_pattern(symbols, repeats, switch):
    # The variable name is counterintuitive here
    # You would think switch would switch the order, but its the opposite
    """
    Duplicates each symbol in symbols an amount of times corresponding with
    the element in the repeats list and concatinates all of the symbols.
    The resulting string is reversed if switch is false.

    >>> fourth_pattern(['-', '+'], [4, 5], True)
    '----+++++'
    >>> fourth_pattern(['-', '+'], [4, 5],  False)
    '+++++----'
    >>> fourth_pattern([], [],  False)
    ''

    # Add your own doctests below
    >>> fourth_pattern(['A', '!'], [5, 10], True)
    'AAAAA!!!!!!!!!!'
    >>> fourth_pattern(['<', '>'], [3, 3], True)
    '<<<>>>'
    >>> fourth_pattern(['-', ''], [0, 100], False)
    Traceback (most recent call last):
    ...
    AssertionError: repeats must be positive
    """
    # YOUR CODE GOES HERE #
    result = ""
    for i in range(len(symbols)):
        assert repeats[i] > 0, "repeats must be positive"
        result += symbols[i] * repeats[i]
    return result if switch else result[::-1]

# Question 3
def shortest_bridge(bridge1, bridge2, bridge3):
    """
    Returns the bridge with the shortest description.
    Bridges that come earlier are prioritized to break ties.

    >>> shortest_bridge("flame","deep river", "flower")
    'bridge1'
    >>> shortest_bridge("hot flames","river", "flower")
    'bridge2'
    >>> shortest_bridge("flame","river", "calm and green")
    'bridge1'
    >>> shortest_bridge("very dangerous","deep river", "red flower")
    'bridge2'

    # Add your own doctests below
    >>> shortest_bridge("", "", "")
    'bridge1'
    >>> shortest_bridge("Python Bridge", "Java Bridge", "C# Bridge")
    'bridge3'
    >>> shortest_bridge("Damn bro", "idk", "what to test")
    'bridge2'
    """
    # YOUR CODE GOES HERE #
    min_length = len(bridge1)
    shortest = '1'
    if len(bridge2) < min_length: 
        min_length = len(bridge2)
        shortest = '2'
    if len(bridge3) < min_length: 
        min_length = len(bridge3)
        shortest = '3'
    return "bridge" + shortest

# Question 4.1
def average_without_min_max(people):
    """
    Returns the average of people after removing the min and max elements
    
    Args:
        people: a non-empty array
    
    >>> average_without_min_max([10, 10, 1, 16])
    10.0
    >>> average_without_min_max([2, 4, 10, 7, 9])
    6.67
    >>> average_without_min_max([2, 0, 10, 5])
    3.5

    # Add your own doctests below
    >>> average_without_min_max([])
    0.0
    >>> average_without_min_max([1, 2, 30, 4, 5])
    3.67
    >>> average_without_min_max([2, 4, 10, 20, 50, 0])
    9.0
    """
    # YOUR CODE GOES HERE #
    min_vals_needed = 3
    if len(people) < min_vals_needed:
        return 0.0
    else: 
        people.sort()
        no_min_max = people[1:-1]
        round_to = 2
        return round(sum(no_min_max) / len(no_min_max), round_to)

# Question 4.2
def best_average_bridge(people, bridges):
    """
    Given a list of bridges and their ratings, 
    returns the bridge with the highest average rating.
    First occurance is prioritized to break ties. 

    >>> ratings = [[1, 10, 5], [4, 6, 9]]
    >>> names = ["flames", "river"]
    >>> best_average_bridge(ratings, names)
    'river'

    >>> ratings = [[6, 10, 5, 3, 8], [10, 10, 9], [6, 6, 90]]
    >>> names = ["flames", "flower", "river"]
    >>> best_average_bridge(ratings, names)
    'flower'

    >>> ratings = [[], [], []]
    >>> names = ["flames", "flower", "river"]
    >>> best_average_bridge(ratings, names)
    'flames'

    >>> best_average_bridge([], [])
    'No bridges to choose from'

    # Add your own doctests below
    >>> best_average_bridge([[1, 2], [3, 4]], ["flower", "river"])
    'flower'
    
    >>> best_average_bridge([[1, 2, 333], [3, 4, 6]], ["flames", "river"])
    'river'
    
    >>> best_average_bridge([[1], [3, 4, 90]], ["flower", "trolls"])
    'trolls'
    >>> 
    """
    # YOUR CODE GOES HERE #
    avgs = []
    for ratings in people:
        avgs.append(average_without_min_max(ratings))
        
    if len(bridges) > 0:
        return bridges[avgs.index(max(avgs))] 
    else: 
        return "No bridges to choose from"

# Question 5
def sleepy_vs_awake(flowers):
    """
    Returns the flower that flowers has more of between 
    Sleeperose and Awakentia. Returns True if there's a tie
    and False if neither flower is in flowers.

    >>> sleepy_vs_awake(["Sleeperose", "Rose", "Sleeperose"])
    'Sleeperose'
    >>> sleepy_vs_awake(["Sleeperose", "Awakentia", "rose"])
    True
    >>> sleepy_vs_awake(["rose", "sleeperose", "awakentia", "daisy"])
    False
    >>> sleepy_vs_awake(["rose", "sleeperose", "Awakentia", "daisy"])
    'Awakentia'

    # Add your own doctests below
    >>> sleepy_vs_awake(["SleEpERose", "SLEEEPEROSE", "Awakentia", "sleprose"])
    'Awakentia'
    >>> sleepy_vs_awake(["Sleeperose", "", "Awakentia", "Wakeupia"])
    True
    >>> sleepy_vs_awake(["", "", "", ""])
    False
    """
    # YOUR CODE GOES HERE #
    awakes = flowers.count('Awakentia')
    sleeps = flowers.count('Sleeperose')
    if awakes == 0 and sleeps == 0:
        return False
    elif awakes == sleeps:
        return True
    elif awakes > sleeps:
        return "Awakentia"
    else:
        return "Sleeperose"

# Question 6
def sign(bridge_type, hint, your_name):
    """
    Returns a sign to new travelers with some advice about the bridge 
    and signed with your name

    >>> print(sign("Flower bridge", "Do the opposite.", "Dr. Who"))
    Dear traveler,
    Please be careful with the Flower bridge. My advice is: Do the opposite.
    <BLANKLINE>
    See you in Pythonia: Dr. Who
    >>> print(sign("Flame Bridge", "Do not be afraid of it.", ""))
    Dear traveler,
    Please be careful with the Flame Bridge. My advice is: Do not be \
afraid of it.
    <BLANKLINE>
    See you in Pythonia: 

    # Add your own doctests below
    >>> print(sign("Python", "", "Anonymous"))
    Dear traveler,
    Please be careful with the Python. My advice is: 
    <BLANKLINE>
    See you in Pythonia: Anonymous
    
    >>> print(sign("Unknown Bridge", "Turn back!", "theboyroy"))
    Dear traveler,
    Please be careful with the Unknown Bridge. My advice is: Turn back!
    <BLANKLINE>
    See you in Pythonia: theboyroy
    
    >>> print(sign("", "", ""))
    Dear traveler,
    Please be careful with the . My advice is: 
    <BLANKLINE>
    See you in Pythonia: 
    """
    # YOUR CODE GOES HERE #
    return f"Dear traveler,\nPlease be careful with the {bridge_type}. \
My advice is: {hint}\n\nSee you in Pythonia: {your_name}"

# Question 7
def my_nickname(first, last, age):
    """
    Returns a nickname given your full name and age

    >>> my_nickname("Marina", "Langlois", 25)
    '2aiaLANGLOIS5'
    >>> my_nickname("Marina", "Langlois", 2.5)
    'Error'
    >>> my_nickname("", "Langlois", 25)
    '2LANGLOIS5'
    >>> my_nickname("", "Langlois", 5)
    '0LANGLOIS5'

    # Add your own doctests below
    >>> my_nickname("Issac", "Roy", 18)
    '1saROY8'
    >>> my_nickname(["Issac"], "Roy", 18)
    'Error'
    >>> my_nickname("Issac", "Roy", 108)
    'Error'
    """
    # YOUR CODE GOES HERE #
    max_age = 100
    tens, ones = age//10, age%10
    every_other = 2
    if not (isinstance(first, str) and isinstance(last, str)): return "Error"
    elif not (isinstance(age, int) and 0 <= age < max_age): return "Error"
    else: return f"{tens}{first[1::every_other]}{last.upper()}{ones}"