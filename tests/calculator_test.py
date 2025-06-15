import pytest
from calc.calculator import stringcalculator

def test_stringcalculator_should_return_zero_on_empty_string():
    result=stringcalculator("")
    assert result == 0

def test_stringcalculator_should_return_one_on_anynumericvalue_string():
    result=stringcalculator("1")
    assert result == 1

def test_stringcalculator_should_return_one_on_shoudreturn_that_specifc_numericvalue_string():
    result=stringcalculator("2")
    assert result == 2




