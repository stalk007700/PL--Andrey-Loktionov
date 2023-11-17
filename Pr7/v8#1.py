def ch(n):
    r=[]
    for i in range(1, n+1):
        for a in str(i):
            if int(a) != 0:
                a = [int(a)]
                if all(i % a == 0 for a in a):
                    r.append(i)
    return r
p=ch(100)
print(p)
