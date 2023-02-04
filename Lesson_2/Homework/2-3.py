#  Требуется вывести все целые степени двойки
#  (т.е. числа вида 2k), не превосходящие числа N.

n = int(input())
count = 1

while count <= n:
    print(count)
    count *= 2
    
