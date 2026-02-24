def find_largest(lst):
    if not lst:  # handle empty list
        return None
    largest = lst[0]
    for item in lst:
        if item > largest:
            largest = item
    return largest

# Example usage
my_list = [10, 25, 7, 42, 18]
print("Largest element is:", find_largest(my_list))