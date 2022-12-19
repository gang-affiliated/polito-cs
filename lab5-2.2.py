
import random

x = 0
y = 0

print(x)

for i in range(100):

    which_way = random.randint(1, 4)

    if which_way == 1 : x += 1
    elif which_way == 2 : x -= 1
    elif which_way == 3 : y += 1
    elif which_way == 4 : y -= 1

    print(f"{x} , {y}")
