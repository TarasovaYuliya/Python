import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def ShakerSort(A):  # функция шейкерной (коктейльной) сортировки
    for i in range(0, int(len(A) / 2)):
        for j in range(i, len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
        for j in range(len(A) - 2 - i, i, -1):
            if A[j] < A[j - 1]:
                a = A[j]
                A[j] = A[j - 1]
                A[j - 1] = a


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a


def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    pivot = A[fst]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время шейкерной"])
x = []
y1 = []
y2 = []
y3 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    print("Исходный массив: " + str(A))
    B = A.copy()
    C = A.copy()

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("A = " + str(A))
    # print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B) - 1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("B = " + str(B))
    # print("Быстрая   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    ShakerSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("C = " + str(C))

    table.add_row(
        [str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C8")
plt.show()
