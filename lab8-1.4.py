row = int(input("how many rows browski?: "))
col = int(input("how many colmns cuz?: "))

list = [[0 for c in range(col)] for r in range(row)]


def print_tablr(list):
 print(f"+{('-' * 3 + '+') * row}")

 for er in list:
     print('|', end='')

     for index, element in enumerate(er):
         print(f" {element:^} |", end='')
     print()
     print(f"+{('-' * 3 + '+') * row}")

print_tablr(list)

for r in range(len(list)):
    for c in range(len(list)):
        list[r][c] = 1

print_tablr(list)

for r in range(len(list)):
    for c in range(len(list)):
        list[r][c] = 0 if (r+c) % 2 == 0 else 1
print_tablr(list)

for r in range(len(list)):
    for c in range(len(list)):
        if r == 0 or r == len(list)-1:
            list[r][c] = 0
print_tablr(list)

for r in range(len(list)):
    for c in range(len(list)):
        if c == 0 or c == len(list)-1:
            list[r][c] = 1
print_tablr(list)

def nested_sum(list) :
    total = 0
    for i in list :
        try:
            total += i
        except TypeError: #(if type is list)
            total += nested_sum(i) #(puts the nested list in try mode)
    return total

print(f"sum is: {nested_sum(list)}")