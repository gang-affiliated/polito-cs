import time
def main():

    def same_set(a, b):
        check_set_1 = set()
        check_set_2 = set()
        for i in a:
            if i not in check_set_1:
                check_set_1.add(i)
            if i in check_set_1:
                pass
        for n in b:
            if n not in check_set_2:
                check_set_2.add(n)
            if n in check_set_2:
                pass
        if check_set_1 == check_set_2:
            return True
        else:
            return False

    li1 = []
    li2 = []

    long = int(input("how long is this list 1 foo: "))

    for i in range(long):
        nums = int(input(f"num{i + 1} : "))
        li1.append(nums)

    long2 = int(input("and how long is list 2 gang: "))

    for i in range(long2):
        nums = int(input(f"num{i + 1} : "))
        li2.append(nums)

    print("finna see if your lists are the same...")
    time.sleep(2.5)
    if same_set(li1, li2) is True:
        print("yessir, they are")
    else:
        print("nah these are diff lists foo!")

if __name__ == '__main__':
    main()