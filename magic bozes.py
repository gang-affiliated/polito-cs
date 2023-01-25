alices_list = {}

if len(alices_list) == 42:
    print("Alice cant take something new anymore!")

if len(alices_list) == 43:
        exit("its all fucked up now thx 2 u")

def alice_takes(obj, num):
    if obj in alices_list:
        alices_list.update({obj:alices_list[obj]+num})
    else:
        alices_list.update({obj:num})
    return alices_list

def alice_gives(obj, num):
    if obj in alices_list:
        alices_list.update({obj:alices_list[obj]-num})
    else:
        print("Alice doesn't have that item!")
    return alices_list

alice_takes('apple', 1)
print(alices_list)
alice_takes('apple', 1)
print(alices_list)
alice_takes('apple', 2)
print(alices_list)
alice_takes('banana', 3)
print(alices_list)
alice_gives('banana', 1)
print(alices_list)
alice_gives('orange', 1)
