"""
DSC 20 Winter 2024, Lab 03
Name: Issac Roy
PID: A17787465
Source: TODO
"""

# Question 1.1
def updated_slogans(slogans):
    """
    Returns a list of capitalized slogans.

    Args:
        slogans: a list of slogans represented as strings.

    Returns: the input slogans with all characters capitalized.

    >>> slogans = ["best SweaTERs", "Cheap and WARM"]
    >>> updated_slogans(slogans)
    ['BEST SWEATERS', 'CHEAP AND WARM']
    >>> slogans = ["", "SleiGH RiDe"]
    >>> updated_slogans(slogans)
    ['', 'SLEIGH RIDE']
    >>> slogans = ["!!!", "BeWaRE! DANger ahead", "Candy CANE lane"]
    >>> updated_slogans(slogans)
    ['!!!', 'BEWARE! DANGER AHEAD', 'CANDY CANE LANE']
    """
    # YOUR CODE GOES HERE #
    return [s.upper() for s in slogans]

# Question 1.2
def prices_total(prices):
    """
    Calculate the total price of ornaments with 20 dollars or less.

    Args:
        prices: a list of ornament prices, each represented as an integer.

    Returns:
        the total price of eligible ornaments.

    >>> prices = [3, 40, 10, 2]
    >>> prices_total(prices)
    15
    >>> prices = [4, 40, 20, 1]
    >>> prices_total(prices)
    25
    >>> prices = []
    >>> prices_total(prices)
    0
    """
    # YOUR CODE GOES HERE #
    return sum([price for price in prices if price <= 20])

# Question 1.3
def buying_ornaments(stores):
    """
    Returns a list of strings containing ornament type if budget is enough,
    or 'too pricey' if the ornament price exceeds budget.

    Args:
        stores: a list of tuples as stores, where the first element 
        in the tuple contains ornament type, the second containing price of 
        ornament, and the third containing the budget for the store.

    Returns:
        a list of strings that is converted from tuples based on requirements.

    >>> stores = [("heavy", 10, 10), ("light", 5, 10), ("heavy", 100, 20)]
    >>> buying_ornaments(stores)
    ['heavy', 'light', 'too pricey']

    >>> stores = [("orange", 20, 0), ("white", 0, 0), ("green", 100, 10)]
    >>> buying_ornaments(stores)
    ['too pricey', 'white', 'too pricey']

    >>> stores = [("small", 20, 10), ("huge", 15, 14), ("polka dot", 10, 150), \
("purple", 100, 150), ("festive", 277.1, 277)]
    >>> buying_ornaments(stores)
    ['too pricey', 'too pricey', 'polka dot', 'purple', 'too pricey']
    """
    # YOUR CODE GOES HERE #
    return ['too pricey' if s[1] > s[2] else s[0] for s in stores]

#Question 2
def delivery(ornament_weights):
    """
    Return a list of strings representing how to take each ornament home.

    Args:
        ornament_weights: a list of integers representing ornament weights.

    Returns:
        a list of messages according to individual pumpkin weight.

    >>> delivery([22, 40, 55, 91])
    ['I got it', 'I got it', 'Help me', 'Call delivery']
    >>> delivery([])
    []
    >>> delivery([0, 100000])
    ['I got it', 'Call delivery']
    """
    # YOUR CODE GOES HERE #
    return ['I got it' if w <= 40 else 'Help me' if w <= 80 else
            'Call delivery' for w in ornament_weights]

#Question 3
def prices(ornaments):
    """
    Returns a list of delivery costs for each ornament.

    Args:
        ornaments: a list of lists where each inner list contains the 
        weight and size for one ornament.

    Returns:
        a list of delivery costs based on formula provided.

    >>> prices([[22, 40, 55, 91], [1, 2, 3, 3]])
    [2.2, 16.0, 166.375, 753.571]
    >>> prices([[], []])
    []
    >>> prices([[61], [5]])
    [8445.963]
    """
    # YOUR CODE GOES HERE #
    return [round((ornaments[0][i]/10)**ornaments[1][i], 3)
            for i in range(len(ornaments[0]))]

#Question 4
def adjusted_prices(prices, company_fees):
    """
    Returns adjusted price due to peak delivery period.

    Args:
        prices: a list of delivery prices for ornaments.
        company_fees: a dictionary where the keys are company names and 
        values are extra delivery fees for the company.

    Return a list of lists where each inner list contains delivery prices 
    for an individual company with extra fees.

    >>> prices = []
    >>> company_fees = {'Santa Express': 1, 'UPS': 1.5, 'USPS': 3}
    >>> adjusted_prices(prices, company_fees)
    [[], [], []]

    >>> prices = [1, 2, 2]
    >>> company_fees = {'USPS': 3, 'FedEx': 2, 'UPS': 1.5}
    >>> adjusted_prices(prices, company_fees)
    [[4, 5, 5], [3, 4, 4], [2.5, 3.5, 3.5]]

    >>> prices = [2.2, 16, 166.375, 753.571]
    >>> company_fees = {'Santa Express': 1, 'UPS': 1.5, 'USPS': 3}
    >>> adjusted_prices(prices, company_fees)
    [[3.2, 17, 167.375, 754.571], [3.7, 17.5, 167.875, 755.071], \
[5.2, 19, 169.375, 756.571]]
    """
    # YOUR CODE GOES HERE #
    return [[price + fee for price in prices] for fee in company_fees.values()]

