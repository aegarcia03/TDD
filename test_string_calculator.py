from string_calculator import string_calculator


def test_empty_string_returns_zero():
    assert string_calculator("") == 0
    
def test_single_number_returns_value():
    assert string_calculator("1") == 1

def test_two_numbers_returns_value():
    assert string_calculator("1,2") == 3

def test_handle_unknown_number_of_args():
    assert string_calculator("1,2,3,4,5") == 15
    
def test_handle_newlines_instead_of_comas():
    assert string_calculator("1,2\n3") == 6

def test_not_allow_separator_at_the_end():
    try:
        string_calculator("1,2,")
        assert False, "Expected exception not thrown"
    except ValueError as e:
        assert str(e) == "Invalid input: trailing separator not allowed"
        
def test_handle_different_delimeters():
    assert string_calculator("//;\n1;2") == 3
    
    