from curses.ascii import isdigit
import python_findstring
import pytest

def test_ispresent():
    assert python_findstring.ispresent("a1")