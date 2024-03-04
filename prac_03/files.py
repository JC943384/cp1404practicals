NAME_FILE = "name.txt"
out_file = open(NAME_FILE, "w")
name = input("Please enter your name: ")
print(name, file=out_file)
out_file.close()

with open('name.txt', 'r') as out_file:
    name = out_file.read()
    # Print the name
    print("Your name is", name)

NUM_OF_NUMBERS_TO_ADD = 2
with open("numbers.txt", 'r') as file:
    total = 0
    for i in range(NUM_OF_NUMBERS_TO_ADD):
        num = int(file.readline())
        total += num
    print("first two numbers adds:", total)

with open("numbers.txt", 'r') as out_file:
    total = 0
    for line in out_file:
        num = int(line)
        total += num
    print("The total sum of all numbers in numbers.txt is:", total)




