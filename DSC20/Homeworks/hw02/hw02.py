"""
DSC 20 Winter 2024 Homework 02
Name: Issac Roy
PID: A17787465
Source: \
https://www.geeksforgeeks.org/python-difference-between-sorted-and-sort/
"""

# Question 1
def valid_pairs(keys, values):
    """
    Creates tuples of key value pairs if the key is a valid immutable type

    >>> keys = ["fun", ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not valid',)]

    >>> keys = [1, "fun", [2], (1,), {}]
    >>> values = [1, {}, (1,), "island", [2]]
    >>> valid_pairs(keys, values)
    [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'), ('not valid',)]

    >>> keys = []
    >>> values = []
    >>> valid_pairs(keys, values)
    []

    # Add at least 3 doctests below here #
    >>> keys = [{'a': 'b'}, 10.0]
    >>> values = ['Python bad', 'Pythonia']
    >>> valid_pairs(keys, values)
    [('not valid',), (10.0, 'Pythonia')]
    
    >>> keys = [{'a', 'b'}, 'We are in:']
    >>> values = ['Python good', 'Pythonia']
    >>> valid_pairs(keys, values)
    [('not valid',), ('We are in:', 'Pythonia')]
    
    >>> keys = [(0, 0), (1, 1)]
    >>> values = ['He He', 'Ha Ha']
    >>> valid_pairs(keys, values)
    [((0, 0), 'He He'), ((1, 1), 'Ha Ha')]
    """
    # YOUR CODE GOES HERE #
    out = []
    for key, value in zip(keys, values):
        if isinstance(key, list) or isinstance(key, set) \
        or isinstance(key, dict):
            out += [('not valid',)]
        else:
            out += [(key, value)]
    return out

# Question 2
def tup_to_dict(tuples):
    """
    Creates a dictionary of lists from the valid tuples provided

    >>> lst = [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'),\
    ('not valid',)]
    >>> tup_to_dict(lst)
    {1: [1], 'fun': [{}], (1,): ['island']}

    >>> lst = [("not valid",), ("tree", "green"), ("tree", "blue"),\
    (1, ["key"])]
    >>> tup_to_dict(lst)
    {'tree': ['green', 'blue'], 1: [['key']]}

    # Add at least 3 doctests below here #
    >>> tup_to_dict([(1, 'yes'), (1.0, 'no'), (2, 'maybe')])
    {1: ['yes', 'no'], 2: ['maybe']}
    
    >>> tup_to_dict([('not valid',), ('not valid',), ('not valid',)])
    {}
    
    >>> tup_to_dict([((0, 0), 'gold'), ((1, 1), {'Day 0': 'HELP'})])
    {(0, 0): ['gold'], (1, 1): [{'Day 0': 'HELP'}]}
    """
    # YOUR CODE GOES HERE #
    out = dict()
    for tuple in tuples:
        if tuple[0] == 'not valid':
            continue
        if tuple[0] in out:
            out[tuple[0]] += [tuple[1]]
        else:
            out[tuple[0]] = [tuple[1]]
    return out

# Question 3
def foods(items, prices):
    """
    Creates a dictionary comparing the average prices of 2 food items
    The average will be 0 if there are no prices to compare

    >>> items = ["Ziblo","Crinx"]
    >>> prices = [[1, 2], [3, 4], [5, 6]]
    >>> foods(items, prices)
    {'Ziblo': 3.0, 'Crinx': 4.0}

    >>> items = ["Yumzo","Fluzu"]
    >>> prices = [[2, 3], [3, 4], [4, 5], [5, 6.2]]
    >>> foods(items, prices)
    {'Yumzo': 3.5, 'Fluzu': 4.55}

    # Add at least 3 doctests below here #
    >>> items = ["Ziblo", "Fluzu"]
    >>> prices = []
    >>> foods(items, prices)
    {'Ziblo': 0, 'Fluzu': 0}
    
    >>> items = ["Yumzo", "Crinx"]
    >>> prices = [[1, 100], [2, 200], [0.5, 50]]
    >>> foods(items, prices)
    {'Yumzo': 1.17, 'Crinx': 116.67}
    
    >>> items = ["Ziblo", "Yumzo"]
    >>> prices = [[20, 0], [13, 0], [16, 100]]
    >>> foods(items, prices)
    {'Ziblo': 16.33, 'Yumzo': 33.33}
    """
    # YOUR CODE GOES HERE #
    out = {items[0]: 0, items[1]: 0}
    sum0, sum1 = 0, 0
    round2 = 2
    for price0, price1 in prices:
        sum0 += price0
        sum1 += price1
    if len(prices):
        out[items[0]] = round(sum0/len(prices), round2)
        out[items[1]] = round(sum1/len(prices), round2)
    return out

