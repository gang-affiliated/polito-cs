import random

nums = list()
for i in range(5):
    nums.append(random.randint(1,50))

print(nums)

weakest = 50

for n in nums:
    if n > weakest:
        pass
    if n < weakest:
        weakest = n

nums.remove(weakest)

print("begone weakling!")
print(nums)
