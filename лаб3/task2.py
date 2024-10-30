def find_common_participants(group1: str, group2: str, delimiter: str = ',') -> list:
    # Разделяем строки на элементы по заданному разделителю
    participants_group1 = set(group1.split(delimiter))
    participants_group2 = set(group2.split(delimiter))

    # Находим общие элементы
    common_participants = sorted(participants_group1 & participants_group2)

    return common_participants


# Проверим работу функции с разделителем отличным от запятой
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
