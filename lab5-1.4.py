def main():

    tickets = 10
    buyers = 0
    price = 13.78
    buyers_names = list()
    limited = list()
    while tickets != 0:
        print(f"{tickets} available")
        how_many_tickets = int(input("How many tickets would you like to buy: "))
        if 1 <= how_many_tickets <= 4 and how_many_tickets <= tickets:
            print(f"your total is {(how_many_tickets*price)} ")
            buyornot = input("Continue to purchase [Y/N] : ")
            if buyornot == "Y":
                tickets = tickets - how_many_tickets
                buyers += 1
            if buyornot == "N":
                print("broke boi lmao")
        elif how_many_tickets < 1:
            print("You tryna punk me mf?!")
        elif how_many_tickets > 4:
            print("you can only buy up to 4 tickets")
        elif how_many_tickets > tickets:
            print(f"there is only {tickets} left")

    print(f"sorry all tickets are sold! {buyers} buyers in total!")

if __name__ == '__main__':
    main()