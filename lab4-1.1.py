nums = []

while True:
    xa = int(input("put in nums to sum: "))
    if xa == "let me out":
        break
    else:
     nums.append(xa)
     sums = sum(nums)

     print(*nums, sep='+', end='=' + str(sums) + '\n')