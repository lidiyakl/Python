# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов 
# сделал каждый ребенок, если известно, что Петя и 
# Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int(input("Введите количество журавликов: "))
if s % 2 or (s // 2) % 2:
    print("Введенное число некорректно!")
else:
    print(s//6, s//6*4, s//6)