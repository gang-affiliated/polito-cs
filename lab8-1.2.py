print("enter 5 elemnts for list")

list = []

for i in range(5):
    given = int(input())
    list.append(given)

print(f"heres ur list is {list}")


a = list[0]

new = list
new.pop(0)
new.append(a)

print(f"heres that shit shifted {new}")
