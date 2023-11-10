 # №1
def task(a, b, c, n):
    lst = [2, 2, 1]  # список из цифр
    count = 0
    for i1 in lst:  # каждая цифра должна побывать на 1-м месте
        for i2 in lst:  # каждая цифра должна побывать на 2-м месте
            for i3 in lst:  # каждая цифра должна побывать на 3-м месте
                z = i3 * 100 + i2 * 10 + i1  # воспроизводим число
                if z >= 100 and z <= n:  # проверяем
                    count += 1
    return count

print(task(1, 2, 3, 900))

# №2
def str_rvs (str):
    word = str.split()  # Разбиваем строку на слова
    str_rvs  = ' '.join(reversed(word)) # Переворачиваем порядок слов и объединяем их обратно
    return str_rvs

str = input('Введите строку:')
res = str_rvs(str) # Вызов ф-ции и вывод результата
print('Результат:', res)
