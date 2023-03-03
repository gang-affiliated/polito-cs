import random

def main():
    masa = []
    wanted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    piles = int(input("how many piles: "))

    kartlar = 45

    for i in range(piles):
        l = 1
        b = kartlar - piles + 1
        if b <= 0:
            b = 1
            l = 1
        a = random.randint(l, b)
        masa.append(int(a))
        kartlar = kartlar - a

    dagger_dick = int(sum(masa))

    print("checkpoint 1", masa)
    print("piles", piles)

    dalyarak = True
    m = min(masa)
    n = masa.index(m)
    if dagger_dick < 45 and dalyarak:
        eksik = int(45 - dagger_dick)
        masa[n] = m + eksik
        dalyarak = False

    print("checkpoint 2", masa)

    while masa != wanted:
        for i in range(0, len(masa)):
            masa[i] = masa[i] - 1

        masa.append(int(len(masa)))

        while 0 in masa:
            masa.remove(0)

        print(masa)
if __name__ == '__main__':
    main()