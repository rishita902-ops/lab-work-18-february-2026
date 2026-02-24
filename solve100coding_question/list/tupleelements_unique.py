def is_unique(tup):
    return len(tup) == len(set(tup))

# Example usage
my_tuple = (1, 2, 3, 4, 5)
print("All elements are unique?", is_unique(my_tuple))

my_tuple2 = (1, 2, 3, 2, 5)
print("All elements are unique?", is_unique(my_tuple2))