"""
DSC 20 Winter 2024 Homework 06
Name: Issac Roy
PID: A17787465
Source: N/A
"""

#Question 1
def reverse_str(name):
    """
    Reverses a given string using recursion

    >>> reverse_str('Lina')
    'aniL'
    >>> reverse_str('anna')
    'anna'
    >>> reverse_str('Hello World')
    'dlroW olleH'

    # Add your own doctests below
    >>> reverse_str('Pythonia')
    'ainohtyP'
    
    >>> reverse_str('Issac Roy')
    'yoR cassI'
    
    >>> reverse_str('')
    ''
    """
    return name if len(name) <= 1 else name[-1] + reverse_str(name[:-1])

#Question 2
def reverse_all(names_lst):
    """
    Reverses all the strings in the input using recursion

    >>> names_lst = ["Emma", "Liam", "Olivia", "Noah", "Ava"]
    >>> reverse_all(names_lst)
    ['ammE', 'maiL', 'aivilO', 'haoN', 'avA']
    >>> names_lst = ["William"]
    >>> reverse_all(names_lst)
    ['mailliW']
    >>> names_lst = ["Isabella", "Oliver", "Mia"]
    >>> reverse_all(names_lst)
    ['allebasI', 'revilO', 'aiM']

    # Add your own doctests below
    >>> reverse_all([])
    []
    >>> reverse_all(['', '', ''])
    ['', '', '']
    >>> reverse_all(['ainohtyP', 'si', 'driew'])
    ['Pythonia', 'is', 'weird']
    """
    return [reverse_str(names_lst[0])] + reverse_all(names_lst[1:]) \
        if len(names_lst) > 0 else []

#Question 3
def num_tables(total_ppl, table_size=4):
    """
    Returns the number of tables needed for a certain amount of people and a \
given table size.

    >>> num_tables(35)
    9
    >>> num_tables(20, 2)
    10
    >>> num_tables(2, 20)
    1

    # Add your own doctests below
    >>> num_tables(0, 1)
    0
    >>> num_tables(10, 1)
    10
    >>> num_tables(10, 100)
    1
    """
    return 1 + num_tables(total_ppl-table_size, table_size) \
        if total_ppl > 0 else 0

#Question 4
def orders(price_lst, order_size=3):
    """
    Returns the prices of given orders in groups of order size

    >>> orders([2, 2, 2, 4, 4, 4])
    [6, 12]
    >>> orders([])
    []
    >>> orders([2, 2, 2, 2])
    [6, 2]

    # Add your own doctests below
    >>> orders([0, 0, 0])
    [0]
    >>> orders([0, 0, 0, 100])
    [0, 100]
    >>> orders([0, 0, 0, 100], 4)
    [100]
    """
    if len(price_lst) > order_size:
        return [sum(price_lst[:order_size])] + \
            orders(price_lst[order_size:], order_size)
    elif len(price_lst) > 0:
        return [sum(price_lst)] 
    else: 
        return []

#Question 5
def confuse(reminder_str):
    """
    Given a string, returns another string where every time a word has 2 of \
the same characters consecutively, the second character is replaced with *.

    >>> confuse('book')
    'bo*k'
    >>> confuse('successful')
    'suc*es*ful'
    >>> confuse('')
    ''

    # Add your own doctests below
    >>> confuse('boook')
    'bo*ok'
    >>> confuse('boooook')
    'bo*o*ok'
    >>> confuse('sucCessful')
    'sucCes*ful'
    """
    rem = reminder_str
    skip_char = 2
    if len(rem) > 1:
        if rem[0] == rem[1]:
            return rem[0] + '*' + confuse(rem[skip_char:])
        else:
            return rem[0] + confuse(rem[1:])
    else:
        return rem

#Question 6
def seating_chart(group_sizes, table_sizes):
    """
    Returns the number of tables that don't have enough seats for its \
corresponding group. The two input lists don't have to be the same length.

    >>> seating_chart([3, 3, 3], [4, 4, 4])
    0
    >>> seating_chart([2, 3, 4, 5], [3, 3, 3])
    2
    >>> seating_chart([2, 2], [])
    2

    # Add your own doctests below
    >>> seating_chart([], [2, 2])
    0
    >>> seating_chart([], [])
    0
    >>> seating_chart([2, 2], [3, 3, 3, 3])
    0
    """
    if len(table_sizes) != 0 and len(group_sizes) != 0:
        return (group_sizes[0] > table_sizes[0]) + \
            seating_chart(group_sizes[1:], table_sizes[1:])
    else:
        return len(group_sizes)

#Question 7
def allergens(ingredients, item_to_remove):
    """
    Removes all the allergens from ingredients and returns the rest of the \
list in reverse order.

    >>> allergens(["Sugar", "Jam", "Honey", "Honey"], "Honey")
    ['Jam', 'Sugar']
    >>> allergens(["Kefir", "", "Juice", "Water", "Milk"], "milk")
    ['Water', 'Juice', '', 'Kefir']
    >>> allergens(["Pecans", "PECANS", "PeCANS"], "Pecans")
    []
 
    # Add your own doctests below
    >>> allergens([], 'milk')
    []
    >>> allergens(['', '', ''], 'milk')
    ['', '', '']
    >>> allergens(["Kefir", "MILK", "mIlK", "Water", "Milk"], "milk")
    ['Water', 'Kefir']
    """
    if len(ingredients) > 0:
        if ingredients[0].lower() == item_to_remove.lower():
            return allergens(ingredients[1:], item_to_remove)
        else:
            return allergens(ingredients[1:], item_to_remove) + \
                [ingredients[0]]
    else:
        return []