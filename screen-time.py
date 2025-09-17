def too_much_screen_time(hours):
    # Rule 1: Any single day ≥ 10 hours
    if any(h >= 10 for h in hours):
        return True

    # Rule 2: Any 3-day average ≥ 8 hours
    for i in range(len(hours) - 2):
        avg3 = sum(hours[i:i+3]) / 3
        if avg3 >= 8:
            return True

    # Rule 3: Weekly average ≥ 6 hours
    if sum(hours) / 7 >= 6:
        return True

    return False
print(too_much_screen_time([1, 2, 3, 4, 5, 6, 7]))        # False
print(too_much_screen_time([7, 8, 8, 4, 2, 2, 3]))        # False
print(too_much_screen_time([5, 6, 6, 6, 6, 6, 6]))        # False
print(too_much_screen_time([1, 2, 3, 11, 1, 3, 4]))       # True (11 hours)
print(too_much_screen_time([1, 2, 3, 10, 2, 1, 0]))       # True (10 hours)
print(too_much_screen_time([3, 3, 5, 8, 8, 9, 4]))        # True (avg of [8,8,9] = 8.33)
print(too_much_screen_time([3, 9, 4, 8, 5, 7, 6]))        # True (avg of [9,4,8] = 7, [4,8,5] = 5.66, [8,5,7] = 6.66, weekly avg = 6)
