from math import sqrt,exp

a=float(input('Введите аргумент a: '))
c=float(input('Введите аргумент c: '))
x=float(input('Введите аргумент x: '))

usl=(a*x**2)

if usl<c:
    s=2*exp(0.85*a)
elif usl>=c:
    s=sqrt(usl-c)
s=float('{:.7f}'.format(s))
print(s)
input('\nНажмите Enter для завершения.')
