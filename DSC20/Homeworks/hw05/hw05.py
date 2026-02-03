"""
DSC 20 Winter 2024 Homework 05
Name: Issac Roy
PID: A17787465 
Source: N/A
"""
# Question 1
def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function. No new doctests required.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (True/False) #
    return [True, False, True, False, False, False, False, False, True, True]

# Question 2
def complexity_mc():
    """
    Write your answers to time complexity multiple-choice questions in this
    function. No new doctests required.
    
    >>> answers = complexity_mc()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    15
    >>> all([isinstance(ans, int) and 1 <= ans <= 10 for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (1-10, duplicates allowed) #
    return [1, 6, 4, 5, 4, 7, 1, 7, 7, 3, 2, 4, 6, 10, 7]

# Problem 3
def decipher_text(key1, key2, key3):
    """
    Returns a decoder which decodes a given string based on 3 keys
    
    Args:
        key1: one letter string
        key2: one letter string
        key3: one letter string

    >>> decipher_text('Q', 'b', 'C')('bNswqR')
    'answer'
    >>> decipher_text('W', 'J', 'Z')('TESTYJZRCJDE')
    'testyourcode'
    >>> decipher_text('W', 'J', 'Z')('ONWTWST')
    'onetest'
    >>> decipher_text('D', 's', 'c')('')
    ''

    # Add at least 3 doctests below here #
    >>> decipher_text('b', 'c', 'Z')('WCW Is thBs rBgHt')
    'wow is this right'
    >>> decipher_text('W', 'J', 'Z')('OJGA BOJGA')
    'ooga booga'
    >>> decipher_text('c', 'x', 'd')('PYthOnIa')
    'pythonia'
    """
    # YOUR CODE GOES HERE #
    def decoder(input):
        """
        Decodes the input by replacing the 3 given keys with vowels
        """
        input = input.lower()
        out = []
        for i in range(len(input)):
            if input[i] == key1.lower():
                if i%2 == 1:
                    out.append('i')
                else:
                    out.append('e')
            elif input[i] == key2.lower():
                if i%2 == 1:
                    out.append('o')
                else:
                    out.append('a')
            elif input[i] == key3.lower():
                out.append('u')
            else:
                out.append(input[i])
        return ''.join(out)
    return decoder
  
# Problem 4
def grade_calculator(w1, w2):
    """
    Given 2 weights for 2 categories, returns two grade calculators, one \
which calculates your number grade and one that calculates your letter grade

    Args:
        w1: weight for category one
        w2: weight for category two
        
    Returns:
        num_calc: Takes two tuples of grades for each category and returns \
the final number grade
        letter_calc: Takes two tuples of grades for each category and returns \
the final letter grade 

    >>> output = grade_calculator(0.4, 0.6)
    >>> len(output) == 2
    True
    >>> output[0]((1, 1, 0.5), (1, 1, 1))
    0.93
    >>> output[1]((0.6, 0.7, 0.8), (0.8, 0.8, 0.8))
    'C'
    >>> output[1]((0.5,), (1,))
    'B'
    >>> output[1]((), ())
    'F'
    >>> output[0]((), ())
    0.0
    >>> output[0]((1,), (1,))
    1.0
    >>> output[0]((1,), ())
    0.4

    # Add at least 3 doctests below here #
    >>> output = grade_calculator(0.25, 0.75)
    >>> output[0]((), (0.5,))
    0.38
    >>> output = grade_calculator(0, 1)
    >>> output[0]((0.5,), (0.5,))
    0.5
    >>> output = grade_calculator(0.99, 0.01)
    >>> output[1]((0.5,), (1,))
    'F'
    """
    # YOUR CODE GOES HERE #
    def num_calc(x, y):
        """
        Given two tuples of grades, calculates the final grade as a number \
based on the the given weights
        """
        grade = w1*sum(x)/(len(x)+(len(x)==0)) + w2*sum(y)/(len(y)+(len(y)==0))
        ROUND_TO = 2
        return round(grade, ROUND_TO)
    
    def letter_calc(x, y):
        """
        Given two tuples of grades, calculates the final grade as a letter \
based on the the given weights
        """
        ROUND_DOWN = 10
        floor = lambda grade: grade*ROUND_DOWN//1/ROUND_DOWN
        grade = w1*sum(x)/(len(x)+(len(x)==0)) + w2*sum(y)/(len(y)+(len(y)==0))
        grade_dict = {0.9: 'A', 0.8: 'B', 0.7: 'C', 0.6: 'D'}
        return grade_dict[floor(grade)] if floor(grade) in grade_dict else 'F'
    
    return num_calc, letter_calc