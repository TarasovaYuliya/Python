# Поиск произведения и среднего геометрического

import random
n = int(input("Введите размер списка: "))
A = []
for i in range(n):
    a = random.randint(1, 9)  # генерация случайного целого числа
    A.append(a)
# обработка
# произведение элементов
p = 1
for i in range(n):
    p *= A[i]
l = len(A)  # количество элементов
a = p ** (1 / l)  # среднее геометрическое элементов
# вывод
print("Элементы списка: ")
for i in range(n):
    print(A[i])
print("Произведение элементов: " + str(p))
print("Среднее геометрическое элементов: " + str(a))
