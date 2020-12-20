

def my_funk():
    numb1 = int(input("Введите первое число: "))
    numb2 = int(input("Введите второе число: "))
    while numb2 == 0:
        numb2 = int(input("Деление на 0. Введите число != 0: "))
    else: answer = numb1 / numb2

    return (answer)

print(my_funk())