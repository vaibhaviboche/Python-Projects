def array_diff(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    # Symmetric difference: values in one set but not both
    unique = set1.symmetric_difference(set2)

    return sorted(unique)
print(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]))
# ["cherry"]

print(array_diff(["apple", "banana", "cherry"], ["apple", "banana"]))
# ["cherry"]

print(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))
# ["eight", "four", "six", "two"]

print(array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]))
# ["five", "one", "seven", "three"]

print(array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]))
# ["freeCodeCamp", "rocks"]
