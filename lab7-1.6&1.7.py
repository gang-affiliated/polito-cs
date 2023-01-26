def main():
    import random
    llist = []
    for i in range(5):
        llist.append(random.randint(0, 99))

    print(llist)

    llist.sort()

    print(llist)

    def sum_without_smallest(v):
        v.remove(min(v))
        sonuc = sum(v)
        return sonuc

    print(f"here is the sum w/o the smallest value: {sum_without_smallest(llist)}")
if __name__ == '__main__':
    main()