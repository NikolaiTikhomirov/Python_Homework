# Требуется вывести все целые степени двойки (т.е. числа вида 2**k),
# не превосходящие числа N.
# Ввод:
# 6
# Вывод
# 1 2 4
# Ввод
# 24
# Вывод
# 1 2 4 8 16

n = int(input('До какого числа вы хотите увидеть целые степени двойки? '))
i = 0
while 2**i <= n:
    print(2**i)
    i += 1
