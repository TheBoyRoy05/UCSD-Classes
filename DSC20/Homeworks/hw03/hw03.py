"""
DSC 20 Winter 2024 Homework 03
Name: Issac Roy
PID: A17787465
Source: https://www.programiz.com/python-programming/methods/string/isalnum
"""

# Question 1.1
def animals(animal_dict, target):
    """
    Creates a list of all animals of a type specified by target

    >>> animals_dict = {"dogs": "mammals", "snakes": "reptiles", \
    "dolphins": "mammals", "sharks": "fish"}
    >>> target = "mammals"
    >>> animals(animals_dict, target)
    ['dogs', 'dolphins']

    >>> target = "amphibians"
    >>> animals(animals_dict, target)
    []

    >>> animals_dict = {True: "mammals"}
    >>> animals(animals_dict, target)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below
    >>> animals({"Cow": 10}, target)
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> animals_dict = {"dogs": "mammals", "snakes": "reptiles", \
    "dolphins": "mammals", "sharks": "fish"}
    >>> animals(animals_dict, (0, 0))
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> animals({}, target)
    []
    """
    # YOUR CODE GOES HERE #
    assert isinstance(animal_dict, dict)
    assert all(isinstance(key, str) and isinstance(val, str) \
        for key, val in animal_dict.items())
    assert isinstance(target, str)
    return [key for key, val in animal_dict.items() if val == target]

# Question 1.2
def animal_type(animals):
    """
    Given a dict of animals with their energy levels and animal types, \
returns a list of all animal types (duplicates allowed)
    
    >>> animals = {"dogs": [10, "omnivores"], "snakes": [8, "carnivores"], \
    "lions": [12, "carnivores"], "sheep": [7, "herbivores"]}
    >>> animal_type(animals)
    ['omnivores', 'carnivores', 'carnivores', 'herbivores']

    >>> animals = {"bears": [5, "omnivores"]}
    >>> animal_type(animals)
    ['omnivores']

    >>> animals = {"dogs": [0.8, "omnivores"], "snakes": [8.1, "carnivores"], \
    "lions": [12, "carnivores"], "sheep": [7, "herbivores"]}
    >>> animal_type(animals)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below
    >>> animal_type({})
    []
    
    >>> animal_type({(0, 0): [0, "omnivore"]})
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> animal_type({"dogs": (100, "omnivore")})
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> animal_type({"dogs": (100, False)})
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #
    assert isinstance(animals, dict)
    assert all(isinstance(val, list) and isinstance(key, str) \
        and len(val) == 2 and isinstance(val[0], int) \
            and isinstance(val[1], str) for key, val in animals.items())
    return [val[1] for val in animals.values()]

# Question 1.3
def hungry(animals, food, target_energy):
    """
    Creates a list and populates it with tuples containing the animals that \