# Question 4
def total_cost(items_you_have, ingredients):
    """
    Returns the total cost of the ingredients in items you have

    >>> items = {'Yumzo': 3.5, 'Fluzu': 4.55}
    >>> ingredients = ['Yumzo', 'Fluzu']
    >>> total_cost(items, ingredients)
    8.05

    >>> items = {'Yumzo': 3.5, 'Fluzu': 4.55}
    >>> ingredients = ['Ziblo','Yumzo', 'Fluzu']
    >>> total_cost(items, ingredients)
    8.05

    >>> items = {'Yumzo': 3.5, 'Fluzu': 4.55, 'Crinx': 5.34}
    >>> ingredients = ['Ziblo','Yumzo']
    >>> total_cost(items, ingredients)
    3.5

    # Add at least 3 doctests below here #
    >>> items = {'Ziblo': 3.5, 'Fluzu': 4.55}
    >>> ingredients = ['Yumzo', 'Crinx']
    >>> total_cost(items, ingredients)
    0
    
    >>> items = {'Yumzo': 11.11, 'Fluzu': 1000}
    >>> ingredients = ['Yumzo', 'Ziblo']
    >>> total_cost(items, ingredients)
    11.11
    
    >>> items = {'Yumzo': 3.5, 'Crinx': 0.1, 'Fluzu': 4.55, 'Ziblo': 10.2}
    >>> ingredients = ['Crinx', 'Yumzo', 'Ziblo', 'Fluzu']
    >>> total_cost(items, ingredients)
    18.349999999999998
    """
    # YOUR CODE GOES HERE #
    out = 0
    for ingredient in ingredients:
        if ingredient in items_you_have:
            out += items_you_have[ingredient]
    return out

# Question 5
def shopping(grocery_bag):
    """
    Returns a list of unique items in your grocery bad

    >>> bag = {'shop1': ['Munchi', 'Chirp'], 'shop2': ['Blipz', 'Sprova']}
    >>> shopping(bag)
    ['Blipz', 'Chirp', 'Munchi', 'Sprova']
    >>> bag = {'shop1': ['Munchi', 'Chirp'], 'shop2': ['Munchi', 'Sprova']}
    >>> shopping(bag)
    ['Chirp', 'Munchi', 'Sprova']
    >>> bag = {'shop1': ['Munchi', 'Chirp', 'Blipz'], \
    'shop2': ['Munchi', 'Sprova', 'Sprova'], \
    'shop3': ['Blipz', 'Sprova', 'Eggs']}
    >>> shopping(bag)
    ['Blipz', 'Chirp', 'Eggs', 'Munchi', 'Sprova']

    # Add at least 3 doctests below here #
    >>> bag = {}
    >>> shopping(bag)
    []
    
    >>> bag = {'shop1': [], 'shop2': []}
    >>> shopping(bag)
    []
    
    >>> bag = {'shop1': ['Eggs', 'Eggs'], 'shop2': ['Eggs', 'Eggs'], \
    'shop3': ['Eggs', 'Eggs', 'Eggs', 'Eggs']}
    >>> shopping(bag)
    ['Eggs']
    """
    # YOUR CODE GOES HERE #
    out = []
    for items in grocery_bag.values():
        out += items
    return sorted(list(set(out)))

# Question 6.1
def count_lines_1(filepath):
    """
    Returns the number of lines in a file given its filepath

    >>> count_lines_1('files/test1.txt')
    6
    >>> count_lines_1('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    >>> count_lines_1('files/bridges1.txt')
    4
    >>> count_lines_1('files/bridges2.txt')
    2
    >>> count_lines_1('files/bridges3.txt')
    4
    """
    # YOUR CODE GOES HERE #
    with open(filepath, 'r') as f_in:
        count = 0
        for line in f_in:
            count += 1
        return count

# Question 6.2
def count_lines_2(filepath):
    """
    Returns the number of lines in a file given its filepath

    >>> count_lines_2('files/test1.txt')
    6
    >>> count_lines_2('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    >>> count_lines_2('files/bridges1.txt')
    4
    >>> count_lines_2('files/bridges2.txt')
    2
    >>> count_lines_2('files/bridges3.txt')
    4
    """
    # YOUR CODE GOES HERE #
    with open(filepath, 'r') as f_in:
        return len(f_in.read().split('\n'))

# Question 6.3
def count_lines_3(filepath):
    """
    Returns the number of lines in a file given its filepath

    >>> count_lines_3('files/test1.txt')
    6
    >>> count_lines_3('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    >>> count_lines_3('files/bridges1.txt')
    4
    >>> count_lines_3('files/bridges2.txt')
    2
    >>> count_lines_3('files/bridges3.txt')
    4
    """
    # YOUR CODE GOES HERE #
    with open(filepath, 'r') as f_in:
        return len(f_in.readlines())

