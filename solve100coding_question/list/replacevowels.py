s = "Hello World"
vowels = "aeiouAEIOU"
result = ""

for char in s:
    if char in vowels:
        result += "*"
    else:
        result += char

print(result)