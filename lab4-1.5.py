num = int(input("give num: "))

if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            print("isnot a prime number!")
else:
 print("is a pirme num")
