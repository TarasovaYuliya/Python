# Поиск минимального элемента в списке

# задаем список
min = [3, 5, 67, -65, 34, 21]
# предположим, что минимальный элемент равен mas[0]
minimum = min[0]
for i in range(1, len(min)):
    if min[i] < minimum:
        minimum = min[i]
print(minimum)
