def average_list(lst):
    if len(lst) == 0:
        return 0  # avoid division by zero
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

# Example usage
my_list = [10, 20, 30, 40, 50]
print("Average of list elements:", average_list(my_list))