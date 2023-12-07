import json
import requests
import tkinter as tk

def a():
    name = e.get()
    url = f'https://api.github.com/repos/{name}'
    n = requests.get(url)
    k = n.json()

    d = {
        'company': k.get('company', 'None'),
        'created_at': k.get('created_at', 'None'),
        'email': k.get('email', 'None'),
        'id': k.get('id', 'None'),
        'name': k.get('name', 'None'),
        'url': k.get('url', 'None')
    }
    
    file=open('Andrey_Loktionov.json', 'w')
    json.dump(d, file, indent=1)

# gui
g = tk.Tk()
g.title('Локтионов Андрей Алексеевич')
g.geometry("400x400")

label = tk.Label(g, text='Введите имя репозитория:')
label.pack()

e = tk.Entry(g)
e.pack()

button = tk.Button(g, text='Выполнить', command=a)
button.pack()

g.mainloop()
