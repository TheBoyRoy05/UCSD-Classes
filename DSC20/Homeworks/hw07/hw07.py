"""
DSC 20 Winter 2024 Homework 07
Name: Issac Roy
PID: A17787465
Source: N/A
"""

# Question 1
def marketplace(start, market_map, directions, spent=0):
    """
    Returns the amount of money you spend as you wander the marketplace.
    Returns early if you hit the border and returns scammed if you land on x.

    >>> market_map = [
    ... "...............",
    ... ".5_1_7_x___4_7.",
    ... ".x__8_3__2___6.",
    ... "._5_2_87_35__2.",
    ... ".___6___5_8x2_.",
    ... ".2_7_9_44_3_2_.",
    ... "..............."]

    >>> directions = ['U','R','R','U','L','U','L','L']
    >>> marketplace((5,7), market_map, directions)
    15
    >>> marketplace((1,7), market_map, directions)
    'scammed!'

    >>> directions = ['L','L','L','L','L','L','L','L','L','L','L','L']
    >>> marketplace((3,10), market_map, directions)
    30

    # Add at least 3 doctests below here #
    >>> marketplace((1,1), market_map, [])
    5
    >>> marketplace((1,1), market_map, ['D'])
    'scammed!'
    
    >>> market_map = [
    ... "...............",
    ... "._____________.",
    ... "._____________.",
    ... "._____________.",
    ... "._____________.",
    ... "._____________.",
    ... "..............."]
    >>> directions = ['U','R','R','U','L','U','U','L']
    >>> marketplace((5,6), market_map, directions)
    0
    
    >>> market_map = [
    ... "...............",
    ... ".3_2_1_x_x_x_x.",
    ... ".x_222____33__.",
    ... ".2_9_4____xx_1.",
    ... ".__334__x_2_1_.",
    ... ".2_7_9_44_3_2_.",
    ... "..............."]
    >>> directions = ['L', 'U', 'U', 'U', 'L']
    >>> marketplace((5,6), market_map, directions)
    21
    """
    # YOUR CODE GOES HERE #
    curr_pos = market_map[start[0]][start[1]]
    if curr_pos == '.': return spent
    if curr_pos == 'x': return 'scammed!'
    spending = spent + int(curr_pos) if curr_pos != '_' else spent
    
    if len(directions) == 0: return spending
    
    if directions[0] == 'L':
        new_start = (start[0], start[1]-1)
    elif directions[0] == 'R':
        new_start = (start[0], start[1]+1)
    elif directions[0] == 'D':
        new_start = (start[0]+1, start[1])
    elif directions[0] == 'U':
        new_start = (start[0]-1, start[1])
        
    return marketplace(new_start, market_map, directions[1:], spending)

# Question 2  (EXTRA CREDIT)
def palindromes(word, start=0, end=0, first=True):
    """
    Returns the number of palindromes in a given word. Single letters don't \
count as palindromes.

    >>> palindromes("aaa")
    3
    >>> palindromes("abcba")
    2
    >>> palindromes("ababaa")
    5

    # Add at least 3 doctests below here #
    >>> palindromes('a')
    0
    >>> palindromes('aaaaa')
    10
    >>> palindromes('levelracecarrot')
    6
    """
    # YOUR CODE GOES HERE #
    def is_palindrome(input):
        """
        Returns whether a given input is a palindrome using recursion
        """
        if len(input) <= 1:
            return True
        return input[0] == input[-1] and is_palindrome(input[1:-1])
    
    if end == 0:
        end = len(word) - 1
        
    if len(word) <= 1:
        return 0 if first else []
    
    out = palindromes(word[1:], start+1, end, False) + \
        palindromes(word[:-1], start, end-1, False)
        
    if is_palindrome(word):
        out = [(word, start, end)] + out
        
    return len(set(out)) if first else out

# Question 3
def doctests_q3():
    """
    >>> event = EventTracker(2)
    >>> date = "2-20-2024"
    >>> event.months_left(date)
    '0 months left to midterm.'
    
    >>> EventTracker.change_event("final")
    >>> event.change_event_month(6)
    >>> event.months_left(date)
    '4 months left to final.'

    >>> event.change_event_month(1)
    >>> event.months_left(date)
    'You missed final.'

    >>> event = EventTracker(7)
    >>> EventTracker.change_event("4th of July")
    >>> date = "5-24-2024"
    >>> event.months_left(date)
    '2 months left to 4th of July.'
    >>> date = "12-24-2024"
    >>> event.months_left(date)
    'You missed 4th of July.'

    # Add your own doctests below for better testing, although not required.
    """
    return

