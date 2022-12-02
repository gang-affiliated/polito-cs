pin = '1234'
wrong_input = 0

for i in range(3):
    iinput = input("enter pin: ")
    if iinput == pin:
        print("ur good")
        break
    if iinput != pin:
        wrong_input += 1
        if wrong_input != 3:
            print("wrong pin foo")
        if wrong_input == 3:
            print("ur cards blocked")