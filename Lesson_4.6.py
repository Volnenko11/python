from itertools import count, cycle

start = int(input("Начальное число: "))
for el in count(start):
    if el >= 40:
        break
    else:
        print(el)

start2 = input("Введите последовательность: ")
num = 0
for el in cycle(start2):
    if num == 20:
        break
    else:
        print(el)
        num +=1