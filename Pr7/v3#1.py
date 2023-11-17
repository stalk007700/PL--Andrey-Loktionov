import math

def l(a, b):
    return math.sqrt(a**2 + b**2)

def s(a1, b1, a2, b2):
    g1 = l(a1, b1)
    g2 = l(a2, b2)
    
    if g1 > g2:
        print("Гипотенуза первого треугольника больше")
    elif g1 < g2:
        print("Гипотенуза второго треугольника больше")
    else:
        print("Гипотенузы равны")
s(3, 4, 5, 12)
