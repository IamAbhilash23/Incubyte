import pytest
from calc.calculator import stringcalculator

def test_stringcalculator_should_return_zero_on_empty_string():
    result=stringcalculator("")
    assert result == 0




