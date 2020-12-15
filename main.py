min = 60
hour = 3600


user_input = int(input("Введите время в секундах: "))
if user_input >= hour:
    knowhour = user_input // 3600
    knowmin = user_input % 3600 // 60
    knowsec = user_input % 3600 % 60
    print(f"{knowhour} ч : {knowmin} мин : {knowsec} сек")
elif user_input >= min:
    knowmin2 = user_input // 60
    knowsec2 = user_input % 60
    print(f"0 ч : {knowmin2} мин : {knowsec2} сек")
else: print(f"0 ч : 0 мин : {user_input} сек")

user_input2 = int(input("Введите любое целое число: "))
n = user_input2
print("Ваше число после преобразования n+n*n+n*n*n, равно: ", n+n*2+n*3)

user_input3 = int(input("Введите целое положительное число: "))
max_number = 0

while user_input3 > 0:
    s = user_input3 % 10
    if s >= max_number:
        max_number = s
    user_input3 //= 10
print(max_number)

ui4 = int(input("Выручка компании за период: "))
ui5 = int(input("Расходы компании за период: "))
fr = ui4 - ui5

if fr > 0:
    print(f"Прибыль за период: {fr}")
    r = fr / ui4 * 100
    print(f"Рентабельность по выручке: {r}%")
    people = int(input("Кол-во сотрудников: "))
    print(f"Прибыль на 1 сотрудника: ", fr // people)

else: print(f"Убыток за период: {fr}")


a = int(input("Километры в 1й день: "))
b = int(input("Итого километров: "))
n = 1

while a < b:
    a = a + (a * 10/100)
    print(a)
    if (n+1) > n:
        n = n + 1
    if a >= b:
        print(f"На {n} день спортсмен достиг результата {b} км")


