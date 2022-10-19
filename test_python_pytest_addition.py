import python_pytest_addittion
import pytest

def test_add():
    assert python_pytest_addittion.add(4,5) == 9
def test_sub():
    assert python_pytest_addittion.sub(4,5) == -2