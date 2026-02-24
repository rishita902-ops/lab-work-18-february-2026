def separate_even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers, odd_numbers = separate_even_odd(my_list)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)