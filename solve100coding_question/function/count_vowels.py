def count_vowels(text):
    text = text.lower()  # make it case-insensitive
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Example usage
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))