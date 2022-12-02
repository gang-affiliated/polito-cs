currenty = int(input("put in a year gang: "))
while currenty <= 1582 :
    print("after 1582 you dumb mf dont you know about the Gregorian correction... smh")

if currenty%4 == 0 and currenty%100 != 0:
    print("ur year is a leap year foo")
elif currenty%400 == 0:
    print("issa leap year!")
else:
    print("normal ass lame year")
