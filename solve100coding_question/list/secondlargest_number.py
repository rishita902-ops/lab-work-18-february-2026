def second_largest(lst):
    if len(lst) < 2:
        return None  # Not enough elements
    
    largest = second = float('-inf')
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second

# Example usage
my_list = [10, 25, 7, 42, 18]
print("Second largest number is:", second_largest(my_list))