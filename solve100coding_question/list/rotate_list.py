def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # handle k greater than list length
    return lst[-k:] + lst[:-k]

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Rotated list:", rotate_list(my_list, k))