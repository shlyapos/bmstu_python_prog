x=list(map(float,input('Введите поочереди координаты точек по x: ').split()))
y=list(map(float,input('Введите поочереди координаты точек по y: ').split()))

from math import *

ud=sqrt(x[0]**2+y[0]**2)
bliz=ud

for i in range(len(x)):
    if y[i]>=0:
        rast=sqrt(x[i]**2+y[i]**2)
        if rast>ud:
            udx=x[i]
            udy=y[i]
            ud=rast
        elif rast<bliz:
            blizx=x[i]
            blizy=y[i]
            bliz=rast

print('Самая удалённая:',udx,',',udy,', самая близкая:',blizx,',',blizy)
rastt=sqrt((blizx-udx)**2+(blizy-udy)**2)
print('Расстояние между этими точками: {:4.4f}'.format(rastt))
input('\nНажмите Enter для завершения.')
    
    
    
    
    

            
    
    
