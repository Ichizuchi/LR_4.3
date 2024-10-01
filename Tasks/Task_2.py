from abc import ABC, abstractmethod
import math


class Body(ABC):
    
    @abstractmethod
    def surface_area(self) -> float:
        """Абстрактный метод для вычисления площади поверхности"""
        pass

    @abstractmethod
    def volume(self) -> float:
        """Абстрактный метод для вычисления объема"""
        pass

    @abstractmethod
    def display(self):
        """Абстрактный метод для вывода информации о теле"""
        pass


# Производный класс Parallelepiped (Параллелепипед)
class Parallelepiped(Body):
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self) -> float:
        """Вычисление площади поверхности параллелепипеда"""
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def volume(self) -> float:
        """Вычисление объема параллелепипеда"""
        return self.length * self.width * self.height

    def display(self):
        """Вывод информации о параллелепипеде"""
        print(f"Параллелепипед: длина = {self.length}, ширина = {self.width}, высота = {self.height}")
        print(f"Площадь поверхности = {self.surface_area():.2f}")
        print(f"Объем = {self.volume():.2f}")


# Производный класс Ball (Шар)
class Ball(Body):
    def __init__(self, radius: float):
        self.radius = radius

    def surface_area(self) -> float:
        """Вычисление площади поверхности шара"""
        return 4 * math.pi * self.radius ** 2

    def volume(self) -> float:
        """Вычисление объема шара"""
        return (4 / 3) * math.pi * self.radius ** 3

    def display(self):
        """Вывод информации о шаре"""
        print(f"Шар: радиус = {self.radius}")
        print(f"Площадь поверхности = {self.surface_area():.2f}")
        print(f"Объем = {self.volume():.2f}")


def show_body_info(body: Body):
    body.display()


if __name__ == '__main__':
    parallelepiped = Parallelepiped(length=3, width=4, height=5)
    ball = Ball(radius=2)

    show_body_info(parallelepiped)
    print()
    show_body_info(ball)
