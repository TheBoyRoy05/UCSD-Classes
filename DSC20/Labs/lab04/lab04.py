"""
DSC 20 Winter 2024, Lab 04
Name: Issac Roy
PID: A17787465 
Source: N/A
"""

# Question 1.1
def promotion(lst, points):
    """
    Adds points to each element in the given list using lambda/map.

    Args:
        lst: a list of players' points, each represented as an integer.
        points: an integer to be added to each player's points.

    Returns: the input list with points added to each element.

    >>> promotion([], 8)
    []
    >>> promotion([2, 8, 5], 2)
    [4, 10, 7]
    >>> promotion([9, 10, 21, 6], 0)
    [9, 10, 21, 6]
    """
    # YOUR CODE GOES HERE #
    return list(map(lambda x: x+points, lst))

# Question 1.2
def to_arena(signs):
    """
    Find which signs include the substring "laser tag" using lambda/filter.

    Args:
        signs: a list of sign names, each represented as a string.

    Returns: a list containing only the signs with the substring "laser tag".

    >>> to_arena(["laser tag ->", "<--- laser tag ^", "laser tag!"])
    ['laser tag ->', '<--- laser tag ^', 'laser tag!']
    >>> to_arena([])
    []
    >>> to_arena(["^ arcade", "<- laser tag!", "exit"])
    ['<- laser tag!']
    >>> to_arena(["exit", "arena ^", "exit", "<--- arcade"])
    []
    """
    # YOUR CODE GOES HERE #
    return list(filter(lambda x: x.count('laser tag') > 0, signs))

# Question 1.3
def to_arena2(signs):
    """
    Find which signs include the substring "laser tag" using lambda/map.

    Args:
        signs: a list of sign names, each represented as a string.

    Returns: a list containing None and/or sign names which include the 
    substring "laser tag".

    >>> to_arena2(["laser tag ->", "<--- laser tag ^", "laser tag!"])
    ['laser tag ->', '<--- laser tag ^', 'laser tag!']
    >>> to_arena2([])
    []
    >>> to_arena2(["^ arcade", "<- laser tag!", "exit"])
    [None, '<- laser tag!', None]
    >>> to_arena2(["exit", "arena ^", "exit", "<--- arcade"])
    [None, None, None, None]
    """
    # YOUR CODE GOES HERE #
    return list(map(lambda x: x if x.count('laser tag') > 0 else None, signs))

# Question 1.4
def to_arena3(signs):
    """
    Find which signs include the substring "laser tag" using lambda/filter.

    Args:
        signs: a list of sign names, each represented as a string or None.

    Returns: a list containing only the signs with the substring "laser tag".

    >>> to_arena3(["laser tag ->", "<--- laser tag ^", "laser tag!"])
    ['laser tag ->', '<--- laser tag ^', 'laser tag!']
    >>> to_arena3([])
    []
    >>> to_arena3([None, '<- laser tag!', None])
    ['<- laser tag!']
    >>> to_arena3([None, None, None, None])
    []
    """
    # YOUR CODE GOES HERE #
    return list(filter(None, signs))

# Question 2.1
def base_points(teams):
    """
    Identify if a team has any team members with 0 points.

    Args:
        teams: a dictionary where the keys are team names and the values are
        the team members' points.
    
    Returns: a list of tuples with the team name and 0 or 1.

    >>> teams = {"maps": [20, 89, 1], "filters": [5, 60]}
    >>> base_points(teams)
    [('maps', 1), ('filters', 1)]

    >>> teams = {"DSC10": [25, 70, 0], "DSC15": [0, 0, 10], "DSC20": [20, 35]}
    >>> base_points(teams)
    [('DSC10', 0), ('DSC15', 0), ('DSC20', 1)]
    """ 
    # YOUR CODE GOES HERE #
    return list(map(lambda pair: (pair[0], int(all(pair[1]))), teams.items()))

