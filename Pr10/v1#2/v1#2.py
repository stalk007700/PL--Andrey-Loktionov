def s(m):
    for r in m:
        maxel = max(r)
        minel = min(r)
        maxi = r.index(maxel)
        mini = r.index(minel)
        r[0], r[maxi] = r[maxi], r[0]
        r[-1], r[mini] = r[mini], r[-1]
def b(n):
    with open(n, 'r') as file:
        ls = file.readlines()
        m = [[int(k) for k in l.split()] for l in ls]
    return m

def z(m, n):
    with open(n, 'w') as file:
        for r in m:
            file.write(' '.join(map(str, r)) + '\n')

v = 'Loktionov_Andrey_yb-32_v.txt'
vyv = 'Loktionov_Andrey_yb-32_vyv.txt'

m = b(v)
s(m)
z(m, vyv)
