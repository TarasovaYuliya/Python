# 1. Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и выведите эти числа.

size = input('Введите количество чисел трибоначчи для вывода: ')
size = int(size)


class GlobalValues:
    L = [0, 0, 1]


class Threebonachi:

    def __init__(self):
        i = 3

        while i < size + 1:
            GlobalValues.L.append(GlobalValues.L[i - 1] + GlobalValues.L[i - 2] + GlobalValues.L[i - 3])
            i += 1

    def __iter__(self):
        for i in range(size):
            yield GlobalValues.L[i]


List = Threebonachi()
for number in List:
    print(number, end=' ')