# Question 2.2
def unfortunate(teams, banned_word):
    """
    Return a list containing teams that don't have the banned_word in their 
    team name

    Args:
        teams: a dictionary where the keys are team names and the values are
        the team members' points.
    
    Returns: a list of team names that don't include the banned_word.

    >>> teams = {"maps": [20, 89, 1], "filters": [5, 60]}
    >>> banned_word = "map"
    >>> unfortunate(teams, banned_word)
    ['filters']
    >>> teams = {"DSC10": [25, 70, 0], "filter them out": [], "DSC20": [20, 35]}
    >>> banned_word = "FiLter"
    >>> unfortunate(teams, banned_word)
    ['DSC10', 'DSC20']
    >>> unfortunate({}, banned_word)
    []
    """
    # YOUR CODE GOES HERE #
    return list(filter(lambda x: x.count(banned_word.lower()) == 0, \
        teams.keys()))

# Question 3.1
def removed(teams, threshold):
    """
    Calculate how many players are left based on how many times they were hit
    compared to the threshold.

    Args:
        teams: a dictionary where the keys are team names and the values are
        the number of times each team member was hit.
        threshold: an integer representing the number of times a player can be 
        hit before they are eliminated.

    Returns: a list of tuples with the team name and the number of players left
    after elimination.

    >>> teams = {"team_maps": [0, 9, 4], "team_filters": [4, 7, 5, 1]}
    >>> removed(teams, 5)
    [('team_maps', 2), ('team_filters', 2)]

    >>> removed(teams, 10)
    [('team_maps', 3), ('team_filters', 4)]

    >>> removed(teams, 1)
    [('team_maps', 1), ('team_filters', 0)]
    """
    # YOUR CODE GOES HERE #
    return list(map(lambda pair: (pair[0], \
        len(list(filter(lambda x: x < threshold, pair[1])))), teams.items()))

# Question 3.2
def lost_tags(teams):
    """
    Disqualify any team where a team member lost their name tag.

    Args:
        teams: a dictionary where the keys are team names and the values are
        the status of their name tag ("still have" or "lost).

    Returns: a list of tuples with the team name, the number of lost name tags, 
    and whether or not the team was disqualified

    >>> teams = {"maps": ["still have", "lost"], "filters": ["still have", " still have"]}
    >>> lost_tags(teams)
    [('maps', 1, 'Disqualified'), ('filters', 0, 'Ok to continue!')]

    >>> teams = {"DSC10": ["lost", "lost", "lost"], "DSC15": [], "DSC20": ["still have"]}
    >>> lost_tags(teams)
    [('DSC10', 3, 'Disqualified'), ('DSC15', 0, 'Ok to continue!'), ('DSC20', 0, 'Ok to continue!')]
    """  
    # YOUR CODE GOES HERE #
    temp = map(lambda i: (i[0], \
        len(list(filter(lambda x: x == 'lost', i[1])))), teams.items())
    
    return list(map(lambda i: (i[0], i[1], \
        'Disqualified' if i[1] else 'Ok to continue!'), temp))

# Question 3.3
def eliminate(teams, rankings, elims):
    """
    Eliminate teams based on their rankings.

    Args:
        teams: a list of strings representing team names
        rankings: a list of integers representing each team's rankings
        elims: the number of teams to elminate
    
    Returns: a tuple containing teams that were not eliminated

    >>> teams = ["team1", "team2", "team3", "team4"]
    >>> rankings = [3, 2, 4, 1]
    >>> eliminate(teams, rankings, 1)
    ('team1', 'team2', 'team4')
    >>> eliminate(teams, rankings, 3)
    ('team4',)
    >>> eliminate(teams, rankings, 0)
    ('team1', 'team2', 'team3', 'team4')
    >>> eliminate([],[], 0)
    ()
    """
    # YOUR CODE GOES HERE #
    return tuple(filter(lambda x: x != 'ELIMINATED', \
        map(lambda team, rank: team if rank <= len(teams)-elims \
            else "ELIMINATED", teams, rankings)))