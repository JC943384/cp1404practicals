numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])  # numbers[0]---3
print(numbers[-1])  # numbers[-1]---2
print(numbers[3])  # numbers[3]---1
print(numbers[:-1])  # numbers[:-1]---[3, 1, 4, 1, 5, 9]
print(numbers[3:4])  # numbers[3:4]---[1]
print(5 in numbers)  # 5 in numbers---True
print(7 in numbers)  # 7 in numbers---False
print("3" in numbers)  # "3" in numbers---False
print(numbers + [6, 5, 3])  # numbers + [6, 5, 3]---[3, 1, 4, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(numbers)
# Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)
# Print all the elements from numbers except the first two (slice)
print(sum(numbers[1:]))

# Print whether 9 is an element of numbers
if 9 in numbers:
    print("9 is an element of numbers")
else:
    print("9 is not an element of numbers")

