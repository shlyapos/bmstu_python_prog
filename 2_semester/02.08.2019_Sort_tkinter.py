# Тест сортировки.

# Программа может отсортировать входной массив, а также подсчитывает время
# сортировки массивов разных вводимых размерностей.

''' ............................ Переменные ............................... '''
# f_massiv1 - Фрейм для расположения двух полей ввода/вывода и кнопки
# f_tabl - Фрейм для расположения таблицы результатов
# massiv_active
# method_name - Массив, который содержит названия видов сортируемых массивов
# number_label - Массив для строк таблицы с названиями методов
# number_label_time - Матрица результатов для каждого метода
# number_entry - Поля ввода размерностей случайных массивов
# abc1 ─┐
# abc2  ├─ Массивы запрещённых для ввода символов
# abc3 ─┘
''' ....................................................................... '''

from tkinter import messagebox as mb
from random  import uniform
from tkinter import *

import numpy as np
import timeit

root = Tk(className = 'Тест сортировки')

f_massiv1 = Frame(root)
f_tabl = LabelFrame(root, text='[Обработка случайных массивов]')

# ...............Вывод__сообщения_со_справкой............... #
def info():
    messagebox.showinfo('О программе',
                        ''' Программа подсчитывает время
 выполнения сортировки вставками

 Автор: Сучков А.Д.
 Группа: ИУ7-22Б''')
# .......................................................... #
'''////////////////////////////////////////////////////////'''
# ...................Сортировка_вставками................... #
def sortirovka(massiv):
    for i in range(1,len(massiv)):
        count = massiv[i]
        j = i - 1
        while (j >= 0) and (massiv[j] > count):
            massiv[j+1] = massiv[j]
            j -= 1
        massiv[j+1] = count
        
    return massiv
# .......................................................... #
'''////////////////////////////////////////////////////////'''
# .......Выполнение__сортировки_для заданного_массива....... #
def do_sort():
    global f
    f = True
    s = entry_massiv1.get()
    if '.' in s:
        a = list(s.split())
        s = ''
        a = list(map(float, a))
    else:
        a = list(s.split())
        s = ''
        a = list(map(int, a))
    sortirovka(a)
    for i in range(len(a)):
        s += str(a[i])
        if i != len(a) - 1:
            s += ' '
    entry_massiv2.delete(0, END)
    entry_massiv2.insert(0, s)
    f = False
# .......................................................... #
'''////////////////////////////////////////////////////////'''
# ................Подсчёт_времени_сортировки................ #
def time_inf(massiv, flag):
    if flag:
        time_start = timeit.default_timer()
        sortirovka(massiv)
        time_end = timeit.default_timer() - time_start
    else:
        time_start = timeit.default_timer()
        massiv.sort()
        time_end = timeit.default_timer() - time_start
        
    return time_end
# .......................................................... #
'''////////////////////////////////////////////////////////'''
# ...............Создание__случайных_массивов............... #
def create_massiv(size):
    massiv = list()
    for i in range(0, size):
        massiv.append(uniform(-10, 10))
        
    return massiv
# .......................................................... #
'''////////////////////////////////////////////////////////'''
# ..............Сортировка__случайных_массивов.............. #
def sort_random_massiv():
    flag, number = check_size()    # Проверка пустых полей
    if not(flag):
        mb.showerror("Ошибка", 'Введите размер массива в поле № {}'
                     .format(number))
    else:
        massiv1 = create_massiv(int(number_entry[0].get()))
        massiv2 = create_massiv(int(number_entry[1].get()))
        massiv3 = create_massiv(int(number_entry[2].get()))

        copy_massiv1 = massiv1[:]
        copy_massiv2 = massiv2[:]
        copy_massiv3 = massiv3[:]

        matrix_inf = [[0] * 3 for i in range(4)]

        matrix_inf[0][0] = time_inf(copy_massiv1, True)
        matrix_inf[0][1] = time_inf(copy_massiv2, True)
        matrix_inf[0][2] = time_inf(copy_massiv3, True)

        matrix_inf[1][0] = time_inf(copy_massiv1, True)
        matrix_inf[1][1] = time_inf(copy_massiv2, True)
        matrix_inf[1][2] = time_inf(copy_massiv3, True)

        copy_massiv1 = copy_massiv1[::-1]
        copy_massiv2 = copy_massiv2[::-1]
        copy_massiv3 = copy_massiv3[::-1]

        matrix_inf[2][0] = time_inf(copy_massiv1, True)
        matrix_inf[2][1] = time_inf(copy_massiv2, True)
        matrix_inf[2][2] = time_inf(copy_massiv3, True)
        
        matrix_inf[3][0] = time_inf(massiv1, False)
        matrix_inf[3][1] = time_inf(massiv2, False)
        matrix_inf[3][2] = time_inf(massiv3, False)

        go_to_tabl(matrix_inf)
# .......................................................... #
'''////////////////////////////////////////////////////////'''
# .................Перенос_данных_в_таблицу................. #
def go_to_tabl(matrix):
    global number_label_time
    global count_operations
    for i in range(0, len(number_label_time)):
        for j in range(0, len(number_label_time[i])):
            if count_operations:
                number_label_time[i][j].grid_remove()
                count_operations = 1
            number_label_time[i][j] = Label(f_tabl,
                                            text='{:6.5e}'
                                            .format(matrix[i][j]),
                                            relief=SUNKEN)
            number_label_time[i][j].grid(row=i+2,
                                         column=j+1,
                                         sticky=S+N+W+E)
