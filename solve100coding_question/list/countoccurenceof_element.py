def count_element(tup, element):
    return tup.count(element)

# Example usage
my_tuple = (1, 2, 3, 2, 4, 2, 5)
element = 2
print(f"{element} occurs", count_element(my_tuple, element), "times")