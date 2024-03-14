import pytest
import source.myfunction as myfunction


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
