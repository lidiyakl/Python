# Дан массив, состоящий из целых чисел. Напшите программу,
# которая в данном массиве определит количество эл-тов,
# у которых оба соседних элемента меньше данного.

a = list(map(int, input().split()))
count = 0
for i in range(1, len(a) - 1):
    if a[i] == max(a[i - 1 : i + 2]):
        count += 1
print(count)

# вар 2
# print(len([i for i in range(1, len(a) - 1) if a[i] > a[i - 1] and a[i] > a[i + 1]]))

# вар 3
# print(len([i for i in range(1, len(a) - 1) if a[i] == max(a[i - 1 : i + 2])]))
