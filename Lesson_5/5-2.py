# Написать программу, которая заменяет все максимальные
# оценки на минимальные в школьном журнале.


def max_to_min(list):
    Min = min(list)
    Max = max(list)
    return [Min if i == Max else i for i in list]


print(*max_to_min([int(i) for i in input().split()]))
