# Работа с файлами

# Программа открывает указанные файлы и совершает с ними операции

# Переменные:
# choice - Выбор пользователя
# file_name - Имя файла
# infile - Открытие файлов
# outfile - Файл с полученным ответом
# numb_str - Количество записей
# field - Поля в записях
# word -
# summ - Сумма стоимости всех автомобилей
# number - Количество заданных автомобилей

file_name=('None')

choice=None
while choice != '0':
    print('\n// Имя используемого файла /',file_name)
    print('\n',':'*79)
    print('''
            [1] - Выбор файла
            [2] - Создание в файле нового
                  набора записей
            [3] - Добавление записей
            [4] - Вывод всех записей
            [5] - Поиск по 1-му полю
            [6] - Поиск по 2-м полям
            [7] - Средняя стоимость 


            [0] - Выход
''')
    print(':'*79)
    choice=input('\n// Команда / ')

    if choice == '1':
        file_name = 'None'
        while file_name == 'None':
            file_name = input('\n// Введите имя файла / ')
            try:
                infile = open(file_name)
            except:
                print('// Файл не найден')
                file_name = 'None'

    elif choice == '2':
        infile=open(file_name,'w')

    elif choice == '3':
        infile=open(file_name,'a')
        numb_str=int(input('\n// Введите количество записей / '))

        print('\n// Введите строки /')
        
        for i in range(numb_str):
            print(input(),file=infile)
        infile.close()
            
    
    elif choice == '4':
        print('\n')
        infile=open(file_name,'r')
        string=' '

        if file_name!='None':

            while string!='':
                string=infile.readline()
                if string!='':
                    print(string)
        else:
            print('\n// Файл не выбран')

    elif choice == '5':
        print('\n// Поиск по 1-му полю')

        infile = open(file_name,'r')
        index = int(input('\n// Введите номер поля / '))
        field = input('\n// Введите значение поля / ')
        print('\n')
        string = ' '
        matrix = []
        
        if file_name!='None':
            
            while string!='':
                string = infile.readline()
                if string != '':
                    matrix.append(string)

            for i in range(len(matrix)):
                if i != len(matrix)-1:
                    matrix[i]=matrix[i][:(len(matrix[i])-1)]
                    
                stroka=[]
                word=''
                
                for j in range(len(matrix[i])):
                    if matrix[i][j] != ' ':
                        word+=matrix[i][j]
                    else:
                        if word != '':
                            stroka.append(word)
                        word=''
                stroka.append(word)

                if stroka[index-1]==field:
                    print(matrix[i])
                    
    elif choice == '6':
        print('\n// Поиск по 1-му полю')

        infile = open(file_name,'r')
        index1 = int(input('\n// Введите номер 1-го поля / '))
        field1 = input('// Введите значение 1-го поля / ')
        index2 = int(input('\n// Введите номер 2-го поля / '))
        field2 = input('// Введите значение 2-го поля / ')
        print('\n')
        
        string = ' '
        matrix = []
        f=0
        
        if file_name!='None':

            print('// Вывод ')
            
            while string!='':
                string = infile.readline()
                if string != '':
                    matrix.append(string)

            for i in range(len(matrix)):
                if i != len(matrix)-1:
                    matrix[i]=matrix[i][:(len(matrix[i])-1)]
                    
                stroka=[]
                word=''
                
                for j in range(len(matrix[i])):
                    if matrix[i][j] != ' ':
                        word+=matrix[i][j]
                    else:
                        if word != '':
                            stroka.append(word)
                        word=''
                stroka.append(word)

                if stroka[index1-1]==field1 and stroka[index2-1]==field2:
                    f=1
                    print(matrix[i])
            if f==0:
                print('// Полей не найдено')

    elif choice == '7':
        print('\n// Расчёт стоимости марки автомобиля')

        field=input('\n // Введите марку автомобиля /')
        outfile=open('txt3.txt','w')
        summ=0
        number=0

        if file_name!='None':
            infile = open(file_name,'r')
            string=' '
            
            while string!='':
                if string!='':
                    string = infile.readline()
                    
                if string[-1]=='\n':
                    string=string[:-1]
                    
                    
                word=''
                stroka=[]
                
                for i in range(len(string)):
                    if string[i] != ' ':
                        word+=string[i]
                    else:
                        if word != '':
                            stroka.append(word)
                        word=''
                stroka.append(word)

                for p in stroka:
                    if p == field:
                        summ+=int(stroka[2])
                        number+=1
            if number != 0:              
                sr_cost=summ/number
                
            
        print(str(sr_cost),file=outfile)
        outfile.close()
                        
    elif choice == '0':
        print('// Выход')

    else:
        print('\n// Нет такой команды')
