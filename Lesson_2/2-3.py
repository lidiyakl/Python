# Уставшие от необычно теплой зимы жители решили узнать,
# действительно ли это самая длинная оттепель за всю
# историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованием статистики
# за прошлые годы. Их интересует, сколько дней длилась
# самая длинная оттепель. Оттепелью называют период, в
# который среднесуточная температура ежедневно превышал
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N - общее количество
# рассматриваемых дней (1 <= N <=100). В следующих строках
# располагается N целых чисел.
# Каждое число - среднесуточная температура в соответствующий
# день. Температуры - целые числа и лежат в диапазоне от -50
# до 50.

n = int(input())
count = 0
max = 0
for i in range(n):
    temp = int(input())
    if temp > 0:
        count += 1
    else:
        if count > max:
            max = count
        count = 0
print(max)