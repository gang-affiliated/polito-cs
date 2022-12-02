primes = []

def isprime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

n = int(input("give num: "))

for x in range(2, n):
    if isprime(x):
        primes.append(x)

print(primes)