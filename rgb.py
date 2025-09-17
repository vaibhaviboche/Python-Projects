def rgb_to_hex(rgb_string):
    # Extract the numbers using split and strip
    numbers = rgb_string.strip()[4:-1].split(',')
    r, g, b = [int(n.strip()) for n in numbers]

    # Convert each to two-digit hex and concatenate
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
print(rgb_to_hex("rgb(255, 255, 255)"))  # "#ffffff"
print(rgb_to_hex("rgb(1, 11, 111)"))     # "#010b6f"
print(rgb_to_hex("rgb(173, 216, 230)"))  # "#add8e6"
print(rgb_to_hex("rgb(79, 123, 201)"))   # "#4f7bc9"
