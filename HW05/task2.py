# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

a = int(input())
b = int(input())


def find_sum(a, b):
    if a == 0 and b == 0:
        return 0
    if a >= b:
        return find_sum(a - 1, b) + 1
    if b > a:
        return find_sum(a, b - 1) + 1


print(find_sum(a, b))
