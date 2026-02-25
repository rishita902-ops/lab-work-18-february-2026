def are_anagrams(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

# Example
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False