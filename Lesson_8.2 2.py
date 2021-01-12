class VolnenkoError(Exception):
    pass


def get_numerator() -> int:
    return int(input("Числитель: "))


def get_denominator() -> int:
    value = int(input("Знаменатель: "))

    if value == 0:
        raise VolnenkoError

    return value


while True:
    try:
        numerator = get_numerator()
        denominator = get_denominator()

        print(f"Отлично! Результат = {numerator / denominator}")
    except VolnenkoError:
        print("0 в качестве знаменателя? Переделывай!")
    except KeyboardInterrupt:
        break