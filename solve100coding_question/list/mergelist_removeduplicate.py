def merge_unique(lst1, lst2):
    return list(set(lst1 + lst2))

# Example usage
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print("Merged list without duplicates:", merge_unique(list1, list2))