from Calculator import Calculator
import pytest

@pytest.fixture
def calc():
    return Calculator()

def test_calculator(calc):
    assert all([val == 0 for val in calc.history.values()])
    
def test_add(calc):
    sum = calc.add(2, 3)
    assert sum == 5 and calc.history['adds'] == 1
    
def test_subtract(calc):
    diff = calc.subtract(2, 3)
    assert diff == -1 and calc.history['subs'] == 1
    
def test_multiply(calc):
    product = calc.multiply(2, 3)
    assert product == 6 and calc.history['mults'] == 1
    
def test_divide(calc):
    quotient = calc.divide(2, 3)
    assert quotient == 2/3 and calc.history['exceptions'] == 0
    
def test_int_divide(calc):
    quotient = calc.divide(2, 3, intDiv=True)
    assert quotient == 0 and calc.history['exceptions'] == 0
    
def test_divide_exception(calc):
    with pytest.raises(ValueError):
        calc.divide(2, 0)
    assert calc.history['exceptions'] == 1
    
def test_repr(calc):
    calc.add(2, 3)
    calc.subtract(2, 3)
    calc.multiply(2, 3)
    with pytest.raises(ValueError):
        calc.divide(1, 0)
    assert repr(calc) == '4'