can eat the given food and how much they need to reach the target energy, \
and populates the list with dislike :( if they can't eat it

    >>> animals = {"dogs": [10, "omnivores"], "snakes": [8, "carnivores"], \
    "lions": [12, "carnivores"], "sheep": [7, "herbivores"]}
    >>> target = 15
    >>> food = ("lettuce", ["omnivores", "herbivores"], 2)
    >>> hungry(animals, food, target)
    [('dogs', 3), 'dislike :(', 'dislike :(', ('sheep', 4)]

    >>> animals = {"dogs": [10, "omnivores"], "snakes": [8, "carnivores"], \
    "lions": [12, "carnivores"], "bears": [5, "omnivores"]}
    >>> target = 15
    >>> food = ("grass", ["herbivores"], 2)
    >>> hungry(animals, food, target)
    ['dislike :(', 'dislike :(', 'dislike :(', 'dislike :(']

    >>> food = ("berries", "herbivores", 2)
    >>> hungry(animals, food, target)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below
    >>> hungry(animals, (True, ['omnivores'], 1), target)
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> hungry(animals, ("berries", ['omnivores'], -1), target)
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> hungry(animals, ("berries", ['omnivores'], 1), 0)
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> hungry(animals, ('berries', ['omnivores'], 1), 1)
    [('dogs', 0), 'dislike :(', 'dislike :(', ('bears', 0)]
    """
    # YOUR CODE GOES HERE #
    assert isinstance(animals, dict)
    assert all(isinstance(val, list) and isinstance(key, str) \
        and isinstance(val[0], int) and isinstance(val[1], str) \
            for key, val in animals.items())
    
    assert isinstance(food, tuple)
    assert isinstance(food[0], str) 
    assert isinstance(food[1], list)
    assert isinstance(food[2], int)
    assert all(isinstance(animal_type, str) for animal_type in food[1])
    assert food[2] > 0
    
    assert isinstance(target_energy, int) and target_energy > 0
    
    energy_pos = 2
    return [(key, max((target_energy-val[0])//food[energy_pos] + \
        ((target_energy-val[0])%food[energy_pos] != 0), 0)) \
            if val[1] in food[1] else 'dislike :(' \
                for key, val in animals.items()]

# Question 2
def affordable_arcade_game(arcade_games, budget):
    """
    Returns the highest rated game within the budget. \
Titles with later alphabetical order are prioritized for ties.

    >>> arcade_games = {'Pac-Man': [(5, 4.7), (10, 4.9)],\
    'Galaga': [(8, 4.8), (12, 4.6)],\
    'Street Fighter II': [(15, 4.9)],\
    'Mortal Kombat': [(12, 4.7), (18, 4.8)],\
    'Donkey Kong': [(10, 4.5), (14, 4.6)]}
    >>> affordable_arcade_game(arcade_games, 10)
    'Pac-Man'
    >>> affordable_arcade_game(arcade_games, 15)
    'Street Fighter II'

    # Add your own doctests below
    >>> affordable_arcade_game(arcade_games, 8)
    'Galaga'
    
    >>> arcade_games['Mortal Kombat'] = [(10, 4.9)]
    >>> affordable_arcade_game(arcade_games, 10)
    'Pac-Man'
    
    >>> arcade_games = {'Pac-Man': [(5, 4.7)]}
    >>> affordable_arcade_game(arcade_games, 15)
    'Pac-Man'
    """
    # YOUR CODE GOES HERE #
    affordable = [(key, max([0] + [val[1] for val in arcade_games[key] \
        if val[0] <= budget])) \
            for key in sorted(list(arcade_games.keys()))[::-1]]
    
    keys = [i[0] for i in affordable]
    vals = [i[1] for i in affordable]
    
    return keys[vals.index(max(vals))]

# Question 3
def calculate_probability_ratio(prizes, probabilities, target_prize):
    """
    Returns the probability of winning the target prize relative to the \
total probablity.

    >>> calculate_probability_ratio(["Gold Coin", "Silver Coin", "Gem", \
        "Key"], [0.1, 0.2, 0.3, 0.4], "Gem")
    0.3

    >>> calculate_probability_ratio(["Sword", "Shield", "Bow", "Staff"], \
        [0.25, 0.2, 0.3, 0.25], "Shield")
    0.2

    >>> calculate_probability_ratio(["Coin", "Shield", "Gem"], \
        [0.25, 0.2, 0.5], 0)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below
    >>> calculate_probability_ratio(["Coin", "Shield", "Gem"], \
        [0.25, 0.2], "Coin")
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> calculate_probability_ratio(["Coin", "Shield", "Gem"], \
        [0.25, 2, 0.5], "Coin")
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> calculate_probability_ratio(["Coin", "Shield", "Gem"], \
        [0.05, 0.2, 0.25], "Coin")
    0.1
    """
    # YOUR CODE GOES HERE #
    assert isinstance(prizes, list) 
    assert all([isinstance(prize, str) for prize in prizes])
    assert isinstance(probabilities, list) 
    assert all([isinstance(prob, float) for prob in probabilities])
    assert isinstance(target_prize, str)
    
    assert len(prizes) == len(probabilities)
    assert target_prize in prizes
    
    return [probabilities[i] / sum(probabilities) for i in range(len(prizes)) \
        if prizes[i] == target_prize][0]

# Question 4
def account(string):
    """
    Given an alphanumeric string with at least one number, returns the string \
with all consonents lowercased and vowels uppercased and all the digits \
at the start of the string repeated as many times as the last digit.

    >>> string = "helloDSC20"
    >>> account(string)
    'hEllOdsc'

    >>> string = "DSC2023python"
    >>> account(string)
    '202320232023dscpythOn'

    >>> string = "hello!! DSC20"
    >>> account(string)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below
    >>> account('')
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> account('HELLOWORLD')
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> account('2190920')
    ''
    """
    # YOUR CODE GOES HERE #
    assert string.isalnum()
    assert any([c.isnumeric() for c in string])
    
    letters = [c.upper() if c in 'aeiou' else c for c in string.lower() \
        if not c.isnumeric()]
    nums = [c for c in string if c.isnumeric()]
    return ''.join(nums)*int(nums[-1]) + ''.join(letters)

# Question 5
def prize_combinations(prizes, target_tickets):
    """
    Returns all possible pairs of prizes you can buy with the tickets you have.

    >>> prizes = [("Plush Toy", 10), ("Board Game", 20), ("Puzzle", 5), \
        ("Remote Control Car", 30)]
    >>> prize_combinations(prizes, 15)
    [('Plush Toy', 'Puzzle'), ('Puzzle', 'Plush Toy')]

    >>> prize_combinations(prizes, 10)
    []

    >>> prize_combinations(prizes, 1.0)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below
    >>> prize_combinations(prizes, 25)
    [('Board Game', 'Puzzle'), ('Plush Toy', 'Puzzle'), \
('Puzzle', 'Board Game'), ('Puzzle', 'Plush Toy')]

    >>> prize_combinations([], 25)
    []
    
    >>> prizes.append("Hello World")
    >>> prize_combinations(prizes, 25)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #
    assert isinstance(prizes, list)
    assert all([isinstance(prize, tuple) and len(prize) == 2 \
        and isinstance(prize[0], str) and isinstance(prize[1], int) \
            for prize in prizes])
    assert isinstance(target_tickets, int)
    
    return sorted([(p1[0], p2[0]) for p1 in prizes for p2 in prizes \
        if p1[0] != p2[0] if p1[1] + p2[1] <= target_tickets])
    
# Question 6
def manage_inventory(inventory, action, item_name, quantity):
    """
    Performs an action to an item in the inventory by either adding or \
subtracting it by quantity. If you try to remove more items than you have, \
no action happens.

    Parameters:
        inventory (dict): keys are items (str) and values are positive ints
        action (str): either 'add' or 'remove'
        item_name (str): item to be altered
        quantity (int): non-negative int to alter item by

    >>> inventory = {'coins': 100, 'health potions': 5}
    >>> manage_inventory(inventory, 'add', 'coins', 50)
    {'coins': 150, 'health potions': 5}

    >>> manage_inventory(inventory, 'remove', 'health potions', 10)
    {'coins': 100, 'health potions': 5}

    >>> manage_inventory(inventory, 'remove', 'health potions', 3)
    {'coins': 100, 'health potions': 2}

    >>> manage_inventory([], 'remove', 'health potions', 3)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below
    >>> manage_inventory(inventory, -10, 'health potions', 3)
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> manage_inventory(inventory, 'remove', 'health potions', -3)
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> inventory = {'coins': 100, 'health potions': 0}
    >>> manage_inventory(inventory, 'remove', 'health potions', 3)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #
    assert isinstance(inventory, dict)
    assert all([isinstance(key, str) and isinstance(val, int) and val > 0 \
        for key, val in inventory.items()])
    assert isinstance(action, str)
    assert isinstance(item_name, str)
    assert isinstance(quantity, int) and quantity >= 0
    
    return {key: (val if item_name != key else \
        val + quantity if action == 'add' else \
            val - quantity if action == 'remove' and quantity <= val \
                else val) for key, val in inventory.items()}

# Question 7 Extra Credit
def arcade(games, money):
    """
    Returns the first profitable game in games. A game is profitable if the \
sum of points gained/lost is strictly positive and if the money you have, \
converted to game coins, is greater than or equal to the sum of the \
game coins used in previous games.

    >>> games = {"Pac-Man": [(20, 5), (15, 8), (-25, 12)], \
    "Space Invaders": [(-10, 3), (3, 5)], \
    "Street Fighter II": [(10, 2), (5, 8), (10, 7)]}
    >>> money = 5
    >>> arcade(games, money)
    'Street Fighter II'

    >>> money = 10
    >>> arcade(games, money)
    'Pac-Man'

    >>> money = -2
    >>> arcade(games, money)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below
    >>> games["Street Fighter II"] = [(1, 0)]
    >>> arcade(games, 0)
    'Street Fighter II'
    
    >>> games["Street Fighter II"] = [(1)]
    >>> arcade(games, 0)
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> games["Pac-Man"].append((1.0, 2.0))
    >>> arcade(games, 10)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #
    assert isinstance(games, dict)
    assert all([isinstance(key, str) and isinstance(vals, list) \
        and all([isinstance(val, tuple) and len(val) == 2 \
            and isinstance(val[0], int) and isinstance(val[1], int) \
                for val in vals]) for key, vals in games.items()])
    assert isinstance(money, int) and money >= 0
    
    mnt_to_coins = 4
    return [key for key, vals in games.items() \
        if sum([val[0] for val in vals]) > 0 \
            if sum([val[1] for val in vals]) <= money*mnt_to_coins][0]