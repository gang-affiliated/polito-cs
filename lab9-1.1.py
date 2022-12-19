li = []

def swap(li):
    a = li[-1]
    b = li[0]
    li.remove(a)
    li.remove(b)
    li.append(b)
    li.insert(0, a)

def shift(li):
    li = li[-1:]+li[:-1]
    print(li)

def zerofy_evens(li):
    for num in li:
        if li[num]%2 == 0:
            li[num] = 0
    print(li)

def second_largest(li):
    li.remove(max(li))
    print(max(li))

def main():

 long = int(input("how long is this list foo: "))

 for i in range(long):
     nums = int(input(f"num{i+1} : "))
     li.append(nums)

 print(li)

 print("things you can do! \n"
       "swap , shift , zerofy evens , second largest")
 ffunction = input("what do you want to do with this list?: ")

 if ffunction == 'swap':
     swap(li)
     print(li)

 elif ffunction == 'shift':
     shift(li)

 elif ffunction == 'zerofy_evens':
     zerofy_evens(li)

 elif ffunction == 'second largest':
     second_largest(li)

if __name__ == '__main__':
    main()
