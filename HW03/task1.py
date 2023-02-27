# Требуется вычислить, сколько раз встречается некоторое число X
# в массиве из случайных чисел.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

arrayLegth = int(input('Какой длины будет массив? '))
array = []
for i in range(arrayLegth):
    array.append(int(randint(0, 5)))
num = int(input('Какое число вы хотите искать в массиве? '))
count = 0
for i in range(len(array)):
    if array[i] == num:
        count += 1
print(array)
print(count)
