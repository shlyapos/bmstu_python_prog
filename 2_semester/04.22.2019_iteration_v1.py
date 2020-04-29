# Уточнение корней
# упрощённый метод ньютона

from tkinter import *
from tkinter import messagebox
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import numpy as np

def F(x):
    return cos(x)
def f(x):
    return sin(x)

def set_table_row(text0, text1, text2, text3, text4, text5, n):
    Label(table_frame, text=text0, bg=bg_color_main, relief=GROOVE). \
        grid(row=n, column=0, sticky="NSWE")
    Label(table_frame, text=text1, bg=bg_color_main, relief=GROOVE).\
        grid(row=n, column=1, sticky="NSWE")
    Label(table_frame, text=text2, bg=bg_color_main, relief=GROOVE). \
        grid(row=n, column=2, sticky="NSWE")
    Label(table_frame, text=text3, bg=bg_color_main, relief=GROOVE). \
        grid(row=n, column=3, sticky="NSWE")
    Label(table_frame, text=text4, bg=bg_color_main,
          relief=GROOVE). \
        grid(row=n, column=4, sticky="NSWE")
    Label(table_frame, text=text5, bg=bg_color_main, relief=GROOVE). \
        grid(row=n, column=5, sticky="NSWE")

def newton_easy(l, r, eps, max_iter, x0):
    
    if f(x0) == 0:
        return x0, 0, 0
    
    pro = F(x0)
    if pro == 0:
        return x0, 0, 2
    x = x0 - f(x0) / pro
    i = 1
    while abs(x - x0) > eps:
        if not (l <= x <= r):
            return None, i, 2
        
        if i >= max_iter:
            return x, i, 1
        x0 = x
        pro = F(x0)
        if pro == 0:
            return x0, i, 2
        x = x0 - f(x0) / pro
        i += 1
    if not (l <= x <= r):
            return x0, i, 2
    return x, i, 0


def calc_def():
    global table_frame

    try:
        a, b = map(float, (a_var.get(), b_var.get()))
        h = float(h_var.get())
        eps = float(eps_var.get())
        max_iter = int(max_iter_var.get())
    except:
        messagebox.showerror(error_title, error_text1)
        return False

    if a >= b:
        messagebox.showerror(error_title, error_text2)
        return False

    if not(0 < eps < h/2):
        messagebox.showerror(error_title, error_text4)
        return False
    if max_iter < 1:
        messagebox.showerror(error_title, error_text5)
        return False


    table_frame.grid_forget()
    table_frame = Frame(main, bg=bg_color_main)
    table_frame.grid(row=1, column=0, padx=15, pady=2, sticky="NSW")
    

    n = 1
    #
    x_root = []
    y_root = []
    while a + h*(n-1) < b:

        l = a + h*(n-1)
        r = (a + h*n) if a + h*n < b else b

        x, iter_n, err = newton_easy(l, r, eps, max_iter, x0=l)
        if err == 2:
            x, iter_n, err = newton_easy(l, r, eps, max_iter, x0=r)                
        
        if ((err == 0 or err == 1) and (len(x_root) == 0 or
                                        abs(x - x_root[-1])) > 2*eps):
            x_root.append(x)
            y_root.append(f(x))
            frm = "{:.4f}"
            set_table_row(str(len(x_root)), "[{:.4f}; {:.4f}]".format(l, r),
                          frm.format(x), "{:.0e}".format(y_root[-1]),
                          str(iter_n), str(err), n)
            
        
        n += 1

    if len(x_root) == 0:
        Label(table_frame, text="Корни не найдены",
              bg=bg_color_main, relief=GROOVE). \
        grid(row=n, column=0, sticky="NSWE")
    else:
        set_table_row(" # ", "[x(i); x(i+1)]", "корень X", "f(X)",
                      "Количество\n итераций", "Код ошибки", 0)
    
    x = [0] * mat_steps
    y = [0] * mat_steps
    h_mat = (b-a) / (mat_steps - 1)
    for i in range(mat_steps):
        x[i] = a + h_mat*i
        y[i] = f(x[i])
    x_max = []
    y_max = []
    for i in range(1, mat_steps - 1):
        if y[i-1] <= y[i] >= y[i+1] or y[i-1] >= y[i] <= y[i+1]:
            x_max.append(x[i])
            y_max.append(y[i])
    plt.clf()
    plt.grid(True)
    plt.plot(x, y, color = 'black', linewidth = 1)
    plt.scatter(x_max, y_max, color = 'red', linewidth = 0.5)
    plt.scatter(x_root, y_root, color = 'green', linewidth = 0.5)
    
    plt.title(f_name)
    plt.xlabel('x')
    plt.ylabel('y')


    root_patch = ptch.Patch(color = 'green', label = 'Roots')
    exs_patch = ptch.Patch(color = 'red', label = 'Extremums')
    pathc_list = []
    if len(x_root):
        pathc_list.append(root_patch)
    if len(x_max):
        pathc_list.append(exs_patch)
        
    plt.legend(handles = pathc_list)
    plt.show()
                   

