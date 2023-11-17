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
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

sm=s(M)
print(sm)
