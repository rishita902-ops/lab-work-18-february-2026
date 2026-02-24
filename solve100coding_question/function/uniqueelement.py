def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 5]
print("Unique elements:", unique_elements(my_list))