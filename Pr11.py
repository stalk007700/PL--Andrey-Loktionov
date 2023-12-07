import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


def calk():
    a = e1.get()
    b = e2.get()
    c = cb.get()
    if c == '+':
        r = int(a) + int(b)
        t.delete(0, tk.END)
        t.insert(0, r)
    elif c == '-':
        r = int(a) - int(b)
        t.delete(0, tk.END)
        t.insert(0, r)
    elif c == '*':
        r = int(a) * int(b)
        t.delete(0, tk.END)
        t.insert(0, r)
    else:
        r = int(a) / int(b)
        t.delete(0, tk.END)
        t.insert(0, r)


def ChekBoks():
    message = ''
    if y1.get() == 1:
        message += 'Выбран_вариант_1; '
    if y2.get() == 1:
        message += 'Выбран_вариант_2; '
    if y3.get() == 1:
        message += 'Выбран_вариант_3; '
    messagebox.showinfo('Вы выбрали', message)


def of():
    fr = filedialog.askopenfilename()
    with open(fr, 'r', encoding='utf-8') as dok:
        text.delete(1.0, tk.END)
        text.insert(tk.END, dok.read())


win = tk.Tk()
win.title('Вкладка')
win.geometry('500x500')


nb = ttk.Notebook(win)
nb.pack(pady=10, padx=10)  


tb1 = ttk.Frame(nb)
tb2 = ttk.Frame(nb)
tb3 = ttk.Frame(nb)

nb.add(tb1, text="Калькулятор")
nb.add(tb2, text="Чекбоксы")
nb.add(tb3, text="Работа с текстом")

e1 = tk.Entry(tb1, width=10)
e1.grid(row=0, column=0)

cb = ttk.Combobox(tb1, width=3)
cb['values'] = ('+', '-', '*', '/')
cb.current(0)  
cb.grid(row=0, column=1)

e2 = tk.Entry(tb1, width=10)
e2.grid(row=0, column=2)

p1 = tk.Button(tb1, text='=', command=calk)
p1.grid(row=0, column=3)

t = tk.Entry(tb1, width=10)
t.grid(row=0, column=4)

l2 = tk.Label(tb1)
l2.grid(row=0, column=5)

y1 = tk.IntVar()
y2 = tk.IntVar()
y3 = tk.IntVar()

ch1 = tk.Checkbutton(tb2, text='Первый', variable=y1)
ch2 = tk.Checkbutton(tb2, text='Второй', variable=y2)
ch3 = tk.Checkbutton(tb2, text='Третий', variable=y3)

ch1.grid(row=1, column=0)
ch2.grid(row=2, column=0)
ch3.grid(row=3, column=0)

p2 = tk.Button(tb2, text='Выбрать', command=ChekBoks)
p2.grid(row=2, column=1)

m = tk.Menu(win)
win.config(m=m)

dok = tk.Menu(m)
m.add_cascade(label='Fail', m=dok)
dok.add_command(label='Open', command=of)

text = tk.Text(tb3, wrap="word")
text.pack(fill="both", expand=True)

win.mainloop()
