#Напишите программу, которая вычисляет площадь
#круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
#не менее 42 знаков после запятой.

from math import pi
import decimal

def circle(d: decimal) -> tuple[decimal, decimal]:
    decimal.getcontext().prec = 42
    _pi = decimal.Decimal(pi)
    if d <= 1000:
        s= (_pi * d**2) / 4
        l = _pi * d

    return decimal.Decimal(s), decimal.Decimal(l)

print(circle(decimal.Decimal(34)))
    
#Напишите программу, которая решает квадратные уравнения даже если
#дискриминант отрицательный.
#Используйте комплексные числа для извлечения квадратного корня.
    
