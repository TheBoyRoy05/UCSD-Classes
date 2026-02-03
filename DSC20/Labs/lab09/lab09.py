"""
DSC 20 Winter 2024 Lab 09
Name: Issac Roy
PID: A17787465
Source: N/A
"""

# Utility data structures
landscapes = ['Return vs Print', 'Dictionaries', 'Files', 'List Comprehension',
              'Lambda Functions', 'Iterators', 'Complexity', 
              'Scope of variables', 'Classes and Objects', 'Inheritance', 
              'Special Methods','Mutable data']
num_landscapes = 12

# Question 1
def admission_checker(xp_levels):
    """
    Checks necessary conditions for admission into Javania. Raise an exception
    when condition check fails. If all necessary conditions pass, evaluate
    capability to survive in Javania -- return True if it passes 
    and False otherwise.

    >>> xp_levels = {'Return vs Print': 20, 'Dictionaries': 20, 'Files': 20,\
        'List Comprehension': 20, 'Lambda Functions': 20, 'Iterators': 20,\
        'Complexity': 20, 'Scope of variables': 20, 'Classes and Objects': 20,\
        'Inheritance': 20, 'Special Methods': 20, 'Sorting': 20}
    >>> admission_checker(xp_levels)
    Traceback (most recent call last):
    ...
    KeyError: 'Landscape Sorting does not exist in Pythonia!'
    >>> xp_levels = {'Return vs Print': 20, 'Dictionaries': 20, 'Files': 20,\
        'List Comprehension': 20, 'Lambda Functions': 20, 'Iterators': 20,\
        'Complexity': 20, 'Scope of variables': 20, 'Classes and Objects': 20,\
        'Inheritance': 20, 'Special Methods': 20, ('Mutable data',): 20}
    >>> admission_checker(xp_levels)
    Traceback (most recent call last):
    ...
    TypeError: Landscape is represented in a wrong way!
    >>> xp_levels = {'Return vs Print': 20, 'Dictionaries': 20, 'Files': 20,\
        'List Comprehension': 10, 'Lambda Functions': 10, 'Iterators': 10,\
        'Complexity': 10, 'Scope of variables': 10, 'Classes and Objects': 10,\
        'Inheritance': 10, 'Special Methods': 10, 'Mutable data': 10}
    >>> admission_checker(xp_levels)
    False
    >>> xp_levels = {'Return vs Print': 20, 'Dictionaries': 20, 'Files': 20,\
        'List Comprehension': 20, 'Lambda Functions': 20, 'Iterators': 20,\
        'Complexity': 20, 'Scope of variables': 20, 'Classes and Objects': 20,\
        'Inheritance': 20, 'Special Methods': 20, 'Mutable data': 20}
    >>> admission_checker(xp_levels)
    True
    """
    # YOUR CODE GOES HERE #
    if not isinstance(xp_levels, dict):
        raise TypeError('Survey result is represented in a wrong way!')
    if not all([isinstance(landscape, str) for landscape in xp_levels.keys()]):
        raise TypeError('Landscape is represented in a wrong way!')
    for key, level in xp_levels.items():
        if not isinstance(level, int):
            raise TypeError(f'Experience level for {key} is represented in a wrong way!')
        if level%10 != 0:
            raise ValueError(f'Experience level for {key} is incorrectly entered!')
    for land in xp_levels.keys():
        if land not in landscapes:
            raise KeyError(f'Landscape {land} does not exist in Pythonia!')
    if len(xp_levels) < 6:
        raise KeyError('You miss too many Pythonia landscapes!')
    return len(xp_levels) > 8 and sum([val for val in xp_levels.values()])/len(xp_levels) >= 20

# Question 2
class Javanian():
    '''
    Implementation of a Player in Javania.

    >>> kate = Javanian({'LinkedLand': 20, 'QueueChannel': 10,\
            'Stack Sand Dunes': 50})
    >>> jim = Javanian({'Javalake': 20, 'Interface Canyon': 10,\
            'this.valley': 30, 'BST': 40})
    >>> gabi = Javanian({'LinkedLand': 30, 'Disjoint Forest': 40})
    >>> gabi
    LinkedLand, Disjoint Forest
    >>> print(gabi)
    I visited 2 places and have a total of 70 XP points.
    >>> jim
    Interface Canyon, Javalake, this.valley, BST
    >>> print(jim)
    I visited 4 places and have a total of 100 XP points.
    >>> kate
    QueueChannel, LinkedLand, Stack Sand Dunes
    >>> print(kate)
    I visited 3 places and have a total of 80 XP points.
    >>> gabi > 100
    False
    >>> jim > kate
    True
    >>> kate > gabi
    True
    >>> len(gabi)
    2
    >>> len(jim)
    4
    >>> len(kate)
    3
    '''
    # Question 2.1 (Initialization)
    # YOUR CODE GOES HERE #
    def __init__(self, locations):
        self.locations = locations
    
    # Question 2.2 (String Representations)
    # YOUR CODE GOES HERE #
    def __str__(self):
        return f'I visited {len(self.locations)} places and have a total of \
{sum([val for val in self.locations.values()])} XP points.'
        
    def __repr__(self) -> str:
        return ', '.join(sorted(self.locations, key=self.locations.get))
    
    # Question 2.3 (Greater than Method)
    # YOUR CODE GOES HERE #
    def __gt__(self, xp):
        my_xp = sum([val for val in self.locations.values()])
        if isinstance(xp, int):
            return my_xp > xp
        else:
            return my_xp > sum([val for val in xp.locations.values()])
    
    # Question 2.4 (Length Method)
    # YOUR CODE GOES HERE #
    def __len__(self):
        return len(self.locations)
    