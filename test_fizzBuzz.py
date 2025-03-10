from fizzBuzz import fizzBuzz

def test_fizzBuzz_int_to_str():
    assert fizzBuzz(1) == "1"

def test_multiple_of_3():
    assert fizzBuzz(3) == "Fizz"

def test_multiples_of_5():
    assert fizzBuzz(5) == "Buzz"

def test_multiples_of_3_and_5():
    assert fizzBuzz(15) == "FizzBuzz"

# Now I need to refactor?