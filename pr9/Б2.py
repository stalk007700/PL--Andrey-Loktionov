def f():
    m1 = m2 = 0    
    while True:
        k = int(input("Введите натуральное число: "))        
        if k == 0:
            break        
        if k > m1:
            m2 = m1
            m1 = k
        elif k > m2:
            m2 = k   
    return m2
r = f()
print("Второе по величине число:",r)
