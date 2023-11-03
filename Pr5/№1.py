a=input("Введите текст: ")
w=a.split()
c= 0
for w in w:
    if w.lower().startswith('е'):
        c+=1
print("Количество слов, начинающихся с 'е':", c)
