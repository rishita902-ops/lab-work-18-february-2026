# Create a list of 20 numbers
numbers = [1, 5, 3, 5, 7, 5, 9, 2, 5, 8,
           6, 5, 4, 5, 10, 5, 12, 5, 14, 5]

print("Original List:")
print(numbers)

# Ask user for a number
num = int(input("Enter a number to remove duplicates (except first occurrence): "))

# Check if number exists in list
if num in numbers:
    first_index = numbers.index(num)

    # Create new list keeping first occurrence only
    result = []
    count = 0

    for i in range(len(numbers)):
        if numbers[i] == num:
            count += 1
            if count == 1:
                result.append(numbers[i])
        else:
            result.append(numbers[i])

    print("Updated List:")
    print(result)
else:
    print("Number not found in the list.")