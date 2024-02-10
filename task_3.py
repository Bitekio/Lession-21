""" Homework """


class Airplane:
    """Класс для представления самолета."""

    def __init__(self, model, max_passengers, current_passengers):
        """Инициализация самолета с заданныой моделью"""
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        """Проверка на равенство моделей самолетов."""
        return self.model == other.model

    def __add__(self, passengers):
        """Добавление пассажиров в салон самолета."""
        if self.current_passengers + passengers <= self.max_passengers:
            self.current_passengers += passengers
        else:
            print("Невозможно добавить больше пассажиров. Достигнута максимальная вместимость.")

    def __sub__(self, passengers):
        """Уменьшение количества пассажиров в салоне самолета."""
        if self.current_passengers - passengers >= 0:
            self.current_passengers -= passengers
        else:
            print("Невозможно удалить больше пассажиров. В самолете нет пассажиров.")

    def __iadd__(self, passengers):
        """Увеличение количества пассажиров в салоне самолета с помощью оператора '+='."""
        self.__add__(passengers)
        return self

    def __isub__(self, passengers):
        """Уменьшение количества пассажиров в салоне самолета с помощью оператора '-='."""
        self.__sub__(passengers)
        return self

    def __gt__(self, other):
        """Сравнение двух самолетов по максимально возможному количеству пассажиров на борту."""
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        """Сравнение двух самолетов по максимально возможному количеству пассажиров на борту."""
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        """Сравнение двух самолетов по максимально возможному количеству пассажиров на борту."""
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        """Сравнение двух самолетов по максимально возможному количеству пассажиров на борту."""
        return self.max_passengers <= other.max_passengers


if __name__ == "__main__":
    plane1 = Airplane("Boeing 747", 500, 200)
    plane2 = Airplane("Airbus A380", 600, 300)

    print("Are planes of the same model?", plane1 == plane2)

    plane1 += 50
    print("Current passengers in plane 1:", plane1.current_passengers)

    plane2 -= 100
    print("Current passengers in plane 2:", plane2.current_passengers)

    print("Plane 1 has more seats than plane 2?", plane1 > plane2)
    print("Plane 1 has less seats than or equal to plane 2?", plane1 <= plane2)
