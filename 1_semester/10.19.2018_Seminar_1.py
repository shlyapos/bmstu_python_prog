n=int(input('Введите количество студентов: '))
t=list(map(float,input('Введите время обслуживания для {} студентов в одну\
 строку: '.format(n)).split()))

c=[0]*n
min=t[0]
mint=1

for i in range(n):
    c[i]=c[i-1]+t[i]
    if t[i]<min:
        mint=i+1
        min=t[i]

print('\nНомер студента   Время пребывания')

for i in range(n):
    print('   ',(i+1),'               ',c[i])

print('\nНомер студента с минимальным временем обслуживания:',mint)
input('\nНажмите Enter для завершения.')
        
    
      
