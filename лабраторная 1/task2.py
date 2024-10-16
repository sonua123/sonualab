# TODO Найдите количество книг, которое можно разместить на дискете

pages = 100
lines = 50
chars = 25
bytes = 4

book_size = pages * lines * chars * bytes

disk_size = 1.44
disk_size_bytes = disk_size * 1024 * 1024

number_of_books = disk_size_bytes // book_size

print("Количество книг, помещающихся на дискету:", int(number_of_books))
