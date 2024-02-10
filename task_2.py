""" Homework """

class Complex:
    """Класс для представления комплексных чисел."""

    def __init__(self, real, imag):
        """Инициализация комплексного числа с заданными действительной и мнимой частями."""
        self.real = real
        self.imag = imag

    def __str__(self):
        """Возвращает строковое представление комплексного числа."""
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __add__(self, other):
        """Сложение двух комплексных чисел."""
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """Вычитание двух комплексных чисел."""
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """Умножение двух комплексных чисел."""
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        """Деление двух комплексных чисел."""
        denominator = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)


if __name__ == "__main__":
    c1 = Complex(2, 3)
    c2 = Complex(1, -1)

    print("c1 =", c1)
    print("c2 =", c2)
    print("c1 + c2 =", c1 + c2)
    print("c1 - c2 =", c1 - c2)
    print("c1 * c2 =", c1 * c2)
    print("c1 / c2 =", c1 / c2)
