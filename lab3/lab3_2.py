def find_common_participants(group1, group2, delimiter=','):
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    set1 = set(participants1)
    set2 = set(participants2)

    common_participants = sorted(list(set1.intersection(set2)))

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, '|')
