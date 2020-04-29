# Калькулятор.

# Программа получает на вход два числа производит с ними выбранные операции
# сложения или вычитания в восьмиричной системе счисления.

''' ............................ Переменные ............................ '''
# f_button, f_result - Фреймы для кнопок чисел и знака "="
# f_input1, f_input2, f_output - Фреймы для полей ввода и вывода
# mainmenu - Основное меню программы
# /----------------------------------------------\
#   do_menu - Меню выбора оперции +/-
#   clear_menu - Меню очистки полей ввода и вывод
# \----------------------------------------------/
# operation - Выбранная операция (1-Сложение, 2-Вычитание)
# result - Ответ (поле вывода)
# command - Отвечает за распознавание кнопок калькулятора в функциях
# /-----------------------------------------------------------------\
#   1 - Кнопка button_1
#   2 - Кнопка button_2
#   3 - Кнопка button_3
#   и т.д.
# \-----------------------------------------------------------------/
# button_result - Кнопка отвечающая за вывод ответа
# entry_input1 - Поле ввода числа 1
# entry_input2 - Поле ввода числа 2
# label_output - Вывод ответа на экран
# label_plus - Отрисовка + са между числами
# label_minus - Отрисовка - са ммежду числами
''' .................................................................... '''

from tkinter import *
from tkinter import messagebox as mb

abc1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z','8','9','+','=', ';', ':', ',',
        "'", '/', '|', '`']

abc2 = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п',
         'р','с','т','у','Ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

root = Tk(className = 'Калькулятор')

f_button = Frame(root)
f_result = Frame(root)

f_input1 = LabelFrame(root, text = 'Число 1')
f_input2 = LabelFrame(root, text = 'Число 2')
f_output = LabelFrame(root, text = 'Вывод')

mainmenu = Menu(root)
root.config(menu = mainmenu)

command = -1        # Команды кнопок
result = ''         # Результат
operation = 1       # Операции сложения/вычитания
input_active = 1    # Активные поля ввода

# ........... Описание кнопок ........... #
def button0(event):
    global command
    command = 0
    inp(command)
    
def button1(event):
    global command
    command = 1
    inp(command)

def button2(event):
    global command
    command = 2
    inp(command)

def button3(event):
    global command
    command = 3
    inp(command)

def button4(event):
    global command
    command = 4
    inp(command)

def button5(event):
    global command
    command = 5
    inp(command)

def button6(event):
    global command
    command = 6
    inp(command)

def button7(event):
    global command
    command = 7
    inp(command)

def buttontochka(event):
    global command
    command = 8
    inp(command)

def buttoncl(event):
    if input_active == 1:
        entry_input1.delete(len(entry_input1.get())-1,END)
    else:
        entry_input2.delete(len(entry_input2.get())-1,END)

def buttonresult(event):
    global result
    count1 = entry_input1.get()
    count2 = entry_input2.get()
    # ------------ Проверка знака  числа ------------ #
    count1, f1 =  check_sign(count1)# Знак для числа 1
    count2, f2 =  check_sign(count2) # Знак для числа 2
    # ----------------------------------------------- #
    count1 = f8t10(count1)
    count2 = f8t10(count2)
    
    if f1 == 1:
        count1 = -count1
    if f2 == 1:
        count2 = -count2

    if operation == 1:
        result = count1 + count2
    else:
        result = count1 - count2
        
    result, fr = check_sign(str(result))
    result = f10t8(result)
    
    if fr == 1:
        result = '-' + result
    print_result()
# ....................................... #
'''/////////////////////////////////////'''
# ..... Перевод чисел из 8-й в 10-ю ..... #
def f8t10(count):
    s = list(count.split('.'))
    if len(s) == 1:
        count = int(0)
    else:
        count = float(0)
    
    len_str = len(s[0]) - 1
    for i in s[0]:
        count += int(i)*8**len_str
        len_str -= 1

    if len(s) == 2:
        len_str = 1
        for i in s[1]:
            count += float(i)*8**(-len_str)
            len_str += 1
            
    return count
# ....................................... #
'''/////////////////////////////////////'''
# ........ Проверка знака  числа ........ #
def check_sign(count):
    f = 0
    if '-' in count:
        f = 1
        if '.' in count:
            count = str(abs(float(count)))
        else:
            count = str(abs(int(count)))
    return count, f            