# Question 5.1
def decode_directions(encoded_messages, decode_scheme):
    """
    Returns a list of directions after message has been decoded.

    Args:
        encoded_messages: a list of 8 bit bit-strings as encoded messages.
        decode_scheme: a dictionary containing correspondence between 
        modulo operation result and direction.
    
    Returns:
        a list of directions after computing decoding key and checking
        the decoding scheme. 

    >>> encoded_messages = []
    >>> decode_scheme = {0: '+', 1: '>', 2: '+', 3: '<', 4: '<', 5: '>'}
    >>> decode_directions(encoded_messages, decode_scheme)
    []

    >>> encoded_messages = ['11111111', '10111111', '01000011', '10101111']
    >>> decode_directions(encoded_messages, decode_scheme)
    ['+', '>', '<', '+']

    >>> encoded_messages = ['10010000', '00100111', '01100101', '11001001']
    >>> decode_scheme = {0: '+', 1: '+', 2: '+', 3: '+', 4: '+', 5: '+'}
    >>> decode_directions(encoded_messages, decode_scheme)
    ['+', '+', '+', '+']
    """
    # YOUR CODE GOES HERE #
    return [decode_scheme[m.count('1')%6] for m in encoded_messages]

# Question 5.2
def prop_straight(directions):
    """
    Returns proportion of times where straight is the right direction.

    Args:
        directions: a list of correct directions when facing crossroads.

    Returns:
        the proportion of times where the correct direction is straight, 
        rounded to 2 decimal places.

    >>> directions = []
    >>> prop_straight(directions)
    0.0

    >>> directions = ['+', '<', '+']
    >>> prop_straight(directions)
    66.67

    >>> directions = ['+', '>', '<', '+']
    >>> prop_straight(directions)
    50.0

    >>> directions = ['+', '+', '+', '+']
    >>> prop_straight(directions)
    100.0
    """
    # YOUR CODE GOES HERE #
    return round(len([d for d in directions if d=='+'])/len(directions)*100,2)\
        if len(directions) != 0 else 0.0

#Question 6.1
def most_expensive(file1):
    """
    Returns the most expensive activity in the given csv file.

    Args:
        file1: a csv file containing Frost Festival activities.

    Returns: a string of the most expensive activity in the input file.

    >>> most_expensive("Files/frost_festival1.csv")
    'Sleigh Ride'
    
    >>> most_expensive("Files/frost_festival2.csv")
    'Skate with the Elves'

    >>> most_expensive("Files/frost_festival3.csv")
    'Ice Maze'
    """
    # YOUR CODE GOES HERE #
    with open(file1, 'r') as f_in:
        max_price = 0
        out = ''
        lines = f_in.readlines()[1:]
        for i in range(len(lines)):
            info = lines[i].split(',')
            price = int(info[2][1:])
            if price >= max_price:
                max_price = price
                out = info[0]
    return out

# Question 6.2
def combine(my_file, tutor_file):
    """
    Combine the content of two files into one.

    Args:
        my_file: a csv file containing Pythonia Frost Festival activities.
        tutor_file: a csv file containing more Pythonia Frost Festival 
        activities.
        
    Returns:
        None.

    >>> combine("Files/my_list.csv", "Files/tutor_list.csv")
    >>> with open("Files/my_list.csv") as f:
    ...     print(f.read())
    ...
    Event,Time,Price,Wait Time,
    Yeti Hunting,10 AM,$10,0 min,
    Skate with the Elves,12 PM,$10,120 min,
    Photobooth,3 PM,$5,30 min,
    Ice Maze,5 PM,$12,150 min,
    Sleigh Ride,7 PM,$15,30 min,

    >>> combine("Files/my_list2.csv", "Files/tutor_list2.csv")
    >>> with open("Files/my_list2.csv") as f:
    ...     print(f.read())
    ...
    Event,Time,Price,Wait Time,
    Yeti Hunting,11 AM,$10,120 min,
    Skate with the Elves,2 PM,$8,120 min,
    Photobooth,3 PM,$5,30 min,
    Ice Maze,4 PM,$17,90 min,
    Skate with the Elves,7 PM,$8,120 min,
    Photobooth,9 PM,$5,30 min,
    """
    # YOUR CODE GOES HERE #
    with open(my_file, 'a') as my_file:
        with open(tutor_file, 'r') as tutor_file:
            my_file.write('\n' + ''.join(tutor_file.readlines()[1:]))