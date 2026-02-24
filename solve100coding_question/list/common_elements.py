def common_elements(lst1, lst2):
    common = []
    for item in lst1:
        if item in lst2 and item not in common:
            common.append(item)
    return common

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Common elements:", common_elements(list1, list2))