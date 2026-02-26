import pytest
from app.calc import add, div, subtract

def test_add():
    assert add(2, 3) == 5

def test_div():
    assert div(10, 2) == 5

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(10, 0)
def test_subtract():
    assert subtract(3, 2) == 1