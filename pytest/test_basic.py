
from basic01 import add , divide
import pytest


# def test_add():
#     result = add(a=4, b= 9)
#     assert result == 13


# def test_add_string():
#     result = add(a="I love ", b= "bugs")
#     assert result == "I love bugs"


# def test_divide():
#     result = divide(a=10, b= 5)
#     assert result == 2
    
# def test_divide_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         divide(10,0)
    
# def test_divide_by_zero_case():
#     with pytest.raises(ValueError):
#         divide(10,0)
    

# advance way to write code 

def test_add():
    assert add(-1, 1) == 0, "should be 0" # passed case
    assert add(0, 0) == 1, " 0 + 0 should be 0" # failed case



def test_divide():
    with pytest.raises(ValueError, match="can not divide"):
        divide(4,0)

   