#Проверить, является ли дробь A / B правильной.

A = int(input("Введите числитель дроби (A): "))
B = int(input("Введите знаменатель дроби (B): "))

if A < B:
    print("Дробь правильная")
else:
    print("Дробь неправильная")