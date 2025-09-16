def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    result = ''
    for i in range(1, n + 1):
        result += str(i) + ' '
    
    return result.strip()
print(number_pattern(4))     # Output: "1 2 3 4"
print(number_pattern(12))    # Output: "1 2 3 4 5 6 7 8 9 10 11 12"
print(number_pattern("hi"))  # Output: "Argument must be an integer value."
print(number_pattern(0))     # Output: "Argument must be an integer greater than 0."
