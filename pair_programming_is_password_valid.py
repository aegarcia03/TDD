def how_many_characters(s):
    return len(s)

def is_digit(ch):
    return ch in '0123456789'

def how_many_digits(s):
    result = 0
    for char in s:
        if is_digit(char):
            result += 1    
    return result


def is_password_valid(password):
    errors = []
    enough_characters = how_many_characters(password) >= 8
    enough_digits = how_many_digits(password) >= 2
    
    if not enough_characters:
        errors.append('Password must be at least 8 characters')
    
    if not enough_digits:
        errors.append('The password must contain at least 2 numbers')
    
    if len(errors) == 0:
        return True
    
    return errors
    