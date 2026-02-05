"""
DSC 20 Fall 2023 Homework 08
Name: TODO
PID: TODO
Source: TODO
"""

# Question 1
def q1_doctests():
    """
    Doctests for ImaginaryParty, ArtsAndCrafts, PythoniaGastronomicAdventure

    >>> party = ImaginaryParty("Alice", "Mansion", "8:00 PM")
    >>> party.host_name
    'Alice'
    >>> party.generate_party_info("Music", "Dance floor")
    'Party details: Music, Dance floor'
    >>> ImaginaryParty.party_fact()
    'The limits of this party are up to your imagination!'
    >>> print(party)
    Host: Alice, Location: Mansion, Start Time: 8:00 PM

    >>> arts_and_crafts = ArtsAndCrafts("Bob", "Club", "9:30 PM")
    >>> ArtsAndCrafts.theme
    'Arts and Crafts'
    >>> arts_and_crafts.supplies
    3
    >>> arts_and_crafts.invite()
    Host: Bob, Location: Club, Start Time: 9:30 PM
    >>> arts_and_crafts.invite()
    Host: Bob, Location: Club, Start Time: 9:30 PM
    >>> arts_and_crafts.invite()
    Host: Bob, Location: Club, Start Time: 9:30 PM
    >>> arts_and_crafts.invite()
    'Not enough supplies'

    >>> adventure = PythoniaGastronomicAdventure("John", "Forest", "5:30 PM")
    >>> PythoniaGastronomicAdventure.theme
    'Gastronomic Adventure'
    >>> print(adventure.generate_party_info("Bonfire", "Dancing"))
    Allergy Warning!
    Party details: Bonfire, Dancing
    """
    return


class ImaginaryParty:
    """
    Implementation of the ImaginaryParty class.
    """

    def __init__(self, host_name, location, start_time):
        """
        Initialize an ImaginaryParty object.

        Args:
        - host_name (str): Name of the party host.
        - location (str): Location of the party.
        - start_time (str): Start time of the party.
        """
        return

    def generate_party_info(self, *details):
        """
        Generate party information based on provided details.

        Args:
        - *details (str): Variable number of party details.
        """
        return

    #@ TODO: static method
    def party_fact():
        """
        Return a fun party fact.
        """
        return

    def __str__(self):
        """
        Return string representation of ImaginaryParty object.
        """
        return


class ArtsAndCrafts(ImaginaryParty):
    """
    Implementation of the ArtsAndCrafts class, inheriting from ImaginaryParty.
    """

    def invite(self):
        """
        Invite a guest to the ArtsAndCrafts party if supplies are available.
        """
        return

    #@ TODO: class method
    def get_remaining_spots(cls):
        """
        Calculate the remaining spots available at the ArtsAndCrafts party.
        """
        return


class PythoniaGastronomicAdventure(ImaginaryParty):
    """
    Implementation of the PythoniaGastronomicAdventure class.
    Inherits from ImaginaryParty.
    """

    def generate_party_info(self, *party_details):
        """
        Generate party information for the Gastronomic Adventure Party.

        Args:
        - *party_details (str): Variable number of party details.
        """
        # party_details is a tuple, but generate_party_info expects multiple
        # inputs, so we use the unpacking operator
        return


# Question 2
def q2_doctests():
    """
    Doctests for Firework and subclasses (Firecracker and Skyrocket)

    >>> firework = Firework("Phantom")
    >>> firecracker = Firecracker("Boom Town")
    >>> roman_candle = RomanCandle("Showtime")
    >>> firework.launch()
    'The Phantom firework was launched and it was a successful launch. \
It created 150 decibels of noise.'
    >>> firework.noise_made
    150
    
    >>> print(firecracker.launch_several(4))
    The Boom Town firework was launched and it was a successful launch. \
It created 150 decibels of noise.
    The Boom Town firework was launched and it was a dud launch. \
It created 30 decibels of noise.
    The Boom Town firework was launched and it was a successful launch. \
It created 150 decibels of noise.
    The Boom Town firework was launched and it was a dud launch. \
It created 30 decibels of noise.
    >>> firecracker.noise_made
    360
    >>> print(firecracker.calculate_complaints())
    Received 1 new noise complaints.
    >>> firecracker.noise_complaints
    1
    >>> print(firecracker.calculate_complaints())
    No new complaints!

    >>> print(roman_candle.launch_several(4))
    The Showtime firework was launched and it was a successful launch. \
It created 150 decibels of noise.
    The Showtime firework was launched and it was a dud launch. \
It created 30 decibels of noise.
    The Showtime firework was launched and it was a successful launch. \
It created 150 decibels of noise.
    The Showtime firework was launched and it was a dud launch. \
It created 30 decibels of noise.
    >>> roman_candle.calculate_complaints()
    'Received 1 new noise complaints.'
    >>> roman_candle.noise_complaints
    1
    >>> roman_candle.noise_made
    360
    >>> roman_candle.cops_called
    0
    >>> test = roman_candle.launch_several(10)
    >>> print(roman_candle.calculate_complaints())
    COPS CALLED!!
    Received 4 new noise complaints.
    >>> test = roman_candle.launch_several(8)
    >>> print(roman_candle.calculate_complaints())
    Received 2 new noise complaints.
    >>> roman_candle.noise_complaints
    7
    """
    return


