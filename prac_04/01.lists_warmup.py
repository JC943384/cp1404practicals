numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])#numbers[0]---3
print(numbers[-1])#numbers[-1]---2
print(numbers[3])#numbers[3]---1
print(numbers[:-1])#numbers[:-1]---[3,1,4,1,5,9]
print(numbers[3:4])#numbers[3:4]---1
print(numbers[5])#5 in numbers---9
#print(numbers[7])#7 in numbers---list index out of range
print(numbers +[6, 5, 3])#numbers + [6, 5, 3]---[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
#"3" in numbers----"3" in numbers index 0

numbers[0] = "ten"#Change the first element of numbers to "ten" (the string, not the number 10)
print(numbers)
numbers[-1] = 1# Change the last element of numbers to 1
print(numbers)

print(sum(numbers[1:]))#Print all the elements from numbers except the first two (slice)

if 9 in numbers:#Print whether 9 is an element of numbers
    print("9 in an element of numbers.")
else:
    print("9 is not an element of numbers")