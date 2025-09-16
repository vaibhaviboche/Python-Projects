def calculate_check_digit_10(isbn):
    total = 0
    for i in range(9):
        total += int(isbn[i]) * (10 - i)
    remainder = total % 11
    return 'X' if remainder == 1 else str((11 - remainder) % 11)

def calculate_check_digit_13(isbn):
    total = 0
    for i in range(12):
        factor = 1 if i % 2 == 0 else 3
        total += int(isbn[i]) * factor
    remainder = total % 10
    return str((10 - remainder) % 10)

def validate_isbn(code, length):
    try:
        if length == 10:
            if len(code) != 10:
                print("ISBN-10 code should be 10 digits long.")
                return
            check_digit = calculate_check_digit_10(code)
        elif length == 13:
            if len(code) != 13:
                print("ISBN-13 code should be 13 digits long.")
                return
            check_digit = calculate_check_digit_13(code)
        else:
            print("Length should be 10 or 13.")
            return

        if code[-1].upper() == check_digit:
            print("Valid ISBN Code.")
        else:
            print("Invalid ISBN Code.")
    except ValueError:
        print("Invalid character was found.")

def main():
    user_input = input("Enter ISBN and length: ")
    try:
        code, length = user_input.split(",")
    except IndexError:
        print("Enter comma-separated values.")
        return

    try:
        length = int(length)
    except ValueError:
        print("Length must be a number.")
        return

    validate_isbn(code, length)

# Commented out for testing purposes
# main()
def calculate_check_digit_10(isbn):
    total = 0
    for i in range(9):
        total += int(isbn[i]) * (10 - i)
    remainder = total % 11
    return 'X' if remainder == 1 else str((11 - remainder) % 11)

def calculate_check_digit_13(isbn):
    total = 0
    for i in range(12):
        factor = 1 if i % 2 == 0 else 3
        total += int(isbn[i]) * factor
    remainder = total % 10
    return str((10 - remainder) % 10)

def validate_isbn(code, length):
    try:
        if length == 10:
            if len(code) != 10:
                print("ISBN-10 code should be 10 digits long.")
                return
            check_digit = calculate_check_digit_10(code)
        elif length == 13:
            if len(code) != 13:
                print("ISBN-13 code should be 13 digits long.")
                return
            check_digit = calculate_check_digit_13(code)
        else:
            print("Length should be 10 or 13.")
            return

        if code[-1].upper() == check_digit:
            print("Valid ISBN Code.")
        else:
            print("Invalid ISBN Code.")
    except ValueError:
        print("Invalid character was found.")

def main():
    user_input = input("Enter ISBN and length: ")
    parts = user_input.split(",")

    if len(parts) != 2:
        print("Enter comma-separated values.")
        return

    code, length = parts

    try:
        length = int(length)
    except ValueError:
        print("Length must be a number.")
        return

    validate_isbn(code, length)


# Commented out for testing purposes
# main()
validate_isbn("1530051126", 10)  # Valid ISBN Code.
validate_isbn("9781530051120", 13)  # Valid ISBN Code.
validate_isbn("1530051125", 10)  # Invalid ISBN Code.
validate_isbn("9781530051120", 10)  # ISBN-10 code should be 10 digits long.
validate_isbn("15-0051126", 10)  # Invalid character was found.
