def is_valid_ipv4(ipv4):
    parts = ipv4.split('.')

    # Must have exactly 4 parts
    if len(parts) != 4:
        return False

    for part in parts:
        # Check if part is purely numeric
        if not part.isdigit():
            return False

        # Check for leading zeros (except "0" itself)
        if len(part) > 1 and part[0] == '0':
            return False

        # Check if value is in range 0–255
        num = int(part)
        if num < 0 or num > 255:
            return False

    return True
print(is_valid_ipv4("192.168.1.1"))       # ✅ True
print(is_valid_ipv4("0.0.0.0"))           # ✅ True
print(is_valid_ipv4("255.01.50.111"))     # ❌ False (leading zero)
print(is_valid_ipv4("255.00.50.111"))     # ❌ False (leading zero)
print(is_valid_ipv4("256.101.50.115"))    # ❌ False (256 out of range)
print(is_valid_ipv4("192.168.101."))      # ❌ False (missing last part)
print(is_valid_ipv4("192168145213"))      # ❌ False (no dots)
