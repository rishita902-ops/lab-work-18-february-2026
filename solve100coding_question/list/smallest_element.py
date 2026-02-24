def find_smallest(lst):
    if not lst:  # handle empty list
        return None
    smallest = lst[0]
    for item in lst:
        if item < smallest:
            smallest = item
    return smallest

# Example usage
my_list = [10, 25, 7, 42, 18]
print("Smallest element is:", find_smallest(my_list))