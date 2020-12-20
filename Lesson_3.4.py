x = int(input("Введите число: "))
y = int(input("Введите отрицательную степень: "))

def my_func(x, y):

    if y == 0:
        return 1
    return x * my_func(x, y+1)

print(1/my_func(x, y))