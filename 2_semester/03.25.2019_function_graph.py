# Уточнение корней.

# Построение графика функции, нахождение и уточнение корней функции упрощённым
# методом Ньютона.

''' ............................ Переменные ............................... '''
# root --------- Основное окно;
# f_input ------ Фрейм с полями ввода;
# f_tabl ------- Фрейм с таблицей;
# arr_lbl_name - Массив, содержит названия полей ввода;
# number_lbl --- Кол-во полей подписи полей ввода;
# number_ent --- Кол-во полей ввода;
# abc1 --------- Массив, содержит запрещённые символы ввода;
# butt_result -- Кнопка запуска программы;
# lbl_enter ---- Пустое поле для отступа;
''' ....................................................................... '''

from tkinter import *
from math import cos, pi, sin
from tkinter import messagebox as mb

import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import numpy as np
import pylab

root = Tk(className = 'Уточнение корней')

f_input = LabelFrame(root, text='Введите данные:')
f_tabl = Frame(root)

# .........................Таблица.......................... #
def append_tabl(rows, lenght):
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            lenght[i][j] = Label(f_tabl, text=rows[i][j],
                                 relief=SUNKEN)
            lenght[i][j].grid(row=i, column=j,
                              sticky=S+N+W+E)
            
# ......................Вывод__ошибки....................... #
def show_error():
    t1 = number_ent[0].get()
    t2 = number_ent[1].get()
    t3 = number_ent[2].get()
    t4 = number_ent[3].get()
    t5 = number_ent[4].get()

    if ((t1 == '') or (t2 == '') or (t3 == '')
        or (t4 == '') or (t5 == '')):
        mb.showerror("Ошибка", 'Заполните все поля')
        return 0
    if float(t1) > float(t2):
        mb.showerror("Ошибка", 'Левая граница больше чем правая')
        return 0
    
    return 1

# .........................Функция.......................... #
def F(x): 
    func = cos(x)
    return func

def f(x):
    func = -sin(x)
    return func

# ....................Рисование__графика.................... #
def draw_graph(matrix, xmin, xmax, dx):
    mat_step = 10000;
    shag = (xmax - xmin) / (mat_step - 1)
    extremums_x = list()
    extremums_y = list()
    roots_x = list()
    roots_y = list()
    x = list()
    y = list()
    
    for i in range(1, len(matrix)):
        if matrix[i][5] == 0:
            roots_x.append(float(matrix[i][2]))
            roots_y.append(F(float(matrix[i][2])))

    while xmin <= xmax:
        x.append(xmin)
        xmin += shag
        
    for i in range(len(x)):
        y.append(F(x[i]))

    for i in range(1, len(x) - 1):
        if ((y[i - 1] <  y[i] > y[i + 1]) or
            (y[i - 1] >  y[i] < y[i + 1])):
            extremums_x.append(x[i])
            extremums_y.append(F(x[i]))

    plt.title('Упрощённый метод Ньютона')
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.grid()

    root_patch = ptch.Patch(color = 'green', label = 'Roots')
    exs_patch =ptch.Patch(color = 'red', label = 'Extremums')
    patch_list = []
    if len(roots_x):
        patch_list.append(root_patch)
    if len(extremums_x):
        patch_list.append(exs_patch)

    plt.legend(handles = patch_list)
    plt.plot(x, y)
    plt.plot(extremums_x, extremums_y, 'ro')
    plt.plot(roots_x, roots_y, 'go')
    plt.show()
    
# .................Упрощённый_метод_Ньютона................. #
def just_nuton(border1, border2, epsilon, m_iter, derivative):
    k = 1
    xi = border1
    xi_1 = xi - F(xi) / derivative
    while abs(xi - xi_1) > epsilon:
        if k > m_iter:
            return xi_1, 2, k
        if not(border1 <= xi_1 <= border2):
            return xi_1, 1, k
        xi = xi_1
        xi_1 = xi - F(xi) / derivative
        k += 1
        
    if not(border1 <= xi_1 <= border2):
            return xi_1, 1, k
        
    return xi_1, 0, k

