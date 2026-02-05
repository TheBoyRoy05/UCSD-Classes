"""
DSC 20 Winter 2024 Homework 10
Name: Issac Roy
PID: A17787465
Source: N/A
"""

class Calculator:
    def __init__(self):
        self.history = {'adds': 0, 'subs': 0, "mults": 0, "exceptions": 0}

    def add(self, x, y):
        self.history['adds'] += 1
        return x + y

    def subtract(self, x, y):
        self.history['subs'] += 1
        return x - y

    def multiply(self, x, y):
        self.history['mults'] += 1
        return x * y

    def divide(self, x, y, intDiv=False):
        if y == 0:
            self.history['exceptions'] += 1
            raise ValueError("Division by zero is not allowed")
        if not intDiv:
            return x / y
        else:
            return x // y

    def __repr__(self):
        return str(sum([val for val in self.history.values()]))