# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input())
min = max = 0
for _ in range(n):
    count = int(input())
    if count == 1:
        max += 1
    else:
        min += 1
if max < min:
    print(max)
else:
    print(min)
