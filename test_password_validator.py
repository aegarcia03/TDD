from password_validator import password_validator

def test_password_length():
    # Test with a short password
    result = password_validator("secure")
    assert result["valid"] == False
    assert "Password must be at least 8 characters" in result["errors"]

    #Test with a long enough password 
    result = password_validator("password123")
    assert "Password must be at least 8 characters" not in result["errors"]


def test_pasword_with_2_numbers():
    #Test with a password with no numbers
    result = password_validator("securepassword")
    assert result["valid"] == False
    assert "The password must contain at least 2 numbers" in result["errors"]

    #Test with a password with numbers
    result = password_validator("securepass123")
    assert "The password must contain at least 2 numbers" not in result ["errors"]

def test_one_capital_letter():
    #Test without a capital letter
    result = password_validator("securepassword")
    assert result["valid"] == False
    assert "password must contain at least one capital letter" in result["errors"]

    #Test with a capital letter
    result = password_validator("SecurePass123")
    assert "password must contain at least one capital letter" not in result ["errors"]

def test_multiple_validation_errors():

    result = password_validator("securepassword")
    assert result["valid"] == False
    assert "password must contain at least one capital letter" in result["errors"]
    assert "The password must contain at least 2 numbers" in result["errors"]
    assert "password must contain at least one special character" in result["errors"]  
    #Check that we have two errors
    assert len(result["errors"]) == 3

def test_one_special_characters():

    #test password without special char
    result = password_validator("SecurePass123")
    assert result["valid"] == False
    assert "password must contain at least one special character" in result["errors"]

    #test password without special char
    result = password_validator("SecurePass123!")
    assert "password must contain at least one special character" not in result["errors"]
    assert result["valid"] == True
    
 