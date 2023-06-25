# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
a = input("Введите первую дробь: ")
b = input("Введите вторую дробь: ")
def dr (drob):
    a = drob.split('/')
    res = int(a[0]) / int(a[1])
    return res

amount = dr(a) + dr(b)
composition = dr(a) * dr(b)

print(a, '+', b, '=', amount)
print(a, '*', b, '=', composition)

from fractions import Fraction as F
a = input()
b = input()

print(a, '+', b, '=', F(a)+F(b))
print(a, '*', b, '=', F(a)*F(b))