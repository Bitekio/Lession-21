""" Homework """


class Flat:
    """Класс для представления квартиры."""

    def __init__(self, area, price):
        """Инициализация квартиры с заданной площадью и ценой."""
        self.area = area  # площадь
        self.price = price  # цена

    def __eq__(self, other):
        """Проверка на равенство площадей квартир."""
        return self.area == other.area

    def __ne__(self, other):
        """Проверка на неравенство площадей квартир."""
        return self.area != other.area

    def __gt__(self, other):
        """Сравнение двух квартир по цене."""
        return self.price > other.price

    def __lt__(self, other):
        """Сравнение двух квартир по цене."""
        return self.price < other.price

    def __ge__(self, other):
        """Сравнение двух квартир по цене."""
        return self.price >= other.price

    def __le__(self, other):
        """Сравнение двух квартир по цене."""
        return self.price <= other.price


if __name__ == "__main__":
    flat1 = Flat(100, 100000)
    flat2 = Flat(120, 120000)

    print("Площади квартир равны?", flat1 == flat2)
    print("Площади квартир не равны?", flat1 != flat2)
    print("Квартира 2 дороже квартиры 1?", flat2 > flat1)
