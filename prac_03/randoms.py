import random

print(random.randint(5, 20))  # line 1
# What was the smallest number you could have seen, what was the largest?
# line 1 smallest number:5 largest number:20

print(random.randrange(3, 10, 2))  # line 2
# What was the smallest number you could have seen, what was the largest? Could line 2 have produced a 4?
# line 2 smallest number:3 largest number:9 It does not produce a 4


print(random.uniform(2.5, 5.5))  # line 3
# What was the smallest number you could have seen, what was the largest?
# line 3 smallest number:2.5 largest number:nearly 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
random_number = random.randint(0, 100)
print(random_number)
