# Step 1: Create test_settings dictionary
test_settings = {
    'theme': 'light',
    'language': 'english',
    'notifications': 'enabled'
}

# Step 2–8: Define add_setting
def add_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

# Step 9–15: Define update_setting
def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# Step 16–21: Define delete_setting
def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

# Step 22–27: Define view_settings
def view_settings(settings):
    if not settings:
        return "No settings available."
    
    output = "Current User Settings:\n"
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"
    return output
print(add_setting(test_settings, ('Volume', 'High')))
print(update_setting(test_settings, ('theme', 'dark')))
print(delete_setting(test_settings, 'language'))
print(view_settings(test_settings))
