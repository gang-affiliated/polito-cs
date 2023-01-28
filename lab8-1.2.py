def main():
    print("enter 5 elemnts for list")

    a_list = []

    for i in range(5):
        given = int(input())
        a_list.append(given)

    list = a_list.copy()

    def shift_right(list):
        copy = list.copy()
        for i in range(len(list)):
            if i == 0:
                list[i] = copy[len(list) - 1]
            else:
                list[i] = copy[i - 1]

        return list

    print("heres ur list is", list)

    print("heres that shit shifted right", shift_right(list))

    list = a_list

    a = list[0]

    new = list
    new.pop(0)
    new.append(a)

    print("heres that shit shifted left", new)

    ending = input("press enter to exit")

    if ending == "":
        exit()


if __name__ == '__main__':
    main()