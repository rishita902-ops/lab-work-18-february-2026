def replace_negatives(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0
    return lst

# Example usage
my_list = [10, -5, 7, -3, 2, -8]
print("After replacing negatives:", replace_negatives(my_list))