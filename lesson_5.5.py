def summary():
    with open('task_5.txt', 'w+') as f_obj:
        line = input('Введите цифры через пробел: \n')
        f_obj.writelines(line)
        my_nbr = line.split()
        res = sum(map(int, my_nbr))
        return res

print(summary())