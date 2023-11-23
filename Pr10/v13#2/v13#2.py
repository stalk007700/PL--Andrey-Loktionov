with open('Loktionov_Andrey_yb-32_v.txt', 'r') as file:
    M = [[int(k) for k in line.split(',')] for line in file]

def f(m):
    maxel = m[0][0]
    minel = m[0][0]
    for r in m:
        for el in r:
            if el > maxel:
                maxel = el
            if el < minel:
                minel = el
    return maxel, minel

def s(m):
    maxel, minel = f(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == maxel:
                m[i][j] = minel
            elif m[i][j] == minel:
                m[i][j] = maxel
    return m

sm = s(M)

with open('Loktionov_Andrey_yb-32_vyv.txt', 'w') as file:
    for r in sm:
        file.write(','.join([str(k) for k in r]) + '\n')
