# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым.
# Простое число - это число, которое имеет 2 делителя:
# 1 и само число.


def simple(n):
    if n == 2:
        return "Yes"
    elif n == 1 or n % 2 == 0:
        return "No"
    for i in range(3, int((n**0.5) + 1), 2):
        if n % i == 0:
            return "No"
    return "Yes"


print(simple(int(input())))
