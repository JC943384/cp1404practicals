NAME_FILE="name.txt"
out_file = open(NAME_FILE,"w")
name = input("Please enter your name ")
print((name), file=out_file)
out_file.close()

with open('name.txt', 'r') as out_file:
    name = out_file.read()

# Print the name
print("Your name is", name)

with open("numbers.txt",'r') as out_file:
    line1 = out_file.readline()
    line2 = out_file.readline()
num1 = int(line1)
num2 = int(line2)
total = num1 + num2
print(total)

with open("numbers.txt",'r') as out_file:
    lines = out_file.readlines()
    total = 0
for line in lines:
    num =int(line)
    total +=num
print(total)




