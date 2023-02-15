# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).


def pair(value):
    sq_num = int(value**0.5)
    res = 1 + (0 if sq_num**2 != value else sq_num)
    for i in range(2, sq_num):
        if value % i == 0:
            res += i + value // i
    return res


for j in range(10, 301):
    sum1 = pair(j)
    sum2 = pair(sum1)
    if sum2 == j and sum1 < sum2:
        print(j, sum1)