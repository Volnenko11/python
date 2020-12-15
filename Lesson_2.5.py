my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
your_list = int(input("Введите число: "))
for el in range(len(my_list)):
    if my_list[0] <= your_list:
            my_list.insert(0, your_list)
    elif my_list[-1] >= your_list:
            my_list.append(your_list)
    elif my_list[el] >= your_list and my_list[el + 1] <= your_list:
            my_list.insert(el + 1, your_list)
    print(f"текущий список - {my_list}")
    your_list = int(input("Введите число "))