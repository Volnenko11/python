from sys import argv

name, first_par, second_par, third_par = argv

print("Имя скрипта: ", name)
print("Выработка часов: ", first_par)
print("Ставка в час: ", second_par)
print("Премия: ", third_par)
first_par = int(first_par)
second_par = int(second_par)
third_par = int(third_par)
res = first_par * second_par + third_par
print(res)