# Метод Ньютона (секущих)

# Программа уточняет для заданной функции корни, выводит их на экран
# (при их успешном уточнении), а также рисует график функции с отмеченными
# корнями и экстремумами.

from math import*
from tkinter import*

import numpy as np
import matplotlib.pyplot as plt
import tkinter.messagebox as box

# ===============================Функция================================ #
# Сама функция
def func(x):
    return sin(x)

# Производная от функции
def dif_func(x):
    return cos(x)
    
# ==========================Меню__кодов_ошибки========================== #
def code_information():
    box.showinfo('Информация об ошибках при поиске корней',
                 '0 - Корень найден\n1 - Количество '
                 'произведенных итераций больше введенного значения\n'
                 '2 - Касательные выходят за границы отрезка\n3 - Выход '
                 'за правую границу отрезка\n4 - Корней нет')

# ==========================Заголовок__таблицы========================== #
def title(event = 0):
    entry = Entry(frame_1, justify = CENTER, width = 69,
              disabledbackground = "white", disabledforeground = "black")
    entry.insert(0, 'Метод Ньютона (метод касательных)')
    entry.configure(state = DISABLED)
    entry.grid(row = 0, column = 0, columnspan = 6)

    entry = Entry(frame_1, width=4, justify=CENTER,
              disabledbackground="white", disabledforeground="black")
    entry.insert(0, '№')
    entry.configure(state = DISABLED)
    entry.grid(row=1, column=0)

    entry = Entry(frame_1, width=17, justify=CENTER,
              disabledbackground="white", disabledforeground="black")
    entry.insert(0, '[x(i); x(i+1)]')
    entry.configure(state=DISABLED)
    entry.grid(row=1, column=1)

    entry = Entry(frame_1, width=9, justify=CENTER,
              disabledbackground="white", disabledforeground="black")
    entry.insert(0, 'x')
    entry.configure(state=DISABLED)
    entry.grid(row=1, column=2)

    entry = Entry(frame_1, width=12, justify=CENTER,
              disabledbackground="white", disabledforeground="black")
    entry.insert(0, 'f(x)')
    entry.configure(state=DISABLED)
    entry.grid(row=1, column=3)

    entry = Entry(frame_1, width=15, justify=CENTER,
              disabledbackground="white", disabledforeground="black")
    entry.insert(0, 'Число итераций')
    entry.configure(state=DISABLED)
    entry.grid(row=1, column=4)

    entry = Entry(frame_1, width=9, justify=CENTER,
              disabledbackground="white", disabledforeground="black")
    entry.insert(0, 'Code')
    entry.configure(state=DISABLED)
    entry.grid(row=1, column=5)

#
def add_string(count, x0, x1, x, it, code, flag):
    if flag:
        f = round(func(x), 20)
        x0 = '{:.4f}'.format(x0)
        x1 = '{:.4f}'.format(x1)
        x = '{:.4f}'.format(x)
        f = '{:1.0e}'.format(f)
        
    entry = Entry(frame_1, width=4, justify=CENTER,
                  disabledbackground="white", disabledforeground="black")
    
    if count == '-':
        entry.insert(0, '-')   
    else:
        entry.insert(0, count)
        
    entry.configure(state=DISABLED)
    entry.grid(row = count + 1, column = 0)

    entry = Entry(frame_1, width=17, justify=CENTER,
              disabledbackground="white", disabledforeground="black")

    xi = float(x0)
    xi_1 = float(x1)
    entry.insert(0, '[' + '{:.4f}'.format(xi) + ' ; ' + '{:.4f}'.format(xi_1) + ']')
        
    entry.configure(state = DISABLED)
    entry.grid(row = count + 1, column = 1)

    entry = Entry(frame_1, width=9, justify=CENTER,
              disabledbackground="white", disabledforeground="black")
    
    if flag and code != 2 and code != 3 and code != 4:
        entry.insert(0, x)
    else:
        entry.insert(0, '-')
        
    entry.configure(state = DISABLED)
    entry.grid(row=count + 1, column=2)

    entry = Entry(frame_1, width=12, justify=CENTER,
              disabledbackground="white", disabledforeground="black")
    
    if flag and code != 2 and code != 3 and code != 4:
        entry.insert(0, f)
    else:
        entry.insert(0, '-')
        
    entry.configure(state=DISABLED)
    entry.grid(row=count + 1, column=3)

    entry = Entry(frame_1, width=15, justify=CENTER,
              disabledbackground="white", disabledforeground="black")
    
    if flag and code != 2 and code != 3 and code != 4:
        entry.insert(0, it)
    else:
        entry.insert(0, '-')
        
    entry.configure(state=DISABLED)
    entry.grid(row=count + 1, column=4)

    entry = Entry(frame_1, width=9, justify = CENTER,
              disabledbackground="white", disabledforeground="black")
    
    entry.insert(0, code)
    entry.configure(state=DISABLED)
    entry.grid(row=count + 1, column=5)
        
