# Требуется определить, можно ли от шоколадки размером
# n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить
# шоколадку на два прямоугольника).

n = int(input("Введите количество долек по длине: "))
m = int(input("Введите количество долек по ширине: "))
k = int(input("Введите количество долек, которые нужно отломить: "))

if (k % n == 0 or k % m == 0) and k < m * n:
    print("yes")
else:
    print("no")
