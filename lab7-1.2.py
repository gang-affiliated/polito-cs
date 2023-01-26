def main():
    import random

    nums = []

    for i in range(10):
        x = random.randint(1, 100)
        nums.append(x)
    print(nums)

    evens = []

    for n in nums:
        if n % 2 == 0:
            evens.append(n)

    print(evens)

    #for i in range(1, 10):
     #   print(nums[-i], end=',')
    #print()

    nums.reverse()
    for number in nums:
        print(number, end=' ')

if __name__ == '__main__':
    main()