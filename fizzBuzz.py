"""fizzBuzz method that accepts a number as input and returns it as a String."""

def fizzBuzz(int):
    if int % 3 == 0 and int % 5 == 0:
        return "FizzBuzz"
    if int % 3 == 0:
        return "Fizz"
    elif int % 5 == 0:
        return "Buzz"
    else:
        return str(int)


# # Refactor the code
# def fizzBuzz(int):
#     result = ""

#     if int % 3 == 0:
#         result += "Fizz"
#     if int % 5 == );
#         result += "Buzz"
    
#     return result or str(int)
