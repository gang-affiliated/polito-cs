import time

llist1 = []
llist2 = []

print("write OK to complete list!")
print(("put in nums for 1st list"))
a = False

while True:
    if a:
        print("put in numbers or write OK to go on")
    user_input1 = input("here: ")

    try:
        llist1.append(int(user_input1))
    except ValueError:
        if user_input1 == 'OK':
            break
        else:
            a = True

print(("and for the second list:"))
a = False

while True:
    if a:
        print("stop foolin around!")
    user_input2 = input("--> ")

    try:
        llist2.append(int(user_input2))
    except ValueError:
        if user_input2 == 'OK':
            break
        else:
            a = True

print("now with the powers that have been granted to me by the god of creation and the goddes of life, I will merge your lists! ")
time.sleep(3)

def merge(a, b):
    merged = []
    for i in range(len(max(a, b))):
        try:
            merged.append(a[i])
            merged.append(b[i])
        except IndexError:
            if len(a) > len(b):
                try:
                    merged.append(a[i])
                except: pass
            elif len(b) > len(a):
                try:
                    merged.append(b[i])
                except: pass
    return merged

print(merge(llist1, llist2))