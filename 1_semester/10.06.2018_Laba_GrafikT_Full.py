# Черчение графика функции.

# Программа получает на вход диапазон аргумента x и шаг, с которым он
# изменяется, и выводит график зависимости z(x).

# Графики: z1=x-cos(x);
#          z2=1.8*x**4+2.6*x**3-2.3*x**2+10.1*x-7.1;

# Переменные: z - значение функции; 
#             x - Аргумент;
#             d1,d2 - Диапазон аргумента x;
#             sh - Шаг с которым изменяется аргумент x;
#             minz,maxz - Минимальное и максимальное (соостветственно)
# значение функции которое достигается при определённом аргументе x;
#             size - размер поля для вывода функции;         
#             y0 - Положение y=0 на графике;
#             l - Суммарное количество аргументов x при заданном диапазоне;
#             n - Порядковый номер операции;

from math import *

d1,d2=map(float,input('Введите диапазон аргумента x: ').split())
sh=float(input('Введите шаг изменения аргумента x: '))

l=(d2-d1)/sh

x=d1*10
n=0
y=x/10
z2=1.8*y**4+2.6*y**3-2.3*y*y+10.1*y-7.1
maxi=z2
maxa=-11
print('\n\nПодсчёт значений z1 и z2 при различном аргументе x:\n')
print('┌─────────┬────────────┬──────────────┬────────────────────┐')
print('│  Номер  │ Аргумент x │      Z1      │         Z 2        │')
while n<=l:
    y=x/10
    z1=y-cos(y)
    z2=1.8*y**4+2.6*y**3-2.3*y*y+10.1*y-7.1
    x+=(sh*10)
    if z2>maxi:
        maxi=z2
        maxa=y
    n+=1
    if z1>=10000:
        if z2<=10000:
            print('├─────────┼────────────┼──────────────┼────────────────────┤')
            print('│{:5d}    │{:9.1f}   │{:12.3e}  │ {:15.3f}    │'.format(n,y,z1,z2))
        else:
            print('├─────────┼────────────┼──────────────┼────────────────────┤')
            print('│{:5d}    │{:9.1f}   │{:12.3e}  │ {:15.3e}    │'.format(n,y,z1,z2))
    elif z2<=10000:
        print('├─────────┼────────────┼──────────────┼────────────────────┤')
        print('│{:5d}    │{:9.1f}   │{:12.3f}  │ {:15.3f}    │'.format(n,y,z1,z2))
    else:
        print('├─────────┼────────────┼──────────────┼────────────────────┤')
        print('│{:5d}    │{:9.1f}   │{:12.3f}  │ {:15.3e}    │'.format(n,y,z1,z2))
print('└─────────┴────────────┴──────────────┴────────────────────┘')
if maxi<=1000:
    maxi='{:7.3f}'.format(maxi)
elif maxi>=1000:
    maxi='{:7.3e}'.format(maxi)
print('Максимальное значение функции z2:',maxi)
print('Значение аргумента x при котором оно достигается:',maxa)

minz=d1-cos(d1)
maxz=minz
x=d1*10
size=60
f=False
while x<=(d2*10):
    y=x/10
    z=y-cos(y)
    if z<minz:
        minz=z
    elif z>maxz:
        maxz=z
    x+=1
if minz<0<maxz:
    print('График функции z1=x-cos(x)\n')
    y0=round(-minz/(maxz-minz)*size)
    l=(d2-d1)/sh
    if 0<=y0<=size:
        ystep=max(y0,size-y0)//2
        print(ystep)
        if ystep > y0:
            print('  {}   0.0{}{:4.2e}'.format(' '*(y0 - 1),' '*(ystep - 2),
                   (y0+ystep)*(maxz-minz)/size+minz))
            print('  {:4.2e}{}{:4.2e}'.format(minz,' '*(size-9),maxz))
            print('    ┌┼','─'*(y0-1),'┼','─'*ystep,'┼','─'*(size-y0-ystep-1),
                  '┼', '─'*8,'► Y',sep='')   
        elif ystep>size-y0:
            print('{}{:4.2e}{}   0.0'.format
                  (' '*(ystep-2),ystep*(maxz-minz)/size+minz,' '*(y0-ystep-8)))
            print('  {:4.2e}{}{:4.2e}'.format(minz,' '*(size-9),maxz))
            print('    ┌┼','─'*(ystep-1),'┼','─'*(y0-ystep-1),'┼','─'*(size-y0),
                  '┼','─'*8,'► Y',sep='')
        else:
            print('  {}{:4.2e}{}   0.0{}{:4.2e}'.format
                  (' '*(ystep - 2),
                   ystep*(maxz-minz)/size+minz,
                   ' '*(y0-ystep-8),' '*(ystep-3),
                   (y0+ystep)*(maxz-minz)/size+minz))
            print('  {:4.2e}{}{:4.2e}'.format
                  (minz,' '*(size-9),maxz))
            print('    ┌┼','─'*(ystep - 1),'┼','─'*(y0 - ystep - 1),'┼',
                  '─'*(ystep-1),'┼','─'*(size - y0-ystep),
                  '┼','─'*8,'► Y',sep='')
        x=d1*10
        n=0
        while n<=l:
            n+=1
            y=x/10
            z=max(round((y-cos(y)-minz)/(maxz-minz)*size),0)
            if z<y0:
                if f:
                    print('{:4.0f}{}{}{}{}{}{}{}{:7.3f}'
                          .format(n,'│',' '*z,'*',' '*(y0-z-1),'│',' '*(size-y0),
                                  '│',y))
                else:
                    print('{:4.0f}{}{}{}{}{}{}{}'
                          .format(n,'│',' '*z,'*',' '*(y0-z-1),'│',' '*(size-y0),
                                  '│'))
            elif z==y0:
                if f:
                    print('{:4.0f}{}{}{}{}{}{:7.3f}'
                          .format(n,'│',' '*z,'*',' '*(size-y0),'│',y))
                else:
                    print('{:4.0f}{}{}{}{}{}'
                          .format(n,'│',' '*z,'*',' '*(size-y0),'│'))
            else:
                if f:
                    print('{:4.0f}{}{}{}{}{}{}{}{:7.3f}'
                          .format(n,'│',' '*y0,'│',' '*(z-y0-1),'*',' '*(size-z),
                                  '│',y))
                else:
                    print('{:4.0f}{}{}{}{}{}{}{}'
                          .format(n,'│',' '*y0,'│',' '*(z-y0-1),'*',' '*(size-z),
                                  '│'))
            x+=sh*10
            f=not(f)
    else:
        ystep=size//3
        print(ystep)
        print('  {}{:4.2e}{}{:4.2e}'.format
              (' '*(ystep - 1),
               ystep*(maxz - minz)/size+minz,' '*(ystep-8),
               2*ystep*(maxz-minz)/size+minz))
        print('  {:4.2e}{}{:4.2e}'.format
              (minz,' '*(size-8),maxz))
        print('    ┌┼','─'*(ystep - 1),'┼','─'*(ystep - 1),'┼',
              '─'*(size - ystep * 2),'┼','─'*8,'► Y',sep='')
        x=d1*10
        n=0
        while n<=l:
            n+=1
            y=x/10
            z=max(round((y-cos(y)-minz)/(maxz-minz)*size),0)
            if f:
                print('{}{}{}{}{:7.5f}'
                      .format(' '*z,'*',' '*(size-z),'│',y))
            else:
                print('{}{}{}{}'
                      .format(' '*z,'*',' '*(size-z),'│'))
            x+=sh*10
            f=not(f)
