# 2. Создайте итерируемый объект, возвращающий генератор чисел из ряда Лейбница,
# возвращающий новые элементы до тех пор, пока сумма полученных элементов не приблизится
# к ожидаемой сумме ряда с точностью в 2 знака после и выведите эти числа.
import math


class Leibniz:
    L = []

    def listSum(L):
        theSum = 0
        for i in L:
            theSum += i
        return theSum

    def __init__(self):
        i = 0
        while float("%.2f" % (math.pi/4 - Leibniz.listSum(Leibniz.L))) != 0.00:
            Leibniz.L.append((-1) ** i / (2 * i + 1))
            i += 1
        print("На", i, "элементе сумма полученных элементов приблизилась к ожидаемой сумме ряда с точностью в 2 знака")

    def __iter__(self):
        for i in range(len(Leibniz.L)):
            yield Leibniz.L[i]


List = Leibniz()
print("Сумма ряда = pi/4 = ", math.pi/4)
print("Сумма элементов ряда = ", Leibniz.listSum(List))
print("Ряд Лейбница:")
for number in List:
    print(number, end=' ')
