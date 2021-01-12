class Date:
    day: int
    month: int
    year: int

    def __init__(self, date_string: str):
        numbers = Date.extract_numbers(date_string)
        self.validate_numbers(numbers)

        self.day, self.month, self.year = numbers

    @classmethod
    def extract_numbers(cls, date_string: str) -> list:
        return [int(x) for x in date_string.split('-')]

    @staticmethod
    def validate_numbers(numbers: list):
        d, m, y = numbers

        assert 1 <= d <= 31, "Неверное число"
        assert 1 <= m <= 12, "Неверный месяц"
        assert 1865 <= y <= 2100, "Неверный год"


my_date = Date('19-12-2005')