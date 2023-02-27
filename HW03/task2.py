# Требуется найти в массиве из случайных чисел (от 1 до n)
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
arrayLegth = int(input('Какой длины будет массив? '))
array = []
for i in range(arrayLegth):
    array.append(int(randint(1, arrayLegth)))
num = int(input('Введите число X, будем искать ближайшее к нему. '))
nearestValue = arrayLegth
for i in range(len(array)):
    if abs(array[i] - num) < nearestValue:
        nearestElement = array[i]
        nearestValue = abs(array[i] - num)
print(array)
print(nearestElement)
