pacients  = [('Журавлева', 'Валерия', 'Владиславовна', '89088487781', 56, '+'), ('Завьялов', 'Лев', 'Владиславович', '89128487188', 26, '-'), ('Зайцев', 'Никита', 'Алексеевич', '89877777188', 80, '-'), ('Захарова', 'Маргарита', 'Марковна', '8955555118', 16, '+')]
new_pacient = input().split() #Добавляем ФИО отдельными элементами
new_pacient.append(input()) #Добавляем телефон отдельным элементом
new_pacient.append(int(input().strip())) #Добавляем возраст отдельным элементом
new_pacient.append(input().strip()) #Добавляем наличие ковида отдельным элементом
pacients.append(tuple(new_pacient))
#Далее Ваш код...
for i in pacients:
    if i[-1] == '+' and i[-2] > 50:
        print(f'{i[0]} {i[1][0]}.{i[2][0]}. {i[3]}')