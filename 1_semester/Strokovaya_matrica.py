# Строковая матрица.

# Программа получая команды, выполняет определённые команды с заданной матрицей.

# Команды:
#      - Выравнивание по ширине;
#      - Выравнивание по левому краю;
#      - Выравнивание по правому краю;
#      - Замена во всём тексте одного слова другим;
#      - Удаление заданного слова из текста;
#      - Замена арифметических выражений, состоящих
#       из сложения и вычитания, на результат их вычисления.

# Переменные:
#           matrix   - Исходная матрица;
#         matrix_cop - Копия матрицы;
#           choice   - Выбор пользователя;
#           max_len  - Самая длиная строка;
#           stroka   - Строка из строковой матрицы;
#          old_word  - Старое слово/слово которое нужно удалить;
#          new_word  - Новое слово;
#          dlc_word  - Дополнительное слово/строка;
#           space    - Количество пробелов;
#           delta    - Разница пробелов;
#           quant    - Количество различных операций;
#             n      - Длина строки;
#           i,j,p    - Переменные для цикла for;


# Функция преобразует строку в массив содержащий слова и знаки препинания
# -----------------------------------------------------------------------
def massiv(i,matrix,stroka,dlc_word=''):
    for j in range(len(matrix[i])):
        if ('а'<= matrix[i][j] <='я'  or 'a'<= matrix[i][j] <='z' or
            'А'<= matrix[i][j] <='Я' or 'A'<= matrix[i][j] <='Z'):
            dlc_word+=matrix[i][j]
        else:
            stroka.append(dlc_word)
            stroka.append(matrix[i][j])
            dlc_word=''
            
    return stroka

# Функция для определения самой длиной строки
# -------------------------------------------
def maxln(matrix,max_len,i=0):
    for i in range(len(matrix)):
        if len(matrix[i])>max_len:
            max_len=len(matrix[i])
            
    return max_len

# Функция находит полное число из текста справа и слева от операции 
# -----------------------------------------------------------------
def number(i,j,matrix,f=0):
    global old_word
    global new_word
    for p in range(1,len(matrix[i])):
        if '0'<=matrix[i][j+p]<='9':
            new_word+=matrix[i][j+p]
        elif matrix[i][j+p]=='.':
            new_word+=matrix[i][j+p]
            f=1
        elif matrix[i][j+p]==' ':
            break
        
    for p in range(1,len(matrix[i])):
        if '0'<=matrix[i][j-p]<='9':
            old_word=matrix[i][j-p]+old_word
        elif matrix[i][j-p]=='.':
            old_word=matrix[i][j-p]+old_word
            f=1
        elif matrix[i][j-p]==' ':
            break

    if f==0:
        print(old_word,'            ',new_word)
        old_word=int(old_word)
        new_word=int(new_word)
    elif f==1:
        old_word=float(old_word)
        new_word=float(new_word)

    return (old_word, new_word)
    
print('\n// Исходный текст\n')
print('~'*80)
matrix=[
'   π – иррациональное число, то есть 2.2-1.1 его значение не может быть точно',
'выражено в виде дроби m/n, где m и n – целые числа. Следовательно, его',
' десятичное представление никогда не заканчивается и не является',
'периодическим. Иррациональность числа π была впервые доказана',
'  Иоганном Ламбертом в 1761 году путём разложения тангенса в',
' непрерывную дробь. В 1794 году Лежандр привёл более строгое',
'доказательство иррациональности чисел π и π^2.']

matrix_cop=matrix

for i in range(len(matrix)):
    print(matrix[i])
print('~'*80,'\n')

