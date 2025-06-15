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

def test_stringcalculator_should_return_that_specifc_sumvalue_string():
    result=stringcalculator("2,3")
    assert result == 5

def test_stringcalculator_with_backslash():
    result=stringcalculator("1\n2")
    assert result == 3

#"//[delimiter]\n[numbers…]"
def test_stringcalculator_handling_with_different_delimiters():
    result=stringcalculator("//;\n1;2;3")
    assert result == 6

def test_stringcalculator_handling_with_different_delimiters_with_negative_numbers():
    result=stringcalculator("//!-;\n12!-;12!-;3")
    assert result == 27

def test_stringcalculator_handling_with_different_delimiters_with_negative_numbers():
    result=stringcalculator("//-\n1-2-3")
    assert(result == 6,"negative numbers not allowed <negative_number>")




