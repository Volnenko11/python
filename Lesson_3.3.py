
def my_func():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    summ = [a, b, c]
    summ.sort()
    res = summ[1] * summ[2]

    return res

print(my_func())

