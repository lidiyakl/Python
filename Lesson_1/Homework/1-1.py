# Найдите сумму цифр трехзначного числа.

n = int(input("Введите число: "))
res = 0

while n > 0:
    res = res + n % 10
    n = n // 10

print(res)