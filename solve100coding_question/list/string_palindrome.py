def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

# Example
s = "radar"
print(is_palindrome(s))  # Output: True