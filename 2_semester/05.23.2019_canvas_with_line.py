# Нахождение точек по обе стороны от прямой.

'''
На плоскости задано множество точек.
Провести прямую по данным точкам так, чтобы кол-во точек с одной
и с другой стороны от прямой отличалось минимально.
Дать графическое изображение результатов.
'''

from tkinter import *
from tkinter import messagebox as mb

root = Tk(className='Построение прямой')

fr_input = LabelFrame(root, text='Ввод данных')

# Формирование таблицы значений с координатами точек
def input_points():
    global number
    global ent_point
    
    number = ent_points.get()

    if (number == '' or number == '0' or ('a' <= number <= 'z')
        or ('а' <= number <= 'я') or number == '1'):
        mb.showerror("Ошибка", 'Введите корректные данные')
    else:
        number = int(number)
        point_name = [0] * number
        ent_point = point_name
        for i in range(number):
            point_name[i] = Label(fr_input,
                                  text='Точка ' + str(i + 1))
            point_name[i].grid(row=i+1, column=0)
            
            ent_point[i] = Entry(fr_input)
            ent_point[i].grid(row=i+1, column=1)

        lbl_instr = Label(fr_input,
                          text='Ввод координат производится через пробел')
        lbl_instr.grid(row=0, column=0, columnspan=2)
            
        butt_build = Button(fr_input, text='Начать построение',
                            command=start_building)
        butt_build.grid(row=(number + 2), column=0, columnspan=2,
                        sticky='NSWE')

# Проверка на пустоту полей ввода координат точек
def check_empty():
    global number
    global ent_point
    
    for i in range(number):
        s = ent_point[i].get()
        if s == '':
            mb.showerror("Ошибка", 'Заполните все поля')
            return False
        
    return True

# Нахождение координат прямой, которая удовлетворяет условию
def find_points(x_crd, y_crd):
    left = 0
    right = 0
    diff = 1000
    point1 = list()
    point2 = list()
    for i in range(len(x_crd)):
        for j in range(len(x_crd)):
            if i != j:
                for p in range(len(x_crd)):
                    if p != i and p != j:
                        D = ((x_crd[p] - x_crd[i]) * (y_crd[j] - y_crd[i]) -
                             (y_crd[p] - y_crd[i]) * (x_crd[j] - x_crd[i]))
                        if D < 0:
                            left += 1
                        elif D > 0:
                            right += 1
                    
                if abs(left - right) < diff:
                    diff = abs(left - right)
                    point1 = []
                    point2 = []
                    point1.append(x_crd[i])
                    point1.append(y_crd[i])
                    point2.append(x_crd[j])
                    point2.append(y_crd[j])
                left = 0
                right = 0
            
    return point1, point2

# Масштабирование координат
def scaling(x_arr, y_arr):
    global win_x
    global win_y

    x_min = min(x_arr)
    x_max = max(x_arr)

    y_min = min(y_arr)
    y_max = max(y_arr)

    x_min -= (x_max - x_min) / 10
    x_max += (x_max - x_min) / 10
    y_min -= (y_max - y_min) / 10
    y_max += (y_max - y_min) / 10

    x_pixel = list()
    y_pixel = list()

    for i in range(len(x_arr)):
        x_pixel.append(win_x * ((x_arr[i] - x_min) / (x_max - x_min)))
        y_pixel.append(win_y * ((y_max - y_arr[i]) / (y_max - y_min)))

    return x_pixel, y_pixel
'''
def print_line(y, point1, point2):
    x = (((y - point1[1]) * (point2[0] - point1[0])) /
         point2[1] - point1[1]) + point1[0]
    return x
'''
# Построение графика из заданных точек
def start_building():
    global number
    global ent_point
    global win_x
    global win_y
    global eps

    out = check_empty()

    if out:
        x_crd = list()
        y_crd = list()
        for i in range(len(ent_point)):
            s = ent_point[i].get()
            a = list(s.split())
            x_crd.append(float(a[0]))
            y_crd.append(float(a[1]))

        scaled_x, scaled_y = scaling(x_crd, y_crd)
        
        x_crd = scaled_x
        y_crd = scaled_y

        point1 = list()
        point2 = list()

        point1, point2 = find_points(x_crd, y_crd)

        diff_x = point2[0] - point1[0]
        diff_y = point2[1] - point1[1]
            
        win_canvas = Toplevel()
        c = Canvas(win_canvas, width=win_x, height=win_y, bg='white')
        c.pack()
        
        if abs(point1[0] - point2[0]) < eps:
            c.create_line(point1[0] - diff_x*1000, point1[1] - diff_y*1000,
                          point1[0] + diff_x*1000, point2[1] + diff_y*1000,
                          width=4)
        elif abs(point1[1] - point2[1]) < eps:
            c.create_line(point1[0] - diff_x*1000, point1[1] - diff_y*1000,
                          point2[0] + diff_x*1000, point1[1] + diff_y*1000,
                          width=4)
        else:
            c.create_line(point1[0] - diff_x*1000, point1[1] - diff_y*1000,
                          point2[0] + diff_x*1000, point2[1] + diff_y*1000,
                          width=4)
            
        for i in range(len(x_crd)):
            c.create_oval(x_crd[i], y_crd[i],
                          x_crd[i], y_crd[i], width=3)

''' Константы '''
win_x = 640
win_y = 640
number = ''
ent_point = list()
eps = 1e-5

lbl_points = Label(root, text='Количество точек: ')
ent_points = Entry(root, width=10)
butt_start = Button(root, text='Ввести координаты точек',
                    command=input_points)

''' Отрисовка элементов '''
lbl_points.grid(row=0, column=0, sticky='W')
ent_points.grid(row=0, column=1)
butt_start.grid(row=1, column=0, columnspan=2)

fr_input.grid(row=2, column=0, columnspan=2)

root.mainloop()