class Firework:
    """
    Implementation of the base Firework class
    """

    def __init__(self, brand):
        """ Constructor """
        return

    def launch(self):
        """
        Launch a firework, updates noise_made and returns string
        """
        return

    def launch_several(self, amount):
        """
        Launches fireworks `amount` of times, returns the full string
        """
        return


class Firecracker(Firework):
    """
    Implementation of the Firecracker class
    """

    def __init__(self, brand):
        """ Constructor, set initial brightness """
        return

    def calculate_complaints(self):
        """
        Calculates the number of noise complaints received
        """
        return

        
class RomanCandle(Firecracker):
    """
    Implementation of the RomanCandle class
    """

    def __init__(self, brand):
        """ Constructor, set initial brightness """
        return

    def calculate_complaints(self):
        """ Returns a message describing the number of complaints """
        return


# Question 3 
# Question 3.1
def create_raffle_tix(letters, numbers):
    """
    Concatenate all of the elements in `letters` with each element in
    `numbers` and return the values in a list

    >>> create_raffle_tix(["A", "B", "C"], ["1", 2, "3"])
    ['A1', 'A3', 'B1', 'B3', 'C1', 'C3']
    >>> create_raffle_tix([], [])
    []
    >>> create_raffle_tix(["X", None, "Y"], ["1", 2, [3]])
    ['X1', 'Y1']
    """
    tickets = []
    for letter in letters:
        for number in numbers:
            tickets.append(letter + number)  # add try-except
    return tickets


# Question 3.2
def special_requests(*filepaths):
    """
    Open all of the files in `filepaths` and PRINT a string for each file
    that indicates if this file can be opened or not

    >>> special_requests('files/vegetarian.txt', 'files/b.txt', 'files/c.txt')
    files/vegetarian.txt opened successfully
    files/b.txt not found
    files/c.txt not found

    >>> special_requests('random.txt')
    random.txt not found
    """
    for filepath in filepaths:
        cur_file = open(filepath, "r")  # add try-except
        cur_file.close()
        

# Question 3.3
def create_placards(first_names, last_names):
    """
    For each element in `first_names`, add it with its corresponding element
    in `last_names`. Returns all of the combined names in a list

    >>> create_placards(["cj", "tank", "nico", "dalton"], ["stroud", "dell"])
    <class 'IndexError'>
    <class 'IndexError'>
    ['cj stroud', 'tank dell']

    >>> create_placards(["brock", "george", "brandon"], [None, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []
    
    >>> create_placards([], [])
    []
    """
    names = []
    for i in range(len(first_names)):
        names.append(first_names[i] + " " + last_names[i]) # add try-except
    return names


# Question 4
def validate_resolution(resolution, commitments):
    """
    >>> resolution = 'Exercise regularly'
    >>> commitments = ['I commit to run twice a week', \
                       'I commit to go to the gym every day']
    >>> validate_resolution(resolution, commitments)
    'New Years resolution validated'
    >>> validate_resolution(resolution, ['Funny joke'])
    Traceback (most recent call last):
    ...
    ValueError: commitment does not start with 'I commit to'
    >>> validate_resolution(resolution, 1)
    Traceback (most recent call last):
    ...
    TypeError: commitments is not a list
    >>> validate_resolution('', [1, 2, 'hi'])
    Traceback (most recent call last):
    ...
    TypeError: resolution is empty
    >>> validate_resolution('Hello', ['hi', 2, 'hi'])
    Traceback (most recent call last):
    ...
    TypeError: non-string item in commitments at index 1
    >>> validate_resolution('hi', [])
    Traceback (most recent call last):
    ...
    TypeError: commitments is empty
    >>> validate_resolution('1: idk', [])
    Traceback (most recent call last):
    ...
    ValueError: non-alpha character in resolution
    >>> validate_resolution(False, 0)
    Traceback (most recent call last):
    ...
    TypeError: resolution is not a string

    # Add your own doctests below
    """
    return


# Question 5 (Extra Credit)
def flatten(nested_input):
    """
    Takes in a nested input of lists and tuples and flattens the nested input.
    The flattened output should be a list that only contains the integers
    that were present in the input.

    >>> flatten([1, (2, "Hi"), [4, (5.1, 6)], 7, [(8, 9), 10]])
    [1, 2, 4, 6, 7, 8, 9, 10]
    >>> flatten([3.5, ("Hello", 2), [5, (6.2, "World")], 8, [(9, 10), "11"]])
    [2, 5, 8, 9, 10]
    >>> flatten([(1.1, "A"), [2, (3.3, "B", 4)], 5, ("C", 6, [7, "D"]), 8.8])
    [2, 4, 5, 6, 7]
    """
    return
