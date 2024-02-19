#  all the odd numbers between 1 and 20 with a space between each one.
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#  count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
for t in range(0, 101, 10):
    print(t, end=' ')
print()

#  count down from 20 to 1
for a in range(20, 0, -1):
    print(a, end=' ')
print()


# print n stars. Ask the user for a number, then print that many stars (*), all on one line.
n = int(input("Number of stars: "))
for s in range(n):
    print("*", end="")
print()

# print n lines of increasing stars.
for f in range(0, n+1):
    print("*"*f)