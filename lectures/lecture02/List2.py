# Поиск суммы и среднего арифметического

import random

n = int(input("Введите размер списка: "))
A = []
for i in range(n):
    a = random.randint(1, 9)  # генерация случайного целого числа
    A.append(a)
# обработка
s = sum(A)  # сумма элементов
l = len(A)  # количество элементов
a = s / l  # среднее арифмитическое элементов
# вывод
print("Элементы списка: ")
for i in range(n):
    print(A[i])
print("Сумма элементов: " + str(s))
print("Среднее арифмитическое элементов: " + str(a))