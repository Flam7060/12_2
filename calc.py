import tkinter as tk
w = 240
h = 300


def add_digit(digit):
    vaul = calc.get()
    if vaul[0] == '0' and len(vaul) == 1 :
        vaul = vaul[1:]
    calc.delete(0, tk.END)
    calc.insert(0, vaul + digit)


def add_operation(operation):
    vaul = calc.get()
    if vaul[-1] in '-+/*':
        vaul = vaul[:-1]
    elif '+' in vaul or '-' in vaul or '*' in vaul or '/' in vaul:
        calculate()
        vaul = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, vaul+operation)


def calculate():
    vault = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, eval(vault))


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')

def delet():
    vaul = calc.get()
    calc.delete('end')



def pres_key(event):
    #print(event)
    print(repr(event.char))
    if event.char.isdigit() :
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif  event.char == '\r': # Enter 
        print('1')
        add_operation(event.char)
    elif event.char == '\x08': # BackSpace
        delet()


def digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 12), command=lambda: add_digit(digit))


def operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 12), command=lambda: add_operation(operation))


def calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 12), command=calculate)


def clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 12), command=clear)


win = tk.Tk()
win.title('Калькулятор')

# через + мы указываем координаты открытия от левого угла 1 это по горизонт 2 по верт ({h} x {w} это размеры базового окна )
win.geometry(f'{w}x{h}+200+270')

win.minsize(w, h)  # минимальные размеры / win.maxsize() макс размеры

win.bind('<Key>', pres_key)


calc = tk.Entry(win, justify=tk.RIGHT)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, sticky='wens', padx=5)

digit_button('1').grid(row=1, column=0, sticky='wens', padx=5, pady=5)
digit_button('2').grid(row=1, column=1, sticky='wens', padx=5, pady=5)
digit_button('3').grid(row=1, column=2, sticky='wens', padx=5, pady=5)
digit_button('4').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
digit_button('5').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
digit_button('6').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
digit_button('7').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
digit_button('8').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
digit_button('9').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
digit_button('0').grid(row=4, column=0, sticky='wens', padx=5, pady=5)

#lbl = tk.Label(text=' ')
#lbl.grid(row=1, column=0, sticky='wens', padx=5, pady=5)

operation_button('+').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
operation_button('-').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
operation_button('*').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
operation_button('/').grid(row=4, column=3, sticky='wens', padx=5, pady=5)


calc_button('=').grid(row=4, column=2, sticky='wens', padx=5, pady=5)
clear_button('C').grid(row=4, column=1, sticky='wens', padx=5, pady=5)




win.grid_rowconfigure(0, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.mainloop()  