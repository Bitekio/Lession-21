""" Homework """


class Circle:
    """
    Класс, представляющий окружность.
    """

    def __init__(self, radius):
        """
        Инициализация окружности с заданным радиусом.
        """
        self.radius = radius

    def __eq__(self, other):
        """
        Проверка равенства радиусов двух окружностей.
        """
        return self.radius == other.radius

    def __gt__(self, other):
        """
        Сравнение радиусов двух окружностей (больше).
        """
        return self.radius > other.radius

    def __lt__(self, other):
        """
        Сравнение радиусов двух окружностей (меньше).
        """
        return self.radius < other.radius

    def __le__(self, other):
        """
        Сравнение радиусов двух окружностей (меньше или равно).
        """
        return self.radius <= other.radius

    def __ge__(self, other):
        """
        Сравнение радиусов двух окружностей.
        """
        return self.radius >= other.radius

    def __add__(self, other):
        """
        Пропорциональное увеличение размера окружности.
        """
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        """
        Пропорциональное уменьшение размера окружности.
        """
        result = self.radius - other.radius
        if result < 0:
            return Circle(0)
        else:
            return Circle(result)

    def __iadd__(self, other):
        """
        Пропорциональное увеличение размера окружности с присваиванием.
        """
        self.radius += other.radius
        return self

    def __isub__(self, other):
        """
        Пропорциональное уменьшение размера окружности с присваиванием.
        """
        self.radius = max(0, self.radius - other.radius)
        return self

    def __str__(self):
        """
        Возвращает строковое представление окружности.
        """
        return "Окружность с радиусом " + str(self.radius)


circle1 = Circle(5)
circle2 = Circle(7)

print(circle1 == circle2)
print(circle1 > circle2)
print(circle1 < circle2)
print(circle1 <= circle2)
print(circle1 >= circle2)

circle3 = circle1 + circle2
print(circle3)

circle4 = circle2 - circle1
print(circle4)

circle1 += Circle(3)
print(circle1)

circle2 -= Circle(2)
print(circle2)