# ============================Метод__Ньютона============================ #
def newton_kas(x0, x_k, eps, max_it, n, N):
    if func(x_k) == 0:
        return x_k, 0, 0
    if func(x0) == 0:
        return x0, 0, 0
    it = 1
    if abs(dif_func(x0)) < 1e-4:
        return None, it, 5
    x1 = x0 - func(x0) / dif_func(x0)
    a = x0
    while abs(x1 - x0) > eps:
        if abs(dif_func(x0)) < 1e-4:
            return None, it, 5
        it += 1
        x0 = x1
        x1 = x0 - func(x0) / dif_func(x0)
    if ((a <= round(x1, 4) < x_k) or (x_k <= round(x1, 4) < a)):
        if it < max_it:
            return x1, it, 0
        else:
            return x1, it, 1
        
    elif a < x_k and n == N - 1 and abs(x1 - x_k) <= 1e-5:
        if it < max_it:
            return x1, it, 0
        else:
            return x1, it, 1
        
    elif a > x_k and n == N - 1 and abs(x1 - a) <= 1e-5:
        if it < max_it:
            return x1, it, 0
        else:
            return x1, it, 1
        
    else:
        return None, it, 3

# ==========================Построение_графика========================== #
def draw(a, b):
    plt.clf()
    array_min = list()
    array_max = list()
    array_fmin = list()
    array_fmax = list()
    array_func = list()
    
    x = np.linspace(a, b, 1000)
    plt.plot(x, np.sin(x))
    
    for i in np.arange(a, b, 1e-5):
        if abs(dif_func(i)) < 1e-4:
            if (func(i) - func(i - 0.001)) > 0 and \
               (func(i) - func(i + 0.001)) > 0:
                array_max.append(i)
                array_fmax.append(func(i))
            elif (func(i) - func(i - 0.001)) < 0 and \
                 (func(i) - func(i + 0.001)) < 0:
                array_min.append(i)
                array_fmin.append(func(i))
    if array_max != []:
        plt.plot(array_max, array_fmax, 'o', color='red',
                 label='Maximum')
    if array_min != []:
        plt.plot(array_min, array_fmin, 'o', color='blue',
                 label='Minimum')
    if found_for_print != []:
        for i in found_for_print:
            array_func.append(func(i))
        plt.plot(found_for_print, array_func, 'o', color='green',
                 label='Root')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

