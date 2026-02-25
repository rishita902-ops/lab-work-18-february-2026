dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {}

# Add items from first dictionary
for key in dict1:
    merged[key] = dict1[key]

# Add items from second dictionary
for key in dict2:
    merged[key] = dict2[key]

print(merged)