# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

num_lst = list(map(int, input().split()))
min_num = int(input())
max_num = int(input())


def is_in_mass(num_lst: list[int],
               min_num: int,
               max_num: int) -> list[int]:
    """Возвращает список индексов элементов списка, которые
    находятся в диапазоне [min_num,max_num] """

    res = []
    for i in range(len(num_lst)):
        if min_num <= num_lst[i] <= max_num:
            res.append(i)
    return res


print(is_in_mass(num_lst, min_num, max_num))
