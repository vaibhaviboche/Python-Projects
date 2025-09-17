def adjust_thermostat(current, target):
    if current < target:
        return "heat"
    elif current > target:
        return "cool"
    else:
        return "hold"

# Use print() to see the results
print(adjust_thermostat(68, 72))         # "heat"
print(adjust_thermostat(75, 72))         # "cool"
print(adjust_thermostat(72, 72))         # "hold"
print(adjust_thermostat(-20.5, -10.1))   # "heat"
print(adjust_thermostat(100, 99.9))      # "cool"
print(adjust_thermostat(0.0, 0.0))       # "hold"
