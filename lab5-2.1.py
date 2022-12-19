def main():
    r_old = int(input("give a num bruv: "))
    for i in range(100):
 #random generator
        a = 32_310_901
        B = 1_729
        m = 224
        r_new = ((a * r_old) + B) % m
        print(r_new)
        r_old = r_new


if __name__ == '__main__':
    main()