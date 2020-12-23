from functools import reduce
my_list = [el for el in range(99, 1001) if el%2 == 0]

def result(prev_el, el):

    return el * prev_el

print(reduce(result, my_list))