# .......................................................... #
'''////////////////////////////////////////////////////////'''
# ............Проверка_ввода_правильных_символов............ #
def check_entry(count1, count2):        # Проверка для ввода 
    for i in abc1:                      # заданного массива
        if count2.count(i):
            return False
    for i in abc2:
        if count2.count(i):
            return False
    entry_massiv2.delete(0, END)    
    return True

def check_entry_2(count1, count2):      # Проверка для ввода 
    for i in abc1:                      # размера случайных 
        if count2.count(i):             # массивов
            return False
    for i in abc2:
        if count2.count(i):
            return False

    if count2.count('.'):
        return False
    
    entry_massiv2.delete(0, END)    
    return True

def check_massiv2(count1, count2):      # Для проверки поля 
    if not(f):                          # вывода отсортированного
        for i in abc1:                  # массива 
            if count2.count(i):
                return False
        for i in abc2:
            if count2.count(i):
                return False
        for i in abc3:
            if count2.count(i):
                return False

    return True

def check_size():
    if number_entry[0].get() == '':
        return False, 1
    
    if number_entry[1].get() == '':
        return False, 2
    
    if number_entry[2].get() == '':
        return False, 3

    return True, 0
# .......................................................... #
'''////////////////////////////////////////////////////////'''
# ==================Объявление__переменных================== #
massiv_active = 1
method_name = ['Случайный',
               'Упорядоченный',
               'В обратном порядке',
               'Функция .sort()']
number_label = [0] * len(method_name)
number_label_time = [[0] * 3] * 4
number_entry = [0] * 3

abc1 = ['a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z','+','=',';', ':',
        ',', "'", '/', '|', '`']

abc2 = ['а','б','в','г','д','е','ё','ж','з','и',
        'й','к','л','м','н','о','п','р','с','т',
        'у','Ф','х','ц','ч','ш','щ','ъ','ы','ь',
        'э','ю','я']

abc3 = ['1','2','3','4','5','6','7','8','9','0','.']

f = False            # Флаг для ограничения изменений
                     # пользователем в поле
                     # отсортированного массива
                     # ------------------------- #
count_operations = 0 # отвечает за удаление 
# ========================================================== #
'''////////////////////////////////////////////////////////'''
# ========================Поля_ввода======================== #
entry_massiv1 = Entry(f_massiv1, validate='key', width=40)
entry_massiv1.grid(row=0, column=1, columnspan=2)

entry_massiv2 = Entry(f_massiv1, validate='key', width=40)
entry_massiv2.grid(row=1, column=1, columnspan=2)

entry_massiv1['validatecommand'] = (entry_massiv1.register(check_entry),
                                   '%S', '%P')
entry_massiv2['validatecommand'] = (entry_massiv2.register(check_massiv2),
                                   '%S', '%P')

for i in range(3):
    number_entry[i] = Entry(f_tabl, validate='key', relief=SUNKEN)
    number_entry[i].grid(row=1, column=i+1, sticky=S+N+W+E)
    number_entry[i]['validatecommand'] = (number_entry[i]
                                          .register(check_entry_2),'%S', '%P')
# ========================================================== #
'''////////////////////////////////////////////////////////'''
# ==========================Кнопки========================== #
button_result1 = Button(f_massiv1,
                        text='Отсортировать',
                        command=do_sort)
button_result1.grid(row=0, rowspan=2, column=4,
                    columnspan=2, sticky=S+N+W+E)

button_result2 = Button(f_tabl,
                        text='О\nт\nс\nо\nр\nт\nи\nр\nо\nв\nа\nт\nь',
                        command=sort_random_massiv, width=6)
button_result2.grid(row=0, rowspan=6, column=4, 
                    columnspan=2, sticky=W+E+S+N)
# ========================================================== #
'''////////////////////////////////////////////////////////'''
# ====================Неизменяемый_текст==================== #
label_massiv1 = Label(f_massiv1, text='Введите массив: ')
label_massiv1.grid(row=0, column=0, sticky=E)

label_massiv2 = Label(f_massiv1, text='Отсортированный массив: ')
label_massiv2.grid(row=1, column=0, sticky=E)

label_1 = Label(f_tabl, text='Виды массивов', relief=SUNKEN)
label_1.grid(row=0, rowspan=2, column=0, sticky=S+N+W+E)

label_2 = Label(f_tabl, text='Количество элементов массива', relief=SUNKEN)
label_2.grid(row=0, column=1, columnspan=3, sticky=S+N+W+E)

for i in range(0, len(number_label)):
    number_label[i] = Label(f_tabl, text=method_name[i], relief=SUNKEN)
    number_label[i].grid(row=i+2, column=0, sticky=S+N+W+E)

enter_root = Label(root, text=' ')

enter_f_massiv1 = Label(f_massiv1, text='     ')
enter_f_massiv1.grid(row=0, rowspan=2, column=3)
# ========================================================== #
'''////////////////////////////////////////////////////////'''
# ===================Отрисовка__элементов=================== #
''' ----------------Отрисовка__меню---------------- '''
mainmenu = Menu(root)

root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
mainmenu.add_command(label='Справка', command=info)
''' ----------------------------------------------- '''
f_massiv1.grid(row=0, column=1)
enter_root.grid(row=1, column=0)
f_tabl.grid(row=2, column=1)
''' ----------------------------------------------- '''
# ========================================================== #
'''////////////////////////////////////////////////////////'''

root.mainloop()
