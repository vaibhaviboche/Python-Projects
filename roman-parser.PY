def parse_roman_numeral(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for ch in reversed(s):
        value = roman[ch]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

print(parse_roman_numeral("III"))     # ✅ 3
print(parse_roman_numeral("IV"))      # ✅ 4
print(parse_roman_numeral("XXVI"))    # ✅ 26
print(parse_roman_numeral("XCIX"))    # ✅ 99
print(parse_roman_numeral("CDLX"))    # ✅ 460
print(parse_roman_numeral("DIV"))     # ✅ 504
print(parse_roman_numeral("MMXXV"))   # ✅ 2025
