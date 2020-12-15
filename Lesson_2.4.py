user_str = str(input("Введите несколько слов через пробел: "))
number = 1
new_str = []

for el in range(user_str.count(' ') + 1):
    new_str = user_str.split()
    if len(str(new_str)) <= 10:
        print(f" {number}. {new_str [el]}")
        number += 1
    else:
        print(f" {number}. {new_str [el] [0:10]}")
        number += 1
