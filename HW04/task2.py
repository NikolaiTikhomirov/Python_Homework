# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод –
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном списке,
# содержащим количество ягод на кустах.

# Input: 2 2 1 3 2
# Output: 7

circle_list = list(map(int, input().split()))
res = 0
# len_ = len(circle_list)
for i in range(len(circle_list)):
    # if i == 1:
    #     if res < circle_list[i] + circle_list[len_-1] + circle_list[len_-1]:
    #         res = circle_list[i] + circle_list[len_-1] + circle_list[len_-1]
    # if i == 0:
    #     if res < circle_list[i] + circle_list[len_-1] + circle_list[len_-2]:
    #         res = circle_list[i] + circle_list[len_-1] + circle_list[len_-2]
    if res < circle_list[i] + circle_list[i-1] + circle_list[i-2]:
        res = circle_list[i] + circle_list[i-1] + circle_list[i-2]
print(res)
