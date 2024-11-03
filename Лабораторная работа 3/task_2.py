# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, n=","):
    first_group = set(first.split(n))
    second_group = second.split(n)
    intersection_group = list(first_group.intersection(second_group))
    intersection_group.sort()
    return intersection_group

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
