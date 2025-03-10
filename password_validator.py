'''A function to be used as a validator for the password field of a user registration form. '''

# def password_validator(password):
#     errors = []
#     count = 0

#     if len(password) < 8:
#         errors.append("Password must be at least 8 characters")
    
#     for x in password:
#         if x.isdigit():
#             count += 1

#     if count < 2:
#         errors.append("The password must contain at least 2 numbers")

#     # Return validation result
#     return {
#         "valid": len(errors) == 0,
#         "errors": errors
#     }

# Refactor

# def password_validator(password):
#     errors = []
#     #Check password length
#     if len(password) < 8:
#         errors.append("Password must be at least 8 characters")
    
#     #Check for at least 2 numbers
#     number_count = sum(x.isdigit() for x in password)

#     if number_count < 2:
#         errors.append("The password must contain at least 2 numbers")
        
#     #Check for a least one capital letter
#     if not any(x.isupper() for x in password):
#         errors.append("password must contain at least one capital letter")

#     #Check for one special character
#     special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/'\"\\"
#     if not any(x in special_chars for x in password):
#         errors.append("password must contain at least one special character")
#     # Return validation result
#     return {
#         "valid": len(errors) == 0,
#         "errors": errors
#   }

# Refactor

def password_validator(password):
    errors = []

    validations = [
        (len(password) < 8, 
        "Password must be at least 8 characters"),

        (sum(1 for x in password if x.isdigit()) < 2,
        "The password must contain at least 2 numbers"),

        (not any(x.isupper() for x in password),
        "password must contain at least one capital letter"),

        (not any(x in "!@#$%^&*()-_=+[]{}|;:,.<>?/'\"\\" for x in password),
        "password must contain at least one special character"),
    ]
    
    for condition, error_message in validations:
        if condition:
            errors.append(error_message)
    # Return validation result
    return {
        "valid": len(errors) == 0,
        "errors": errors
  }