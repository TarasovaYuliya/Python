# Поиск максимального элемента в списке

mas = [3, 5, 67, -65, 34, 21] # задаем список
maximum = mas[0] # предположим, что максимальный элемент равен mas[0]
for i in range(1, len(mas)):
    if mas[i] > maximum:
        maximum = mas[i]
print(maximum)
