"""
DSC 20 Winter 2024 Homework 04
Name: Issac Roy
PID: A17787465
Source: https://python-reference.readthedocs.io/ \
en/latest/docs/functions/zip.html
"""

# Question 1
def know_plant(path):
    """
    Returns a dictionary containing all the properties \
for each plant in the diary.

    >>> know_plant('files/diary01.txt')
    {'Harrada': ['Paralyze', 'Silence']}
    >>> know_plant('files/diary02.txt')
    {'Harrada': ['Paralyze'], 'Flame Stalk': ['Invisibility']}

    # Add at least 3 doctests below here #
    >>> know_plant('files/diary03.txt')
    {'Dandelion': ['Wisher']}
    
    >>> know_plant('files/diary04.txt')
    {}
    
    >>> know_plant('files/diary05.txt')
    {'Hydronius': ['wet', 'oozing'], 'Dryonius': ['dry']}
    """
    # YOUR CODE GOES HERE #
    out = {}
    with open(path, 'r') as f:
        reading = False
        for line in f:
            if line == 'Experiment Results:\n':
                reading = True
                continue
            elif line.lower() == 'end\n':
                reading = False
                continue
            
            if reading:
                info = line.replace('?', ',').split(',')
                property_pos = 2
                property = [info[property_pos][:-1]]
                if info[0] in out:
                    out[info[0]] += property
                else:
                    out[info[0]] = property
    return out

# Question 2
def create_potion(plants, path):
    """
    Creates a new file with all the given plants. Then determines if the \
plants are Posion or Potion depending on how many of them have the Paralyze \
property. Finally writes all the properties of the plants in order.

    >>> dict1 = {'Harrada': ['Paralyze', 'Silence']}
    >>> create_potion(dict1, "files/potion1.txt")
    >>> with open("files/potion1.txt", 'r') as f:
    ...     for l in f:
    ...         print(l.strip())
    Harrada
    Potion
    Paralyze,Silence
    >>> dict2 = {'Harrada': ['Paralyze'], 'Flame Stalk': ['Paralyze'],\
'Stone Flower': ['Paralyze']}
    >>> create_potion(dict2, "files/potion2.txt")
    >>> with open("files/potion2.txt", 'r') as f:
    ...     for l in f:
    ...         print(l.strip())
    Harrada
    Flame Stalk
    Stone Flower
    Poison
    Paralyze

    # Add at least 3 doctests below here #
    >>> create_potion({}, "files/potion3.txt")
    >>> with open("files/potion3.txt", 'r') as f:
    ...     for l in f:
    ...         print(l.strip())
    No Output
    
    >>> dict2['Stone Flower'] = ['paralyze']
    >>> create_potion(dict2, "files/potion4.txt")
    >>> with open("files/potion4.txt", 'r') as f:
    ...     for l in f:
    ...         print(l.strip())
    Harrada
    Flame Stalk
    Stone Flower
    Potion
    Paralyze,paralyze
    
    >>> dict3 = {'DefNotPoison': ['Paralyze','Suffocation','Death','Rainbow']}
    >>> create_potion(dict3, "files/potion5.txt")
    >>> with open("files/potion5.txt", 'r') as f:
    ...     for l in f:
    ...         print(l.strip())
    DefNotPoison
    Potion
    Paralyze,Suffocation,Death,Rainbow
    """
    # YOUR CODE GOES HERE #
    with open(path, 'w') as file:
        if len(plants) == 0:
            file.write('No Output')
            return
        
        num_paralyze = 0
        poison_threshold = 2
        properties = []
        for key, vals in plants.items():
            file.write(key+'\n')
            properties += [val for val in vals if val not in properties]
            num_paralyze += ('Paralyze' in vals)
            
        if num_paralyze > poison_threshold:
            file.write('Poison'+'\n')
        else:
            file.write('Potion'+'\n')
        
        file.write(','.join(properties))