else:
    z=1.8*x**4+2.6*x**3-2.3*x**2+10.1*x-7.1
    minz=z
    maxz=minz
    x=d1*10
    while x<=(d2*10):
        y=x/10
        z=1.8*x**4+2.6*x**3-2.3*x**2+10.1*x-7.1
        if z<minz:
            minz=z
        elif z>maxz:
            maxz=z
        x+=1
    print('График функции z2=1.8*x**4+2.6*x**3-2.3*x**2+10.1*x-7.1\n')
    y0 = round(-minz/(maxz - minz)*size)
    l=(d2-d1)/sh
    ystep = max(y0, size - y0)//2
    print(ystep)
    if ystep>y0:
        print('  {}   0.0{}{:4.2e}'.format(' '*(y0-1),' '*(ystep-2),
               (y0+ystep)*(maxz-minz)/size+minz))
        print('  {:4.2e}{}{:4.2e}'.format(minz,' '*(size-9),maxz))
        print('    ┌┼','─'*(y0-1),'┼','─'*ystep,'┼','─'*(size-y0-ystep-1),
              '┼','─'*8,'► Y',sep ='')      
    elif ystep>size-y0:
        print('  {}{:4.2e}{}   0.0'.format
              (' '*(ystep-2),
               ystep*(maxz-minz)/size + minz,
               ' '*(y0-ystep-8)))
        print('  {:4.2e}{}{:4.2e}'.format(minz,' '*(size-9),maxz))
        print('    ┌┼','─'*(ystep-1),'┼','─'*(y0-ystep-1),'┼','─'*(size-y0),
              '┼','─'*8,'► Y',sep ='')
    else:
        print('  {}{:4.2e}{}   0.0{}{:4.2e}'.format
              (' '*(ystep-2),ystep*(maxz-minz)/size+minz,' '*(y0-ystep-8),
               ' '*(ystep-3),
               (y0+ystep)*(maxz-minz)/size+minz))
        print('  {:4.2e}{}{:4.2e}'.format
              (minz,' '*(size-9),maxz))
        print('    ┌┼','─'*(ystep-1),'┼','─'*(y0-ystep-1),'┼','─'*(ystep-1),
              '┼','─'*(size-y0-ystep),'┼','─'*8,'► Y',sep='')
    x=d1*10
    n=0
    while n<=l:
        n+=1
        y=x/10
        z1=1.8*y**4+2.6*y**3-2.3*y**2+10.1*y-7.1
        z=max(round((z1-minz)/(maxz-minz)*size+0.5),0)
        if z<y0:
            if f:
                print('{:4.0f}{}{}{}{}{}{}{}{:7.3f}'
                      .format(n,'│',' '*z,'*', ' '*(y0-z-1),'│',' '*(size-y0),
                              '|',y))
            else:
                print('{:4.0f}{}{}{}{}{}{}{}'
                      .format(n,'│',' '*z,'*', ' '*(y0-z-1),'│',' '*(size-y0),
                              '|'))
        elif z==y0:
            if f:
                print('{:4.0f}{}{}{}{}{}{:7.3f}'
                      .format(n,'│',' '*z,'*',' '*(size-y0),'│',y))
            else:
                print('{:4.0f}{}{}{}{}{}'
                      .format(n,'│',' '*z,'*',' '*(size-y0),'│'))
        else:
            if f:
                print('{:4.0f}{}{}{}{}{}{}{}{:7.3f}'
                      .format(n,'│',' '*y0,'│',' '*(y-y0-1),'*',' '*(size-y),
                              '│',y))
            else:
                print('{:4.0f}{}{}{}{}{}{}{}'
                      .format(n,'│',' '*y0,'│',' '*(y-y0-1),'*',' '*(size-y),
                              '│'))
        x+=sh*10
        f=not(f)
print(' '*y0,'    │')
print(' '*y0,'    ▼')
input('\nНажмите Enter для завершения.')