class EventTracker:
    event = 'midterm'

    def __init__(self, event_month):
        self.event_month = event_month

    @classmethod
    def change_event(cls, new_event):
        cls.event = new_event

    @staticmethod
    def extract_month(date):
        return int(date.split('-')[0])

    def months_left(self, date):
        months = self.event_month - EventTracker.extract_month(date)
        if months < 0:
            return f'You missed {self.event}.'
        else:
            return f'{months} months left to {self.event}.'

    def change_event_month(self, new_month):
        self.event_month = new_month

# Question 4
def doctests_q4():
    """
    >>> n1 = Notebook("My encounters", "Marina", 12, \
    {'people': [], 'animals': []})
    >>> n1.description
    'This notebook is to keep track of encountered people and animals.'
    >>> n1.title
    'My encounters'
    >>> n1.author
    'Marina'
    >>> n1.tip
    12
    >>> n1.get_people()
    []
    >>> n1.new_encounter('people', 'tutors')
    True
    >>> n1.new_encounter('animals', 'recursive dragon')
    True
    >>> n1.new_encounter('people', 'tutors')
    'Already encountered'
    >>> n1.new_encounter('animals', 'baby pandas')
    True
    >>> n1.encounters
    {'people': ['tutors'], 'animals': ['recursive dragon', 'baby pandas']}
    >>> n1.get_people()
    ['tutors']
    >>> n1.get_animals()
    ['recursive dragon', 'baby pandas']
    >>> n1.info()
    "Marina has spent 12 months in Pythonia and has encountered 1 people and \
2 animals. These are noted in 'My encounters'."

    >>> n2 = Notebook("Encounters", "Noto", 1, \
    {'people': ['Ben', 'Matilda', 'Charisse'], 'animals': ['cat']})
    >>> n2.get_people()
    ['Ben', 'Matilda', 'Charisse']
    >>> Notebook.edit_description()
    'This notebook only has 1 purpose - there is no need to modify its \
description!'

    # Add your own doctests below for better nesting, although not required.
    """
    return

class Notebook:
    """
    Implementation of Notebook
    """
    # YOUR CODE GOES HERE #
    description = 'This notebook is to keep track of encountered people \
and animals.'
    
    @staticmethod
    def edit_description():
        return 'This notebook only has 1 purpose - there is no need to \
modify its description!'

    def __init__(self, title, author, tip, encounters) -> None:
        self.title = title
        self.author = author
        self.tip = tip
        self.encounters = encounters

    def info(self):
        return f"{self.author} has spent {self.tip} months in Pythonia and \
has encountered {len(self.encounters['people'])} people and \
{len(self.encounters['animals'])} animals. These are noted in '{self.title}'."

    def get_people(self):
        return self.encounters['people']
    
    def get_animals(self):
        return self.encounters['animals']
    
    def new_encounter(self, new_type, new_add):
        if new_add in self.encounters[new_type]:
            return 'Already encountered'
        else:
            self.encounters[new_type] += [new_add]
            return True

