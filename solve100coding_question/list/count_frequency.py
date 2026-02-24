def count_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 4, 5]
print("Frequency of elements:", count_frequency(my_list))