def err_info(err):
    if err == 0:
        messagebox.showinfo('Код ошибки 0',
                            'Корень найден')
    if err == 1:
        messagebox.showinfo('Код ошибки 1',
                            'Корень не найден за заданное количество итераций')


"""Виджеты"""

# Основное окно Tkinter
main = Tk()

main_menu = Menu(main)

""" Константы   """
size_x, size_y = 840, 960
mat_steps = 50000
bg_color_main = "grey"
main_font = "Arial 11"
title_font = "Arial 14"
entry_width = 30

a_start = '12'
b_start = ''
h_start = ''
eps_start = ''
max_iter_start = ''

window_title_text = "Уточнение корней упрощённым методом Ньютона"
f_name = 'f(x) = sin(x)'
f_name_text = "Нахождение корней"
title_text = "Введите данные для вычисления корней: "
a_text = "Начало интервала: "
b_text = "Конец интервала: "
h_text = "Шаг: "
eps_text = "Точность eps: "
max_iter_text = "Максимальное количество итераций: "
calc_text = "Начать\nуточнение"

error_title = "Ошибка"
error_text1 = "Некорректный формат ввода данных"
error_text2 = "Некорректный интервал (a => b)"
error_text3 = "Некорректный шаг"
error_text4 = "Некорректная погрешность"
error_text5 = "Некорректное максимальное количество итераций"

# Меню действий
action_menu = Menu(main_menu, tearoff = False)
main_menu.add_cascade(  label = "Коды ошибок", menu = action_menu)

action_menu.add_command(label = "0", command = lambda obj = 0: err_info(obj))
action_menu.add_command(label = "1", command = lambda obj = 1: err_info(obj))
                                                                                                         
main_frame = Frame(main, bg=bg_color_main)
main_frame.grid(row=0, column=0, padx=15, pady=15)

# Переменные ввода
a_var = StringVar(main_frame)
b_var = StringVar(main_frame)
h_var = StringVar(main_frame)
eps_var = StringVar(main_frame)
max_iter_var = StringVar(main_frame)

a_var.set(a_start)
b_var.set(b_start)
h_var.set(h_start)
eps_var.set(eps_start)
max_iter_var.set(max_iter_start)

# Надписи ввода
f_name_label = Label(main_frame, text=f_name_text, bg=bg_color_main,
                     font=title_font)
title_label = Label(main_frame, text=title_text, bg=bg_color_main,
                    font=main_font)
a_label = Label(main_frame, text=a_text, bg=bg_color_main, font=main_font)
b_label = Label(main_frame, text=b_text, bg=bg_color_main, font=main_font)
h_label = Label(main_frame, text=h_text, bg=bg_color_main, font=main_font)
eps_label = Label(main_frame, text=eps_text, bg=bg_color_main, font=main_font)
max_iter_label = Label(main_frame, text=max_iter_text,
                       bg=bg_color_main, font=main_font)

# Поля ввода
a_entry = Entry(main_frame, textvariable=a_var, font=main_font,
                width=entry_width)
b_entry = Entry(main_frame, textvariable=b_var, font=main_font)
h_entry = Entry(main_frame, textvariable=h_var, font=main_font)
eps_entry = Entry(main_frame, textvariable=eps_var, font=main_font)
max_iter_entry = Entry(main_frame, textvariable=max_iter_var, font=main_font)


calc_button = Button(main_frame, text=calc_text, command=calc_def)

f_name_label.grid(row=0, column=0, columnspan=3, pady = 10)
title_label.grid(row=1, column=0, columnspan=2, pady = 7, sticky="W")

a_label.grid(row=2, column=0, sticky="W")
a_entry.grid(row=2, column=1, sticky="WE")
b_label.grid(row=3, column=0, sticky="W")
b_entry.grid(row=3, column=1, sticky="WE")
h_label.grid(row=4, column=0, sticky="W")
h_entry.grid(row=4, column=1, sticky="WE")
eps_label.grid(row=5, column=0, sticky="W")
eps_entry.grid(row=5, column=1, sticky="WE")
max_iter_label.grid(row=6, column=0, sticky="W")
max_iter_entry.grid(row=6, column=1, sticky="WE")

calc_button.grid(row=2, column=2, rowspan=5, sticky="NSWE", padx = 5)


# Таблица
table_frame = Frame(main, bg=bg_color_main)
table_frame.grid(row=1, column=0, padx=15, pady=2, sticky="NSW")

main.config(menu = main_menu)
main.title(window_title_text)
main.config(bg=bg_color_main)
main.geometry('{}x{}+5+5'.format(size_x, size_y))
main.resizable(False, False)
main.mainloop()
