import csv
import json
from collections import OrderedDict


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output. json"


def task() -> None:
    with open (INPUT_FILENAME, "r", newline='', encoding='utf-8') as f: # TODO считать содержимое csv файла
                reader = csv.DictReader(f, delimiter=",")
                data_ = []
                for row in reader:
                    data_.append(OrderedDict (row))
                    with open(OUTPUT_FILENAME,"w") as f:
                        json.dump (data_, f, indent=4, ensure_ascii=False)
    json_output = json. dumps (OUTPUT_FILENAME, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open (OUTPUT_FILENAME) as output_f:
          for line in output_f:
             print (line, end="")