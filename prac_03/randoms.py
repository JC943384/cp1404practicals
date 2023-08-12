import random

print(random.randint(5, 20))
# line 1 smallest number:5  largest number:20
print(random.randrange(3, 10, 2))
# line 2 smallest number:3 largest number:9 It does not produce a 4
print(random.uniform(2.5, 5.5))
# line 3 smallest number:2.5 largest number:nearly and less than 5.5

random_number = random.randint(1,100)
print(random_number)