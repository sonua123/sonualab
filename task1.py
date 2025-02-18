from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Базовый класс, представляющий животное.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Конструктор класса Animal.

        :param name: Имя животного
        :param age: Возраст животного
        """
        self._name = name  # Закрытый атрибут, так как имя не должно изменяться напрямую
        self.age = age

    def __str__(self) -> str:
        """
        Магический метод для строкового представления объекта.
        """
        return f"{self.__class__.__name__} по имени {self._name}, возраст: {self.age}"

    def __repr__(self) -> str:
        """
        Магический метод для технического представления объекта.
        """
        return f"{self.__class__.__name__}('{self._name}', {self.age})"

    @abstractmethod
    def make_sound(self) -> str:
        """
        Абстрактный метод, который должны реализовать все дочерние классы.
        """
        pass


class Dog(Animal):
    """
    Класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Dog. Расширяет базовый класс Animal.

        :param name: Имя собаки
        :param age: Возраст собаки
        :param breed: Порода собаки
        """
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        """
        Реализация абстрактного метода. Собака лает.
        """
        return "Гав-гав!"

    def __str__(self) -> str:
        """
        Переопределение метода str для добавления информации о породе собаки.
        """
        return f"Собака породы {self.breed} по имени {self._name}, возраст: {self.age}"


class Cat(Animal):
    """
    Класс, представляющий кошку.
    """

    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Конструктор класса Cat. Расширяет базовый класс Animal.

        :param name: Имя кошки
        :param age: Возраст кошки
        :param color: Цвет шерсти кошки
        """
        super().__init__(name, age)
        self.color = color

    def make_sound(self) -> str:
        """
        Реализация абстрактного метода. Кошка мяукает.
        """
        return "Мяу!"

    def __str__(self) -> str:
        """
        Переопределение метода str для добавления информации о цвете кошки.
        """
        return f"Кошка {self.color} цвета по имени {self._name}, возраст: {self.age}"