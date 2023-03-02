# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 1 строка - первый список через пробел.
# 2 строка - второй список через пробел.

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list3 = list(set(list1 + list2))
print(list3)
for i in range(len(list3)):
    j = i
    for j in range(len(list3)):
        if list3[j] > list3[i]:
            temp = list3[i]
            list3[i] = list3[j]
            list3[j] = temp
print(list3)