# Question 5
def doctests_q5():
    """
    >>> shoem = Merchant('shoemaker', {'boots': [5, 10], 'sandals': \
    [2, 3], 'heels': [1, 20]}, 100, ['Pythonia', 'Garthon'])
    >>> print(shoem)
    shoemaker has brought boots, sandals, heels. \
They are able to sell their wares in Pythonia, Garthon.
    >>> shoem.get_type()
    'shoemaker'
    >>> shoem.get_stock()
    {'boots': [5, 10], 'sandals': [2, 3], 'heels': [1, 20]}
    >>> shoem.get_cash()
    100
    >>> shoem.get_kingdom_licenses()
    ['Pythonia', 'Garthon']
    >>> shoem.sell('boots', 2)
    'shoemaker sold 2 of boots.'
    >>> shoem.get_stock()
    {'boots': [3, 10], 'sandals': [2, 3], 'heels': [1, 20]}
    >>> shoem.get_cash()
    120
    >>> shoem.restock('heels', 4)
    'shoemaker restocked 4 of heels.'
    >>> shoem.get_stock()
    {'boots': [3, 10], 'sandals': [2, 3], 'heels': [5, 20]}
    >>> shoem.travel_to_kingdom('Pythonia')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> pythonia = Kingdom('Pythonia')
    >>> shoem.travel_to_kingdom(pythonia)
    True
    >>> javatown = Kingdom('Javatown')
    >>> shoem.travel_to_kingdom(javatown)
    False
    >>> pythonia.get_name()
    'Pythonia'
    >>> assert isinstance(pythonia.get_curr_merchants(), list)
    >>> assert [isinstance(m, Merchant) for m in pythonia.get_curr_merchants()]
    >>> print(pythonia)
    Kingdom Pythonia has 1 active merchants.
    >>> blacksmith = Merchant('Blacksmith', {'hammers': [25, 5], \
    'nails': [90, 1]}, 10, ['Pythonia'])
    >>> blacksmith.get_id()
    2
    >>> pythonia.new_merchant(blacksmith)
    True
    >>> pythonia.get_total_cash()
    130

    >>> print(pythonia.promote_market())
    shoemaker sold 3 of boots. 
    shoemaker sold 2 of sandals. 
    shoemaker sold 5 of heels. 
    Blacksmith sold 25 of hammers. 
    Blacksmith sold 90 of nails. 
    <BLANKLINE>

    >>> len(pythonia.get_curr_merchants())
    2
    >>> pythonia.temp_ban(blacksmith)
    True
    >>> tailor = Merchant('tailor', {}, 10000, ['Pythonia'])
    >>> pythonia.temp_ban(tailor)
    False
    >>> len(pythonia.get_curr_merchants())
    1

    # Add your own doctests below
    >>> shoem.get_id()
    1
    >>> farmer = Merchant('Farmer', {'carrots': [100, 1], 'apples': [50, 2]}, \
    20, ['Pythonia', 'Javatown'])
    >>> print(farmer)
    Farmer has brought carrots, apples. They are able to sell their wares \
in Pythonia, Javatown.
    >>> c_land = Kingdom('C Land')
    >>> print(c_land)
    Kingdom C Land has 0 active merchants.
    >>> farmer.travel_to_kingdom(c_land)
    False
    >>> farmer.travel_to_kingdom(javatown)
    True
    >>> farmer.sell('carrots', 10)
    'Farmer sold 10 of carrots.'
    >>> farmer.get_cash()
    30
    >>> farmer.restock('carrots', 10)
    'Farmer restocked 10 of carrots.'
    >>> farmer.sell('apples', 25)
    'Farmer sold 25 of apples.'
    >>> farmer.restock('apples', 100)
    'Farmer restocked 100 of apples.'
    >>> print(c_land.promote_market())
    <BLANKLINE>
    >>> c_land.new_merchant(farmer)
    True
    >>> c_land.get_total_cash()
    80
    >>> print(c_land.promote_market())
    Farmer sold 100 of carrots. 
    Farmer sold 125 of apples. 
    <BLANKLINE>
    >>> c_land.get_total_cash()
    430
    >>> c_land.temp_ban('farmer')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> c_land.temp_ban(farmer)
    True
    
    >>> merchant = Merchant('Merchant', {'Excalibur': [1, 1000]}, 0, \
    ['C Land', 'Rust Town'])
    >>> rusttown = Kingdom('Rust Town')
    >>> merchant.travel_to_kingdom('Rust Town')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> merchant.travel_to_kingdom(rusttown)
    True
    >>> print(rusttown)
    Kingdom Rust Town has 1 active merchants.
    >>> merchant.sell('Excalibur', 1)
    'Merchant sold 1 of Excalibur.'
    >>> merchant.get_cash()
    1000
    >>> merchant.restock('Excalibur', 10)
    'Merchant restocked 10 of Excalibur.'
    >>> rusttown.temp_ban(merchant)
    True
    >>> rusttown.new_merchant('farmer')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> rusttown.new_merchant(farmer)
    True
    >>> rusttown.get_total_cash()
    430
    >>> print(rusttown.promote_market())
    Farmer sold 0 of carrots. 
    Farmer sold 0 of apples. 
    <BLANKLINE>
    """

