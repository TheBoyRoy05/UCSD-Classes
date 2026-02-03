"""
DSC 20 Lab 00
Name: Issac Roy
PID:  A17787465
"""

def respect_your_cat(food, num):
    """
    This method is a demand from your cats to provide food for them.
    If the food is strictly less than 5 characters, this method will 
    return "Give me more food!" Otherwise return the food as a string
    followed by 'num' # of exclamation marks.

    >>> respect_your_cat("dog", 5)
    'Give me more food!'
    >>> respect_your_cat("lots of fish and lots of fish", 4)
    'lots of fish and lots of fish!!!!'
    >>> respect_your_cat("Fruits", 0)
    'Fruits'
    """
    # YOUR CODE GOES HERE #
    return food + '!'*num if len(food) >= 5 else 'Give me more food!'