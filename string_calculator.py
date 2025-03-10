# calculator function
def string_calculator(numbers):
    if not numbers:
        return 0
    if numbers.endswith(","):
        raise ValueError("Invalid input: trailing separator not allowed")
    delimeter = ","
    if numbers.startswith("//"):
        delimeter_line, numbers = numbers.split("\n", 1)# Split the first line from the rest
        delimeter = delimeter_line[2:] # Extract the delimiter (after `//`)
   
    numbers = numbers.replace("\n", delimeter)
    parts = numbers.split(delimeter)
  
    return sum(int(n) for n in parts)

