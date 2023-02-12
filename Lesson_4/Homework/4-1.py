# Даны два неупорядоченных набора целых чисел (может быть,
# с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь
# вводит сами элементы множеств

n = int(input())
m = int(input())
num = set(input() for _ in range(n))
mn = set(input() for _ in range(m))

print(sorted(num.intersection(mn)))