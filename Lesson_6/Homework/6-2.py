# Определить индексы элементов массива (списка), значения
# которых принадлежат заданному диапазону (т.е. не меньше
# заданного минимума и не больше заданного максимума)

a = list(map(int, input().split()))
min = int(input())
max = int(input())
b = []
for i in range(len(a)):
    if a[i] > min and a[i] < max:
        b.append(i)
print(b)
