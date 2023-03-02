# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Введите число')
num = int(input())
result = 0
while num / 10 != 0:
    result = result + int(num % 10)
    num = int(num / 10)
print(result)
