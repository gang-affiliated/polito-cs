def main():
    thenum = int(input("give me a num and imma give you its factors fam: "))
    factors = []
    bolen = 2

    # better to use "while thenum > 1" instead of lines 8-9

    for i in range(thenum):
        if thenum > 1:
            if thenum % bolen == 0:
                factors.append(bolen)
                thenum = thenum // bolen
            else:
                bolen += 1
    print(*factors, end=" gang shit no lame shit")


if __name__ == '__main__':
    main()