# ....................................... #
'''/////////////////////////////////////'''
# ..... Перевод чисел из 10-й в 8-ю ..... #
def f10t8(count):
    count = str(count)
    s = list(count.split('.'))
    count = ''

    s[0] = int(s[0])
    while s[0] >= 8:
        count += str(s[0]%8)
        s[0] = s[0]//8
    count += str(s[0])
    count = count[::-1]

    if len(s) == 2:
        count += '.'
        s[1] = (int(s[1])/10**len(s[1]))*8
        while int(s[1]) == 0:
            count += str(int(s[1]))
            a = list(str(s[1]).split('.'))
            s[1] = (int(a[1])/10**len(a[1]))*8
            
        while int(s[1]) != 0:
            count += str(int(s[1]))
            a = list(str(s[1]).split('.'))
            s[1] = (int(a[1])/10**len(a[1]))*8

    return count   
# ....................................... #
'''/////////////////////////////////////'''
# ......... Активные поля ввода ......... #
def activate_entry1(event):
    global input_active
    input_active = 1

def activate_entry2(event):
    global input_active
    input_active = 2
# ....................................... #
'''/////////////////////////////////////'''
# .......... Проверка на буквы .......... #
def check_abc(count, new_count):
    checklist = 0
    for i in count:
        if i in abc1 or i in abc2:
            checklist = 1
            break

    for i in new_count:
        if i in abc1 or i in abc2:
            checklist = 1
            break

    return checklist
# ....................................... #
'''/////////////////////////////////////'''
# ............. Поля  ввода ............. #
def inp(event):
    if input_active == 1:
        if command == 8:
            s = entry_input1.get()
            
            if not('.' in s):
                entry_input1.insert(END, '.')
        else:
            entry_input1.insert(END, str(command))
    else:
        if command == 8:
            s = entry_input2.get()
            
            if not('.' in s):
                entry_input2.insert(END, '.')
        else:
            entry_input2.insert(END, str(command))
# ....................................... #
'''/////////////////////////////////////'''
# ....... Рисование операции  +/- ....... #
def printpl():
    global operation
    operation = 1
    label_minus.grid_remove()
    label_plus.grid(row=1, column=0, padx=15, pady=1)

def printmin():
    global operation
    operation = 2
    label_plus.grid_remove()
    label_minus.grid(row=1, column=0, padx=15, pady=1)

def print_result():
    global label_output
    label_output.grid_remove()
    label_output = Label(f_output, text=result)
    label_output.grid(row=0, column=0)
# ....................................... #
'''/////////////////////////////////////'''
# ............ Очистка полей ............ #
def clear1():
    entry_input1.delete(0, END)

def clear2():
    entry_input2.delete(0, END)

def clear_output():
    global result
    result = ''
    print_result()

def autoclear(count1, count2):
    if count2.count('.') > 1:
        return False
    for i in abc1:
        if count2.count(i):
            return False
    for i in abc2:
        if count2.count(i):
            return False
    
    if count1 != '':
        clear_output()
        
    return True

def clear_all():
    clear1()
    clear2()
    clear_output()
# ....................................... #
'''/////////////////////////////////////'''
# ............. О программе ............. #
def about():
    about_window = Toplevel()
    about_window.title("О программе")
    author = Label(about_window, text='Автор:      Сучков А.Д.')
    group = Label(about_window, text='Группа:      ИУ7-22Б')
    info1 = Label(about_window, text='Программа калькулятор:')
    info2 = Label(about_window, text='Программа складывает или вычитает')
    info3 = Label(about_window, text='два введёных числа и выводит')
    info4 = Label(about_window, text='ответ на экран.')
    
    author.grid(row=0, column=0, padx=0, pady=0)
    group.grid(row=1, column=0, padx=0, pady=0)
    info1.grid(row=2, column=0, padx=0, pady=0)
    info2.grid(row=3, column=0, padx=0, pady=0)
    info3.grid(row=4 ,column=0, padx=0, pady=0)
    info4.grid(row=5, column=0, padx=0, pady=0)
# ....................................... #
    
