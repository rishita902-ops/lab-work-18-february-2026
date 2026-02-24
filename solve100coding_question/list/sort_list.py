def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # swap
    return lst

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Sorted list:", bubble_sort(my_list))