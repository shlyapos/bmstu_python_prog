from math import sqrt

x,y=map(float,input('Введите координаты точки: ').split())
if y<=(-abs(x-2)-2) and (y**2)>=(1-(x-2)**2) and y>=0:
    print('Принадлежит')
else:
    print('Не принадлежит')
input('\nНажмите Enter для завершения.')

                   
      
      
      
