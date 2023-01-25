import random

nums_got = list()

def rolldice():
    num = random.randrange(1,6)
    return num

streak = 1
max_streak = 1
streak_start = 0
streak_end = 0

for i in range(20):
    nums_got.append(rolldice())

for n in range(1, 19):
    if nums_got[n] == nums_got[n-1]:
        streak += 1
    else:
        if streak > max_streak:
            max_streak = streak
            streak_start = n - max_streak
            streak_end = n - 1
        streak = 1

for i in range(len(nums_got)):
    if i == streak_start:
        print('(', end='')
    print(nums_got[i], end='')
    if i == streak_end:
        print(')',end='')