# Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность).

# n = int(input())
# max_number = 0
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

n = int(input())
max_number = -1
while n > 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)
