def s(a):
    ts = 0
    cp = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i][j] > 0:
                ts += a[i][j]
                cp += 1
    return ts, cp
v = "Loktionov_Andrey_yb-32_v.txt"
vyv = "Loktionov_Andrey_yb-32_vyv.txt"

a = []
with open(v, 'r') as file:
    for l in file:
        r = [int(x) for x in l.split()]
        a.append(r)

ts, cp = s(a)

with open(vyv, 'w') as file:
    file.write("Сумма положительных элементов над главной диагональю: " + str(ts) + "\n")
    file.write("Количество положительных элементов над главной диагональю: " + str(cp))
