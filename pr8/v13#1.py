def f(m):
    a = []
    for i in range(len(m)):
        if i % 2 == 1:  
            b = min(m[i])
            a.append(b)
    return a
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
s = f(M)
print(s)
