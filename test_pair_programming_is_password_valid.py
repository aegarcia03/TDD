from password import is_password_valid, how_many_digits, how_many_characters
from pytest import mark
    
def test_how_many_digits_with_zero_digits():
    assert how_many_digits("angela garcia") == 0
    
@mark.parametrize('digit', '0123456789')
def test_how_many_digits_with_one_digits(digit):
    assert how_many_digits(digit + 'angela') == 1
    
@mark.parametrize('digit', '0')
def test_how_many_digits_with_two_digits(digit):
    assert how_many_digits(digit + 'angela' + digit) == 2
    
def test_how_many_characters():
    assert how_many_characters("angela") == 6

def test_is_password_valid():
    assert is_password_valid("angela") == ["Password must be at least 8 characters",
                                           "The password must contain at least 2 numbers"]
    assert is_password_valid("angela garcia") == ["The password must contain at least 2 numbers"]    
    assert is_password_valid("1234567") == ["Password must be at least 8 characters"]
    assert is_password_valid("12345678") == True


