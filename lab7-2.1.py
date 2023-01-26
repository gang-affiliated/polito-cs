import random

def main():

    llist = []
    for i in range(10):
        llist.append(random.randint(0, 99))

    print("Your data: \n" + str(llist))

    llist.sort()

    print("Here's you data sorted:  \n" + str(llist))

    def clear_data_noise(list):
        to_be_removed = []
        for i, n in enumerate(list):
            try:
                if list[i] == (list[i - 1] + list[i + 1]) / 2:
                    to_be_removed.append(n)
            except IndexError:
                if list[i] == list[len(list) - 1] and list[i] == list[i - 1]:
                    to_be_removed.append(n)
                if list[i] == list[0] and list[i] == list[i + 1]:
                    to_be_removed.append(n)
        for l in to_be_removed:
            list.remove(l)
        print(to_be_removed)
        return list

    print("Here's the cleaned version of your data: ")
    print(clear_data_noise(llist))
if __name__ == '__main__':
    main()