# ................. свойства кнопок ................. #
button_0 = Button(f_button, width=3, height=1, text='0')
button_1 = Button(f_button, width=3, height=1, text='1')
button_2 = Button(f_button, width=3, height=1, text='2')
button_3 = Button(f_button, width=3, height=1, text='3')
button_4 = Button(f_button, width=3, height=1, text='4')
button_5 = Button(f_button, width=3, height=1, text='5')
button_6 = Button(f_button, width=3, height=1, text='6')
button_7 = Button(f_button, width=3, height=1, text='7')

button_result = Button(f_result, width=3, height=1, text='=')
button_cl = Button(f_result, width=3, height=1, text='←')
button_tochka = Button(f_button, width=3, height=1, text='.')

''' ................... bind .................... '''
button_0.bind('<Button-1>', button0)
button_1.bind('<Button-1>', button1)
button_2.bind('<Button-1>', button2)
button_3.bind('<Button-1>', button3)
button_4.bind('<Button-1>', button4)
button_5.bind('<Button-1>', button5)
button_6.bind('<Button-1>', button6)
button_7.bind('<Button-1>', button7)

button_result.bind('<Button-1>', buttonresult)
button_cl.bind('<Button-1>', buttoncl)
button_tochka.bind('<Button-1>', buttontochka)
''' ............................................. '''

button_0.grid(row=0, column=0, sticky=W+E)
button_1.grid(row=0, column=1, sticky=W+E)
button_2.grid(row=0, column=2, sticky=W+E)
button_3.grid(row=0, column=3, sticky=W+E)
button_4.grid(row=1, column=0, sticky=W+E)
button_5.grid(row=1, column=1, sticky=W+E)
button_6.grid(row=1, column=2, sticky=W+E)
button_7.grid(row=1, column=3, sticky=W+E)

button_result.grid(row=0, column=3, sticky=W+E)
button_cl.grid(row=1, column=3, sticky=W+E)
button_tochka.grid(row=1, column=4, sticky=W+E)
# ................................................... #
'''/////////////////////////////////////////////////'''
# .......... свойства полей ввода и вывода .......... #
entry_input1 = Entry(f_input1, validate='key')
entry_input2 = Entry(f_input2, validate='key')

entry_input1['validatecommand'] = (entry_input1.register(autoclear), '%S', '%P')
entry_input2['validatecommand'] = (entry_input2.register(autoclear), '%S', '%P')

entry_input1.bind('<FocusIn>', activate_entry1)
entry_input2.bind('<FocusIn>', activate_entry2)

entry_input1.grid(row=0, column=0)
entry_input2.grid(row=0, column=0)
# ................................................... #
'''/////////////////////////////////////////////////'''
# .................... опции меню ................... #
do_menu = Menu(mainmenu, tearoff=0)
do_menu.add_command(label='Сложение', command=printpl)
do_menu.add_command(label='Вычитание', command=printmin)
mainmenu.add_cascade(label='Действия', menu=do_menu)

clear_menu = Menu(mainmenu, tearoff=0)
clear_menu.add_command(label='Число 1', command=clear1)
clear_menu.add_command(label='Число 2', command=clear2)
clear_menu.add_command(label='Вывод', command=clear_output)
clear_menu.add_command(label='Всё', command=clear_all)
mainmenu.add_cascade(label='Очистить', menu=clear_menu)

mainmenu.add_command(label='О программе', command=about)
# ................................................... #
'''/////////////////////////////////////////////////'''
# ................. свойства текста ................. #
label_output = Label(f_output, text=result)
label_output.grid(row=0, column=0)

label_plus = Label(text='+')
label_minus = Label(text='-')
# ................................................... #
'''/////////////////////////////////////////////////'''
# ............... Отрисовка элементов ............... #
printpl()

f_input1.grid(row=0, column=0, columnspan=2, padx=53, pady=1)
f_input2.grid(row=2, column=0, columnspan=2, padx=53, pady=1)
f_output.grid(row=3, column=0, columnspan=2, padx=53, pady=1)

f_button.grid(row=5, column=0, padx=53, pady=10, sticky=E)
f_result.grid(row=5, column=1, padx=53, pady=10, sticky=W)

root.mainloop()
