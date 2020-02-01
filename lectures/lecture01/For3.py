# Задача: расчет степеней двойки от 0 до 0.5 с шагом 0.1

import numpy
for x in numpy.arange(0.0, 0.6, 0.1):
    y = 2 ** x
    print(y)
