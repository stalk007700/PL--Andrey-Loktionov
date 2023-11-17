def s(a):
    a[0], a[-1] = a[-1], a[0]

l = int(input("Введите длину массива: "))
n = []
for i in range(l):
    b= int(input("Введите элемент {i+1}: "))
    n.append(b)

print("Исходный массив:", n)
s(n)
print("Массив после замены:", n)
