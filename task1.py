BOOKS_DATABASE = [
    {"id": 1, "name": "test_name_1", "pages": 200},
    {"id": 2, "name": "test_name_2", "pages": 400},
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name={self.name!r}, pages={self.pages})"


if name == "__main__":
    # Создаём список объектов Book из BOOKS_DATABASE
    books = [Book(**book_data) for book_data in BOOKS_DATABASE]

    # Проверяем метод str
    for book in books:
        print(book)

    # Проверяем метод repr
    print(books)ниги с id=1)