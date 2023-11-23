def f(m):
    a = []
    for i in range(len(m)):
        if i % 2 == 1:  
            b = min(m[i])
            a.append(b)
    return a
def b(n):
    with open(n, 'r') as file:
        ls = file.readlines()
        matr = [[int(k) for k in l.split()] for l in ls]
    return matr

def z(r, n):
    with open(n, 'w') as file:
        file.write(' '.join(map(str, r)) + '\n')

v = 'Loktionov_Andrey_yb-32_v.txt'
vyv = 'Loktionov_Andrey_yb-32_vyv.txt'

matr = b(v)
s = f(matr)
z(s, vyv)