# =====================Запуск_уточнения_и_отрисовки===================== #
def work(event = 0):
    global frame_1
    global found_for_print    # Все корни
    
    found_for_print = []
    
    frame_1.place_forget()
    frame_1 = Frame(window)
    
    title()
    
    frame_1.place(x = 10, y = 260)
    
    a = entry_left.get()
    b = entry_right.get()
    step = entry_step.get()
    eps = entry_eps.get()
    max_it = entry_it.get()

    if a == '' or b == '' or step == '' or eps == '' or max_it == '':
        box.showwarning('Ошибка',
                        'Некоторые поля не заполнены')
        return 1
    
    if float(a) == float(b):
        box.showwarning('Ошибка',
                        'Границы совпадают')
        return 1
    if float(a) > float(b):
        box.showinfo('Ошибка',
                     'Левая граница отрезка больше правой. ')
        return 1
        
    a = float(a)
    b = float(b)
    step = float(step)
    eps = float(eps)
    max_it = float(max_it)
    
    if eps <= 0 or eps >= 1:
        box.showwarning('Ошибка',
                        'Неправильная точность eps')
        return 1
    
    N = abs((a - b)/step)
    n = 0
    x0 = a
    x1 = x0 + step
    count = 0
    ff = 0
    
    while n < N:
        if x1 >= b:
            x1 = b
        x, it, code = newton_kas(x0, x1, eps, max_it, n, N)
        
        if code == 1:
            count += 1
            found_for_print.append(x)
            add_string(count, x0, x1, '-', '-', code, 0)
            
        elif x != None and round(x, 10) <= b:
            count += 1
            
            if b < x1:
                x1 = b
                code = 3
            found_for_print.append(x)
            add_string(count, x0, x1, x, it, code, 1)
            
        elif code == 5 or code == 3:
            x, it, code = newton_kas(x1, x0, eps, max_it, n, N)
            
            if code == 1:
                count += 1
                found_for_print.append(x)
                add_string(count, x0, x1, '-', '-', code, 0)
                
            elif x != None and x <= b:
                count += 1
                if b < x1:
                    x1 = b
                    code = 3
                found_for_print.append(x)
                add_string(count, x0, x1, x, it, code, 1)
                
            else:
                if x1 > b:
                    x1 = b
                    
                for i in np.arange(x0, x1, 0.01):
                    if round(abs(func(i)), 2) == 0:
                        ff = 1
                        count += 1
                        add_string(count, x0, x1, '-', '-', 2, 0)
                        found_for_print.append(i)
                        
        x0 = x1
        x1 += step
        n += 1
        
    if count == 0 and ff == 0:
        add_string(1, x0, x1, '-', '-', 4, 0)
    draw(a, b)
    
# =======================Основная__функция_(main)======================= #
found = []
window = Tk()
frame_1 = Frame(window)

# >>Имена полей ввода
name_lbl = ['Левая граница: ',
            'Правая граница: ',
            'Шаг: ',
            'Точность (eps): ',
            'Макс. кол-во итераций: ']

title_entry = [0] * len(name_lbl)

for i in range(len(title_entry)):
    title_entry[i] = Label(window, text=name_lbl[i])
    title_entry[i].grid(row=i, column=0, sticky='W')
# <<

# >>Левая_раница
entry_left = Entry(window, width=50)
entry_left.grid(row=0, column=1)
# <<

# >>Правая_граница
entry_right = Entry(window, width=50)
entry_right.grid(row=1, column=1)
# <<

# >>Шаг
entry_step = Entry(window, width=50)
entry_step.grid(row=2, column=1)
# <<

# >>Точность_eps
entry_eps = Entry(window, width=50)
entry_eps.grid(row=3, column=1)
# <<

# >>Максимальное_число_итераций
entry_it = Entry(window, width=50)
entry_it.grid(row=4, column=1)
# <<

# >>Кнопка_старта_уточнения
btn = Button(window, text='Начать уточнение корней', bg = 'lightgray')

btn.bind('<Button-1>', work)
btn.bind('<Return>', work)
btn.grid(row=5, column=0, columnspan=2, sticky='SNWE')
# <<

window.title('Уточнение корней')
window.geometry('575x630')

title()

main_menu = Menu(window)

main_menu.add_cascade(label = 'Коды ошибок',command = code_information)
window.config(menu = main_menu)

frame_1.place(x = 10, y = 260)

window.mainloop()
