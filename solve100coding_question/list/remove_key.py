data = {"a": 1, "b": 2, "c": 3}

# Safely remove key 'b'
removed_value = data.pop("b", None)  # Returns None if key doesn't exist

print("Updated dictionary:", data)
print("Removed value:", removed_value)