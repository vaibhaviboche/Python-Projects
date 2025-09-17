def all_unique(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True
print(all_unique("abc"))             # ✅ True
print(all_unique("aA"))              # ✅ True
print(all_unique("QwErTy123!@"))     # ✅ True
print(all_unique("~!@#$%^&*()_+"))   # ✅ True
print(all_unique("hello"))           # ❌ False
print(all_unique("freeCodeCamp"))    # ❌ False
print(all_unique("!@#*$%^&*()aA"))   # ❌ False

