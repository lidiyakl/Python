# Определить индексы элементов массива (списка), значения
# которых принадлежат заданному диапазону (т.е. не меньше
# заданного минимума и не больше заданного максимума)

a = list(map(int, input().split())) # =[int(i) for i in input().split()]
min = int(input())
max = int(input())
b = []
for i in range(len(a)):
    if a[i] >= min and a[i] <= max:
        b.append(i)
print(b)

# print([ind for ind, val in enumerate(a) if min <= val <= max])
# enumerate собирает кортежи из элементов(val) и их индексов(ind).
# Мы выводим только индексы(ind) элементов, соответствующих условию.