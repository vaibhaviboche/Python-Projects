def find_missing_numbers(arr):
    if not arr:
        return []

    n = max(arr)
    full_range = set(range(1, n + 1))
    present = set(arr)

    missing = sorted(full_range - present)
    return missing
print(find_missing_numbers([1, 3, 5]))                         # [2, 4]
print(find_missing_numbers([1, 2, 3, 4, 5]))                   # []
print(find_missing_numbers([1, 10]))                           # [2, 3, 4, 5, 6, 7, 8, 9]
print(find_missing_numbers([10, 1, 10, 1, 10, 1]))             # [2, 3, 4, 5, 6, 7, 8, 9]
print(find_missing_numbers([3, 1, 4, 1, 5, 9]))                # [2, 6, 7, 8]
print(find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12,
                            6, 8, 9, 3, 2, 10, 7, 4]))         # [11]
