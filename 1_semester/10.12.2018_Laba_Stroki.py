# Нахождение слов.

# На вход программе подаётся строка, найти в ней слова с максимальным
# количеством буквы с и вывести их.

# Переменные:
#           stroka - Введённая строка;
#           maxkol - Максимальное количество букв;
#           kol    - Количесвто букв в слове;
#           i      - Переменная для цикла for;
#           word   - Слово в строке;

stroka=str(input('Введите строку: '))

stroka+=' '
maxkol=0
kol=0
word=''

for i in stroka:
    while i!=' ':
        if i=='c':
            kol+=1
        break
    if i==' ':
        if maxkol<kol:
            maxkol=kol
        kol=0
if maxkol==0:
    print('\nНет слов содержащих букву с.')
else:
    if maxkol==1:
        print('\nСлова содержащие 1 букву с:')
    elif maxkol==2 or maxkol==3 or maxkol==4:
        print('\nСлова содержащие {} буквы с:'.format(maxkol))
    else:
        print('\nСлова содержащие {} букв с:'.format(maxkol))
        
    for i in stroka:
        while i!=' ':
            if i=='c':
                kol+=1
            word+=i
            break
        if i==' ':
            if kol==maxkol:
                print(word)
            kol=0
            word=''
input('\nНажмите Enter для завершения.')

            
     
