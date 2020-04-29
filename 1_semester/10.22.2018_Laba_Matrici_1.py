 # Работа с матрицей.

# На вход программа получает квадратную матрицу и разворачивает её на
# 90 градусов по часовой стрелке.

# Переменные:
#            n  - Размер квадратной матрицы
#            A  - Квадратная матрица
#           i,j - Счётчики для циклов for
#           r=n-1-i
#           rj=n-1-j


n=int(input('Введите количество строк и столбцов: '));
print()
A=[[float(j) for j in input('Введите элементы {}-й строки: '.format(i+1))
    .split()] for i in range(n)]

for i in range(len(A)):             # Вывод исходной матрицы
    print('\t'.join(map(str,A[i])))
    
for i in range(n//2):
    r=n-1-i
    for j in range(i,r):
        rj=n-1-j
        t=A[rj][i]
        A[rj][i]=A[r][rj]
        A[r][rj]=A[j][r]
        A[j][r]=A[i][j]
        A[i][j]=t
        
for i in range(len(A)):         # Вывод повёрнутой матрицы
    print('\t'.join(map(str,A[i])))
    
input('\nНажмите Enter для завершения.')
