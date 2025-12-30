import math


def square(side):
    return math.ceil(side * side)


side = float(input("Сторона квадрата: "))
result = square(side)

print(f"Площадь квадрата, округленная в большую сторону: {result}")
