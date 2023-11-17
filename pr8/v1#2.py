def s(m):
    for r in m:
        maxel = max(r)
        minel = min(r)
        maxi = r.index(maxel)
        mini = r.index(minel)
        r[0], r[maxi] = r[maxi], r[0]
        r[-1], r[mini] = r[mini], r[-1]
M = [[3, 1, 4],
     [5, 2, 6],
     [7, 7, 8]]
s(M)
print(M)
