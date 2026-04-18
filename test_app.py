import pytest
import app

def test_add():
    assert app.add(2, 3) == 5
    assert app.add(-1, 1) == 0

def test_subtract():
    assert app.subtract(5, 3) == 2
    assert app.subtract(0, 4) == -4

def test_multiply():
    assert app.multiply(2, 3) == 6
    assert app.multiply(-1, 5) == -5

def test_divide():
    assert app.divide(6, 3) == 2
    assert app.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        app.divide(10, 0)