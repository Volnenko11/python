sum = 0

while True:
    user_number = input("Введите числовую последовательность: ")
    user_number.split()
    for item in user_number:
        if item == "i":
            break
        else:
            sum += int(item)
    print(sum)
    if item == "i":
        break