# Question 7
def emails(filepath):
    """
    Returns all of the emails in the file found at filepath

    >>> emails('files/file1.txt')
    ['milo@pythonia.py', 'ben@discussion.py', 'bryce@gradescope.py']
    >>> emails('files/file2.txt')
    ['milo@pythonia.py', 'ben@discussion.py', 'bryce@gradescope.py', \
'dave@gmail.com']
    >>> emails('files/file3_empty.txt')
    []

    # Add at least 3 doctests below here #
    >>> emails('files/bridges1.txt')
    []
    
    >>> emails('files/test1.txt')
    []
    
    >>> lines = ['issac,roy,10,issacroy@pythonia.py,1000']
    >>> file = open('files/my_file.txt', 'w')
    >>> file.writelines(lines)
    >>> file.close()
    >>> emails('files/my_file.txt')
    ['issacroy@pythonia.py']
    """
    # YOUR CODE GOES HERE #
    with open(filepath, 'r') as f_in:
        out = []
        email_pos = 3
        for line in f_in:
            pieces = line.strip().split(',')
            if len(pieces) > email_pos + 1:
                out.append(pieces[email_pos])
        return out

# Question 8
def counter(filepath_to_fix):
    """
    Converts a given filepath to a valid one and writes the number of digits
    and non digits in the filepath to the file at the filepath

    >>> counter('list123')
    >>> with open('files/list123.txt', 'r') as outfile1:
    ...    print(outfile1.read().strip())
    3
    4
    >>> counter('one1two2three3')
    >>> with open('files/one1two2three3.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    3
    11
    >>> counter('tricky ')
    >>> with open('files/tricky.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    7

    # Add at least 3 doctests below here #
    >>> counter('PYTH0N1A    ')
    >>> with open('files/PYTH0N1A.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    2
    10
    
    >>> counter('0')
    >>> with open('files/0.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    1
    0
    
    >>> counter('0 - 0')
    >>> with open('files/0 - 0.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    2
    3
    """
    # YOUR CODE GOES HERE #
    digits, non_digits = 0, 0
    for c in filepath_to_fix:
        if c.isnumeric():
            digits += 1
        else:
            non_digits += 1
    
    with open(f'files/{filepath_to_fix.strip()}.txt', 'w') as f_out:
        f_out.write(f'{digits}\n')
        f_out.write(f'{non_digits}\n')

# Question 9
def combine_bridges(bridges):
    """
    Creates a new file (combined_brides) with the total number of crossings
    for each unique bridge

    >>> combine_bridges('files/bridges1.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge1:9
    bridge2:3
    bridge3:1

    >>> combine_bridges('files/bridges2.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge1:5
    bridge2:0

    >>> combine_bridges('files/bridges3.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge2:3
    bridge3:1
    bridge1:5

    # Add at least 3 doctests below here #
    
    >>> bridges = ['bridge1:1\\n', 'fire_bridge:10\\n', 'water_bridge:100']
    >>> file = open('files/my_bridges1.txt', 'w')
    >>> file.writelines(bridges)
    >>> file.close()
    >>> combine_bridges('files/my_bridges1.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge1:1
    fire_bridge:10
    water_bridge:100
    
    >>> bridges = ['bridge1:1\\n', 'fire_bridge:10\\n', \
'water_bridge:100\\n', 'water_bridge:2\\n', 'bridge1:1000']
    >>> file = open('files/my_bridges2.txt', 'w')
    >>> file.writelines(bridges)
    >>> file.close()
    >>> combine_bridges('files/my_bridges2.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge1:1001
    fire_bridge:10
    water_bridge:102
    
    >>> bridges = ['the_best_bridge:9999999\\n', 'the_best_bridge:1']
    >>> file = open('files/my_bridges3.txt', 'w')
    >>> file.writelines(bridges)
    >>> file.close()
    >>> combine_bridges('files/my_bridges3.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    the_best_bridge:10000000
    """
    # YOUR CODE GOES HERE #
    info_dict = dict()
    with open(bridges, 'r') as f_in:
        for line in f_in:
            info = line.strip().split(':')
            if info[0] in info_dict:
                info_dict[info[0]] += int(info[1])
            else:
                info_dict[info[0]] = int(info[1])   
                            
    with open('files/combined_bridges.txt', 'w') as f_out:
        lines = []
        for key, value in info_dict.items():
            lines += [f'{key}:{value}\n']
        f_out.writelines(lines)