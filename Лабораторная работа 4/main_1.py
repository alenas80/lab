# TODO решите задачу
import json


def task() -> float:
    with open("input.json") as file:
        json_data = json.load(file)
    dict_sum = sum(proiz["score"] * proiz["weight"] for proiz in json_data)
    return round(dict_sum, 3)

print(task())
