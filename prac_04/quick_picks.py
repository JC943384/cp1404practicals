import random
MIN_NUMBER = 1
MAX_NUMBER = 45
QUICK_PICKS_TIMES = 6
NUMBER_QUICK_PICKS = int(input("How many you quick picks? "))

for _ in range(NUMBER_QUICK_PICKS):
    quick_pick = []
    # if this part used for loop(6) can't avoid each line (quick pick) should not contain any repeated number
    while len(quick_pick) < QUICK_PICKS_TIMES:
        numbers = random.randint(MIN_NUMBER,MAX_NUMBER)
        if numbers not in quick_pick:
            quick_pick.append(numbers)

    quick_pick.sort()

    print(" ".join("{:2}". format(number) for number in quick_pick))


