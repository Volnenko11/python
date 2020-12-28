with open("task_3.txt", "r") as f_obj:
    q = True
    while q == True:
        content = f_obj.readline()
        content1 = content.split()
        zarplata = (content1[1])
        if zarplata >= "20000":
            print(content)
            pass
        else:
            q = False
            print("Это все товарищи, с большими окладами..:(")

with open("task_3.txt", "r") as f_obj:
    def my_res():
        zp = 0
        nbr = 0
        while nbr < 5:
            content = f_obj.readline()
            content1 = content.split()
            zarplata = int(content1[1])
            zp += zarplata
            nbr += 1
        else:
            anwer = zp // nbr
        return (anwer)
    print(my_res())



