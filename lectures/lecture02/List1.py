# Генерация списка случайных чисел от 0 до 1 заданного размера

import random
n = int(input("Введите размер списка: "))  # ввод
A = []  # создание пустого списка
for i in range(n):
    a = random.random()  # генерация случайного числа
    A.append(a)  # добавления числа в список
# вывод
for i in range(n):
    print(A[i])
