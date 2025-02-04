class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name  # защищенный атрибут
        self._author = author  # защищенный атрибут

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    def __str__(self) -> str:
        return f"Книга: {self.name}, Автор: {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Дочерний класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер с проверками

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Устанавливает количество страниц в книге с проверкой."""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self._pages = pages

    def __str__(self) -> str:
        return f"Бумажная книга: {self.name}, Автор: {self.author}, Страниц: {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Дочерний класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем сеттер с проверками

    @property
    def duration(self) -> float:
        """Возвращает продолжительность книги."""
        return self._durationclass
        Book: """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name  # защищенный атрибут
        self._author = author  # защищенный атрибут

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    def __str__(self) -> str:
        return f"Книга: {self.name}, Автор: {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Дочерний класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер с проверками

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Устанавливает количество страниц в книге с проверкой."""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self._pages = pages

    def __str__(self) -> str:
        return f"Бумажная книга: {self.name}, Автор: {self.author}, Страниц: {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Дочерний класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем сеттер с проверками

    @property
    def duration(self) -> float:
        """Возвращает продолжительность книги."""
        return self._duration
