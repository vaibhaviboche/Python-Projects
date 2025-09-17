def is_pangram(sentence, allowed_letters):
    # Normalize: lowercase and filter only alphabetic characters
    filtered = [ch.lower() for ch in sentence if ch.isalpha()]
    used_set = set(filtered)
    allowed_set = set(allowed_letters)

    # Must use all allowed letters at least once, and no other letters
    return used_set.issubset(allowed_set) and allowed_set.issubset(used_set)
print(is_pangram("hello", "helo"))                      # ✅ True
print(is_pangram("hello", "hel"))                       # ✅ False
print(is_pangram("hello", "helow"))                     # ✅ False
print(is_pangram("hello world", "helowrd"))             # ✅ True
print(is_pangram("Hello World!", "helowrd"))            # ✅ True
print(is_pangram("Hello World!", "heliowrd"))           # ✅ False
print(is_pangram("freeCodeCamp", "frcdmp"))             # ✅ False
print(is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz"))  # ✅ True
