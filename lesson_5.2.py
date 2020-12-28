with open("task_2.txt", "r") as f_obj:
    content = f_obj.readlines()
    print(f"{len(content)} - строк в файле")


with open("task_2.txt", "r") as f_obj:
    kolvo = 1
    while kolvo > 0:
        content = f_obj.readline()
        content = content.split()
        kolvo = len(content)
        if kolvo > 0:
            print(f"{kolvo} - слов в строке")
    else:
        print("Строки со словами закончились!")