class Merchant:
    """
    Implementation of a merchant
    """
    id_count = 0

    def __init__(
        self, merchant_type, stock, cash, kingdom_licenses
    ):
        """
        Constructor of Merchant

        Parameters:
        merchant_type (str): type of the merchant
        stock (dict): dictionary containing the merchant's products
        cash (int): amount of money the merchant has
        kingdom_licenses (list): list of kingdoms the merchant can sell in
        """
        # YOUR CODE GOES HERE #
        self.merchant_type = merchant_type
        self.stock = stock
        self.cash = cash
        self.kingdom_licenses = kingdom_licenses
        Merchant.id_count += 1
        self.id_count = Merchant.id_count

    def get_type(self):
        """ Getter for name attribute """
        # YOUR CODE GOES HERE #
        return self.merchant_type

    def get_stock(self):
        """ Getter for the stock attribute """
        # YOUR CODE GOES HERE #
        return self.stock

    def get_cash(self):
        """ Getter for cash attribute """
        # YOUR CODE GOES HERE #
        return self.cash

    def get_kingdom_licenses(self):
        """ Getter for kingdom_licenses attribute """
        # YOUR CODE GOES HERE #
        return self.kingdom_licenses
    
    def get_id(self):
        """ Getter for id attribute """
        # YOUR CODE GOES HERE #
        return self.id_count

    def __str__(self):
        """ String representation of Merchant """
        # YOUR CODE GOES HERE #
        return f'{self.merchant_type} has brought \
{', '.join(self.stock.keys())}. They are able to sell their wares in \
{', '.join(self.kingdom_licenses)}.'

    def sell(self, product, count):
        """
        Updates merchant's cash and product amount when a sale is completed
        """
        # YOUR CODE GOES HERE #
        if count > self.stock[product][0]:
            return f'{self.merchant_type} does not have enough {product} \
to sell.'
        else:
            self.stock[product][0] -= count
            self.cash += self.stock[product][1] * count
            return f'{self.merchant_type} sold {count} of {product}.'

    def restock(self, product, count):
        """
        Adds more product to the Merchant's stock for them to sell
        """
        # YOUR CODE GOES HERE #
        assert product in self.stock
        
        self.stock[product][0] += count
        return f'{self.merchant_type} restocked {count} of {product}.'

    def travel_to_kingdom(self, kingdom):
        """
        Returns a boolean indicating whether the merchant can travel to the 
        specified kingdom
        """
        # YOUR CODE GOES HERE #
        assert isinstance(kingdom, Kingdom)
        
        return kingdom.name in self.kingdom_licenses and \
            kingdom.new_merchant(self)

class Kingdom:
    """
    Implementation of a kingdom
    """

    # TODO: Add class attribute(s) here

    def __init__(self, name):
        """
        Constructor of Kingdom
        
        Parameters:
        name (str): name of the kingdom
        """
        # YOUR CODE GOES HERE #
        assert isinstance(name, str) and name != ''
        
        self.name = name
        self.curr_merchants = []

    def get_name(self):
        """ Getter of Kingdom's name """
        # YOUR CODE GOES HERE #
        return self.name

    def get_curr_merchants(self):
        """ Getter of current active merchants """
        # YOUR CODE GOES HERE #
        return self.curr_merchants

    def __str__(self):
        """ String representation of the kingdom """
        # YOUR CODE GOES HERE #
        return f'Kingdom {self.name} has {len(self.curr_merchants)} active \
merchants.'
    
    def new_merchant(self, merchant):
        """
        Adds a new merchant to the kingdom
        """
        # YOUR CODE GOES HERE #
        assert isinstance(merchant, Merchant)
        
        if merchant in self.curr_merchants:
            return False
        else:
            self.curr_merchants.append(merchant)
            return True
       
    def temp_ban(self, merchant):
        """
        Temporarilty bans a certain merchant
        """
        # YOUR CODE GOES HERE #
        assert isinstance(merchant, Merchant)
        
        if merchant in self.curr_merchants:
            self.curr_merchants.remove(merchant)
            return True
        else:
            return False

    def get_total_cash(self):
        """
        Returns the total amount of cash the merchants have
        """
        # YOUR CODE GOES HERE #
        return sum([m.get_cash() for m in self.curr_merchants])

    def promote_market(self):
        """
        Sell out every market in the kingdom
        """
        # YOUR CODE GOES HERE #
        out = ''
        for merch in self.curr_merchants:
            for item, info in merch.get_stock().items():
                out += merch.sell(item, info[0]) + ' \n'
        return out