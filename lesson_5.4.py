
dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_list = []

with open("task_4.txt", "r") as f_obj:
    for row in f_obj:
        nbr, value = row.split(' - ')
        new_list.append(f"{dict[nbr]} - {value}")

with open("task_4_1.txt", "w") as f_obj:
    f_obj.writelines(new_list)

with open("task_4_1.txt", "r") as f_obj:
    print(f_obj.read())