choice=None
while choice!='0':
    print(':'*80)
    print('''
              [1] - Выравнивание по ширине
              [2] - Выравнивание по левому краю
              [3] - Выравнивание по правому краю
              [4] - Замена во всём тексте одного
                  слова другим
              [5] - Удаление заданного слова из
                  текста
              [6] - Замена арифметических выражений,
                  состоящих из сложения и вычитания,
                  на результат их вычисления


              [8] - Показать текст
              [0] - Выход\n''')
    print(':'*80)

    for i in range(len(matrix)):
        j=0
        while matrix[i][j]==' ':        # удаление лишних пробелов
            j+=1
        matrix[i]=matrix[i][j:]
    
    choice=input('\n// Команда / ')
    
    if choice=='0':
        print('\n// Выход...')
        
    elif choice=='1':
        print('\n// Выравнивание по ширине\n')
        matrix=matrix_cop
        
        max_len=len(matrix[0])
        maxln(matrix,max_len)

        for i in range(len(matrix)):
            stroka=[]
            
            massiv(i,matrix,stroka)
            
            delta=max_len-len(matrix[i])
            matrix[i]=''
            p=0
            while stroka[p]==' ':
                stroka.remove(stroka[p])
            
                    
        
    elif choice=='2':
        print('\n// Выравнивание по левому краю\n')
        matrix=matrix_cop

        for i in range(len(matrix)):
            p=0
            while matrix[i][p]==' ':
                p+=1
            matrix[i]=matrix[i][p:]
            
    elif choice=='3':
        print('\n// Выравнивание по правому краю\n')
        matrix=matrix_cop

        max_len=len(matrix[0])
        
        for i in range(len(matrix)):
            j=0
            while matrix[i][j]==' ':        # удаление лишних пробелов
                j+=1
            matrix[i]=matrix[i][j:]
            
        maxln(matrix,max_len)

        for i in range(len(matrix)):
            matrix[i]=' '*(max_len-len(matrix[i]))+matrix[i]
        
    elif choice=='4':
        print('\n// Замена во всём тексте одного cлова другим\n')
        
        old_word=input('// Введите слово которое нужно заменить / ')
        new_word=input('// Введите новое слово / ')
        print('\n')
        
        for i in range(len(matrix)):
            matrix[i]+=' '
            stroka=[]
            
            massiv(i,matrix,stroka)
            
            matrix[i]=''
            quant=0
            
            for p in range(len(stroka)):
                if stroka[p]!=old_word:
                    matrix[i]+=stroka[p]
                else:
                    matrix[i]+=new_word
                    quant+=1
            if quant==0:
                print('// Заданное слово не найдено')
            
    elif choice=='5':
        print('\n// Удаление заданного слова из текста\n')
    
        old_word=input('// Введите слово которое нужно удалить / ')

        for i in range(len(matrix)):
            stroka=[]
            massiv(i,matrix,stroka)
            matrix[i]=''
            quant=0

            for p in range(len(stroka)):
                if stroka[p]!=old_word:
                    matrix[i]+=stroka[p]
                else:
                    quant+=1
        if quant==0:
            print('\n// Заданное слово не найдено\n')
        
    elif choice=='6':
        print('\n// Замена арифметических выражений, состоящих из сложения и\
 вычитания, на результат их вычисления\n')

        for i in range(len(matrix)):
            dlc_word=0
            old_word=''
            new_word=''
            for j in range(len(matrix[i])-1):
                if matrix[i][j]=='+':
                    number(i,j,matrix)
                    dlc_word=old_word+new_word
                elif matrix[i][j]=='-' and '0'<=matrix[i][j+1]<='9':
                    number(i,j,matrix)
                    dlc_word=old_word - new_word
            if dlc_word!=0:
                matrix[i]=matrix[i][:delta]+str(dlc_word)+matrix[i][quant:]
                        
    elif choice=='7':
        pass

    elif choice=='8':
        print('\n// Исходный текст\n')
        print('~'*80)
        for i in range(len(matrix)):
            print(matrix[i])
        print('~'*80,'\n')
        
    else:
        print('\n// Выбранной команды нет\n')
input=('// Нажмите Enter для завершения программы')
