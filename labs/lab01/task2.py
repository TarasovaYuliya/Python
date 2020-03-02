# В таблице приведены формулы и три варианта исходных данных, по которым надо разработать
# три циклические программы с одними и теми же расчетными формулами.

import numpy

s = 5.9
m = 6
f = 1.2 * 10 ** 3

c = (2, 0.5, 4)
print("FOR:")
for j in range(len(c)):
    y = (s + c[j]) / numpy.log(f) / numpy.e ** (-s)
    h = (y - m) / numpy.log(y)
    print(h)
print("")

c = 0
print("WHILE:")
while c <= 0.9:
    y = (s + c) / numpy.log(f) / numpy.e ** (-s)
    h = (y - m) / numpy.log(y)
    c += 0.1
    print(h)
print("")

s = (-3, 0.8, 4)
c = 0.2
print("ДВОЙНОЙ ЦИКЛ:")
for n in range(len(s)):
    while c <= 0.5:
        y = (s[n] + c) / numpy.log(f) / numpy.e ** (-s[n])
        h = (y - m) / numpy.log(-y)
        c += 0.1
        print(h)
