import pytest
from calculator.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(3, 2) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract(calculator):
    assert calculator.subtract(3, 2) == 1
    assert calculator.subtract(2, 3) == -1
    assert calculator.subtract(0, 0) == 0

def test_multiply(calculator):
    assert calculator.multiply(3, 2) == 6
    assert calculator.multiply(0, 1) == 0
    assert calculator.multiply(-1, 1) == -1

def test_divide(calculator):
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        calculator.divide(5, 0)