def check(x, x0 , eps):
    if x != 'X':
        return False
    if abs(x0 - float(x)) > 2*eps:
        return True
    else:
        return False

# ........................Вычисления........................ #
def prog_start():
    ch = show_error()
    if ch:
        a      = float(number_ent[0].get())
        b      = float(number_ent[1].get())
        eps    = float(number_ent[2].get())
        h      = float(number_ent[3].get())
        max_it = int(number_ent[4].get())

        head_tabl = [['#',
                      '[x(i); x(i+1)]',
                      'X',
                      'f(x)',
                      'кол-во\nитераций',
                      'code']]

        number_tabl_lbl = []
        number_tabl_lbl.append([0]*len(head_tabl[0]))

        n = 1
        der = f(b)
        st = a
        i = 1

        while a <= b:
            border = a + h
            if border >= b:
                border = b
                
            x, code, k = just_nuton(a, border, eps, max_it, der)
            
            if code == 2:
                x, code, k = just_nuton(border, a, eps, max_it, der)

            if code != 2 and code != 1:
                p = check(x, head_tabl[i - 1][2], eps)
                if p:
                    section = ('[ ' + '{:.4f}'.format(a) + '; ' +
                               '{:.4f}'.format(border) + ' ]')
                
                    number_tabl_lbl.append([0]*len(head_tabl[0]))
                    head_tabl.append([n, section, '{:.4f}'.format(x),
                                      '{:.0e}'.format(F(x)), k, code])
                    n += 1
                    i += 1
                
            a += h
            
        append_tabl(head_tabl, number_tabl_lbl)
        draw_graph(head_tabl, st, b, h)

# .................Проверка__входных_данных................. #
def check_entry_1(count1, count2):
    for i in abc1:
        if count2.count(i):
            return False
    if count2.count(','):
        return False
    
    return True

def check_entry_2(count1, count2):
    for i in abc1:
        if count2.count(i):
            return False
        
    if count2.count('.'):
        if count2.count('.') > 1:
            return False
        
    return True

# ::::::::::::::::::::::::Константы::::::::::::::::::::::::: #
arr_lbl_name = ['Начало интервала:',
                'Конец интервала:',
                'Погрешность eps:',
                'Шаг:',
                'Max число итераций:']

number_lbl = [0] * len(arr_lbl_name)
number_ent = number_lbl

abc1 = ['a','b','c','d','f','g','h','i','j','k',
        'l','m','n','o','p','q','r','s','t','u',
        'v','w','x','y','z','а','б','в','г','д',
        'е','ё','ж','з','и','й','к','л','м','н',
        'о','п','р','с','т','у','Ф','х','ц','ч',
        'ш','щ','ъ','ы','ь','э','ю','я','+','=',
        ';',':',"'",'/','|','`','_']

# ::::::::::::::::::::Неизменяемый_текст:::::::::::::::::::: #
lbl_enter = Label(root, text=
                  '''code = 0 - корень успешно найден;''')

for i in range(len(arr_lbl_name)):
    number_lbl[i] = Label(f_input, text=arr_lbl_name[i])
    number_lbl[i].grid(row=i, column=0, sticky=E)

# ::::::::::::::::::::::::Поля_ввода:::::::::::::::::::::::: #
for i in range(len(arr_lbl_name)):
    number_ent[i] = Entry(f_input, width=40, validate='key')
    number_ent[i].grid(row=i, column=1)
    if i == len(arr_lbl_name) - 1:
        number_ent[i]['validatecommand'] = (number_ent[i]
                                        .register(check_entry_1),
                                        '%S', '%P')
    else:
        number_ent[i]['validatecommand'] = (number_ent[i]
                                        .register(check_entry_2),
                                        '%S', '%P')

# ::::::::::::::::::::Отрисовка__фреймов:::::::::::::::::::: #
butt_result = Button(root, width=59, height=2,
                     command=prog_start, text='Начать уточнение')

f_input.pack()
butt_result.pack()

lbl_enter.pack()
f_tabl.pack()

root.mainloop()
