def is_palindrome(text):
    # Remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    return text == text[::-1]


# Example usage
string = input("Enter a string: ")

if is_palindrome(string):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")