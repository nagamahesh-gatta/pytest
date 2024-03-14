import pytest
import source.myfunction as myfunction
import time

def test_add():
    result =  myfunction.add(10, 5)
    assert result == 14, "Assertion miss matched in add function"


def test_add_string():

    result = myfunction.add("I like ", "burgers")
    assert result == "I like burgers"

def test_divide():

    result = myfunction.div(10, 5)
    assert result == 2, "Assertion miss matched in div function"


def test_divide_by_zero():

    with pytest.raises(ValueError):
        myfunction.div(10, 0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = myfunction.div(10, 5)
    assert result == 2

@pytest.mark.skip(reason="This feature is currently broken")
def test_add():

    assert myfunction.add(1, 2) == 3

@pytest.mark.xfail(reason="We know cannot divide by zero")
def test_divide_zero_broken():
    assert myfunction.div(4, 0)