# Question 3
def potion_name(plants):
    """
    Creates a potion name based on the given plants. If there are an even \
number of plants under budget, take the first 3 letters of each plant under \
budget and join them to make the potion name. If there are an odd number \
of plants under budget, do the same, but with the last 3 letters instead.

    >>> input_1 = [('Harrada', 'yellow', 19), ('Flame Stalk', 'red', 13), \
('Stone Flower', 'gray', 32), ('Crystal Snowflake', 'blue', 48), \
('Foxglove', 'pink', 20), ('Dangerous Nightshade', 'purple', 18)]
    >>> potion_name(input_1)
    'Adaalkade'

    >>> input_2 = [('White Snakeroot', 'white', 19), \
('Bitter Hogweed', 'black', 13)]
    >>> potion_name(input_2)
    'Whibit'

    >>> input_3 = []
    >>> potion_name(input_3)
    ''

    # Add at least 3 doctests below here #
    >>> potion_name([['Harrada', 'yellow', 20], ('Flame Stalk', 'red', 13)])
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> potion_name((('Harrada', 'yellow', 20), ('Flame Stalk', 'red', 13)))
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> potion_name([('Harrada', 20), ('Flame Stalk', 'red', 13)])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #
    assert isinstance(plants, list)
    assert all([isinstance(plant, tuple) and len(plant) == 3 \
        for plant in plants])
    
    price_pos = 2
    budget = 20
    name_cuttoff = 3
    temp = list(filter(lambda plant: plant[price_pos] < budget, plants))
    return ''.join(list(map(lambda plant: plant[0][:name_cuttoff] \
        if len(temp)%2 == 0 else plant[0][-name_cuttoff:], temp))).title()

# Question 4
def trade(potions, prices, consumer_list):
    """
    Returns the total price of the two most expensive potions that you have \
which the consumer is looking to buy.

    >>> trade(['health', 'magic'], [10, 10], ['health', 'magic'])
    20
    >>> trade(['health', 'magic', 'large_health'], [10, 20, 30], \
    ['health', 'large_health', 'magic'])
    50
    >>> trade(['health', 'magic', 'large_health', 'large_magic'],\
    [5, 10, 15, 20], ['magic', 'health', 'large_health'])
    25

    # Add at least 3 doctests below here #
    >>> trade(['health', 'magic'], ['10', 10], ['health', 'magic'])
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> trade(['health', 'magic', 'large_health', 'large_magic'],\
    [5, 10, 1, 20], ['magic', 'health', 'large_health'])
    15
    
    >>> trade(['health', 'magic', 'large_health', 'large_magic'],\
    [50, 10, 15, 20], ['magic', 'health', 'small_health'])
    60
    """
    # YOUR CODE GOES HERE #
    assert isinstance(potions, list)
    assert all([isinstance(potion, str) for potion in potions])
    assert isinstance(prices, list)
    assert all([isinstance(price, int) for price in prices])
    assert isinstance(consumer_list, list)
    assert all(isinstance(item, str) for item in consumer_list)
    
    temp = list(filter(lambda pair: pair[0] in consumer_list, \
        zip(potions, prices)))
    target_pots, target_prices = zip(*temp)
    target_prices = sorted(list(target_prices))[::-1]
    return target_prices[0] + target_prices[1]

# Question 5
def potion_magic(potions, operations):
    """
    Performs the given operations in order on potions.

    >>> potion_magic("incorrect input", ['mix'])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> potion_magic(['health', 'magic'], ['eliminate', 'reduce'])
    ['hea', 'mag']
    
    >>> potion_magic(['health_large_potion', 'health'], ['eliminate', 'mix'])
    'htlaeh'

    # Add at least 3 doctests below here #
    >>> potion_magic([], ['mix'])
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> potion_magic(['health_large_potion', 'health'], ['reduce', 'mix'])
    'aehaeh'
    
    >>> potion_magic(['health_large_potion', 'health'], ['eliminate', \
    'reduce', 'mix'])
    'aeh'
    """

    # TODO: Fill out the lambda functions as dictionary values
    # Break lines if go past 79 characters
    op_dict = {
        'mix': lambda lst: ''.join(lst)[::-1],
        'reduce': lambda lst: list(map(lambda x: x[:3] \
            if len(x) >= 3 else x, lst)),
        'eliminate': lambda lst: list(filter(lambda x: len(x) <= 6, lst))
    }

    # YOUR CODE GOES HERE #
    assert isinstance(potions, list) and len(potions) > 0
    assert all([isinstance(potion, str) for potion in potions])
    assert isinstance(operations, list) and len(operations) > 0
    assert all([isinstance(operation, str) and (operation == 'mix' \
        or operation == 'reduce' or operation == 'eliminate') \
            for operation in operations])
    
    for operation in operations:
        potions = op_dict[operation](potions)
    
    return potions