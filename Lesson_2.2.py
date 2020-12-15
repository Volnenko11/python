
user_list = list(input("Введите произвольные элементы: "))
user_list[::2], user_list[1::2], user_list[-1] = user_list[1::2], user_list[::2], user_list[-1]
print(user_list)
