# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: 
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# Вывод: same

def same_by(condition, nums):
	return len(set(map(condition, nums))) == 1 # длина множества равна 1
                                               # в множестве одинаковые элементы не отражаются

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

# вар 2 с изменением данного в задаче кода
# def same_by(f, values):
# 	    return  False if 1 in set(map(f, values)) else True