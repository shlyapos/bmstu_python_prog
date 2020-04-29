# Матрицы.

# Программа удаляет строки начинающиеся с элемента, отличного от малой
# латинской буквы, и сортирует строки по алфавиту, рассматривая только
# первый элемент.

# Переменные:
#           N  - Количество строк в матрице;
#           B  - Исходная матрица;
#           D  - Сформированная матрица;
#          i,j - Переменные для цикла for; 


N=int(input('Введите количество строк в матрице: '))
B=[[str(j) for j in input('Введите элементы {}-й строки матрицы через пробел\
: '.format(i+1)).split()]for i in range(N)]

def Procedure(D,N,i=0):
    while i<N:
        if not('a'<=D[i][0]<='z'):
            D.remove(D[i])
            N-=1
        else:
            i+=1
    for i in range(len(D)-1):
        for j in range(len(D)-2,i-1,-1):
            if D[j][0]>D[j+1][0]:
                D[j],D[j+1]=D[j+1],D[j]
    print('\nПолученная матрица:')
    for i in range(len(D)):
        print('\t'.join(map(str,D[i])))
        
print('\nИсходная матрица:')
for j in range(len(B)):
    print('\t'.join(map(str,B[j])))
Procedure(B,N)
    

