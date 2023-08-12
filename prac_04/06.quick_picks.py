import random
min_num = 1
max_num = 45
pick_times = 6
num_quick = int(input("Enter you want quick picks: "))

for _ in range(num_quick):
    quick_pick = []
    while len(quick_pick) < pick_times:
         numbers = random.randint(min_num,max_num)
         if numbers not in quick_pick:
             quick_pick.append(numbers)

    quick_pick.sort()
    formatted_quick_pick = ', '.join(f'{number:2d}' for number in quick_pick)
    print(formatted_quick_pick)




