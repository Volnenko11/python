user_text = []

while True:
    with open('task_1.txt', 'a+') as f_obj:
        user_text = input("Введите данные: ")
        f_obj.write(f"{user_text}")
    if not user_text:
        break



with open("task_1.txt", "r") as f_obj:
    content = f_obj.readlines()
    print(content)





