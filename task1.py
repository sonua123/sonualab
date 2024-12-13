import doctest


class Car:
    def __init__(self, model: str, engine_power: (int, float), max_speed: (int, float)):
        """
        Создание и подготовка к работе объекта "Автомобиль".
        :param model: Модель автомобиля.
        :param engine_power: Мощность двигателя в лошадиных силах.
        :param max_speed: Максимальная скорость в км/ч.

        Примеры:
        >>> car1 = Car('Toyota', 150, 200)  # инициализация экземпляра класса
        """
        if not isinstance(max_speed, (int, float)):
            raise TypeError('Только численные значения для параметра "максимальная скорость".')
        if max_speed < 0:
            raise ValueError('"Максимальная скорость" должна быть неотрицательным числом.')
        self.max_speed = max_speed

        if not isinstance(model, str):
            raise TypeError('Название модели должно быть строкой.')
        if len(model) == 0:
            raise ValueError('Название модели не может быть пустой строкой.')
        self.model = model

        if not isinstance(engine_power, (int, float)):
            raise TypeError('Только численные значения для параметра "мощность двигателя".')
        if engine_power < 0:
            raise ValueError('"Мощность двигателя" должна быть неотрицательным числом.')
        self.engine_power = engine_power

    def drive(self, distance: int) -> None:
        """
        Функция, которая позволяет автомобилю проехать заданное расстояние.
        :param distance: Расстояние для поездки в километрах.
        :raise ValueError: Если заданное расстояние отрицательное.

        Примеры:
        >>> car1 = Car('Toyota', 150, 200)
        >>> car1.drive(100)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError('Расстояние должно быть числом.')
        if distance < 0:
            raise ValueError('Расстояние не может быть отрицательным.')
        print(f'Автомобиль {self.model} проехал {distance} км.')

    def accelerate(self) -> None:
        """
        Функция, позволяющая автомобилю ускоряться до максимальной скорости.

        Примеры:
        >>> car1 = Car('Toyota', 150, 200)
        >>> car1.accelerate()
        """
        print(f'Автомобиль {self.model} ускоряется до {self.max_speed} км/ч.')

    def change_model(self, new_model: str) -> None:
        """
        Функция, позволяющая сменить модель автомобиля.
        :param new_model: Новое название модели автомобиля.
        :raise TypeError: Если введён неправильный тип данных.
        :raise ValueError: Если введена пустая строка.

        Примеры:
        >>> car1 = Car('Toyota', 150, 200)
        >>> car1.change_model('Honda')
        """
        if not isinstance(new_model, str):
            raise TypeError('Название модели должно быть строкой.')
        if len(new_model) == 0:
            raise ValueError('Название модели не может быть пустой строкой.')
        self.model = new_model
        print(f'Модель автомобиля изменена на {self.model}.')


if name == "__main__":
    # Проверка работоспособности экземпляров класса с помощью doctest
    doctest.testmod()