numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
def replace_missing_with_average(numbers):
    missing_index = numbers.index(None)
    numbers_w = [num for num in numbers if num is not None]
    t_sum = sum(numbers_w)
    count = len(numbers)
    average = t_sum / (count)
    numbers[missing_index] = average
    return numbers
result = replace_missing_with_average(numbers)
print("Измененный список:", result)

