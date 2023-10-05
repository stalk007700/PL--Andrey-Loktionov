n = int(input("Введите натуральное число n (n ≤ 9): "))

if n > 9 or n < 1:
    print()
else:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()  
