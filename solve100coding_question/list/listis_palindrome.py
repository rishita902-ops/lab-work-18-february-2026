def is_palindrome(lst):
    n = len(lst)
    for i in range(n // 2):
        if lst[i] != lst[n - i - 1]:
            return False
    return True

# Example usage
my_list = [1, 2, 3, 2, 1]
print("Is palindrome?", is_palindrome(my_list))