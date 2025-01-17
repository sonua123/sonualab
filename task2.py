BOOKS_DATABASE = [
    {"id": 1, "name": "test_name_1", "pages": 200},
    {"id": 2, "name": "test_name_2", "pages": 400},
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """Класс книги с идентификатором, названием и количеством страниц."""
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Возвращает строку, по которой можно создать такой же объект."""
        return f"Book(id_={self.id_}, name={self.name!r}, pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """Класс библиотеки, хранящий список книг."""
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """Возвращает идентификатор для новой книги."""
        return self.books[-1].id_ + 1 if self.books else 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """Возвращает индекс книги по её ID или вызывает ошибку, если книги нет."""
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if name == "__main__":
    empty_library = Library()  # Создаём пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверяем следующий ID для пустой библиотеки

    books = [Book(**book_data) for book_data in BOOKS_DATABASE]  # Создаём книги из базы
    library_with_books = Library(books=books)  # Создаём библиотеку с книгами

    print(library_with_books.get_next_book_id())  # Проверяем следующий ID для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с ID = 1
