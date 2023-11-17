def s(a):
    ts = 0
    cp = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i][j] > 0:
                ts += a[i][j]
                cp += 1
    return ts, cp

M = [[1, 2, -3],
     [-4, 5, 6],
     [-7, 8, 9]]

ts, cp = s(M)
print("Сумма положительных элементов над главной диагональю:", ts)
print("Количество положительных элементов над главной диагональю:", cp)
