class Person:
    def __init__(self, fam, im, ot, birthday):# указать входные параметры для конструктора
        self.fam = fam
        self.im = im
        self.ot = ot
        self.birthday = birthday # описать конструктор


class Students(Person):
    def __init__(self, fam, im, ot, birthday):# указать входные параметры для конструктора
        super().__init__(fam, im, ot, birthday)
        self.courses = []
         # описать конструктор

    def add_curse(self, curses):# указать входные параметры
       self.courses.append(curses)
     # Описать функцию

    def add_mark(self, lector, curses, mark):# указать входные параметры
        if curses in self.courses:
            if curses in lector.lectures:
                lector.grades[curses] = lector.mark
                lector.mark.append(mark)
            else:
                print('Действие отменено')
        else:
            print('Действие отменено')


class Lectors(Person):
    def __init__(self, fam, im, ot, birthday, experience):# указать входные параметры для конструктора
        super().__init__(fam, im, ot, birthday)
        self.experience = experience
        self.lectures  = []
        self.mark =[]
        self.grades = {}
    
    def lecture_and_mark(self):
        for lecture, mark in self.grades.items():
            avg = sum(mark)/len(mark)
        return(f'{lecture} - {round(avg, 1)}')

    def info(self):
        print(
f'''Информация по преподавателю {self.fam} {self.im:.1}.{self.ot:.1}.
Дата рождения - {self.birthday}
Стаж - {self.experience}
Список читаемых лекций - {', '.join(self.lectures)}
Имеет следующий рейтинг по предметам:
{Lectors.lecture_and_mark(self)}'''
)

	
	
Ivan = Students('Иванов', 'Иван', 'Иванович', '01.01.2000')
Ivan.add_curse('Анатомия')
Ivan.add_curse('Физиология')
Ivan.add_curse('Биология')
Anna = Students('Косинцева', 'Анна', 'Петровна', '01.05.2001')
Anna.add_curse('Анатомия')
Anna.add_curse('Патологическая физиология')
Pavel = Lectors('Кузнецов', 'Павел', 'Владимирович', '01.12.1972', 10)
Pavel.lectures = ['Физиология', 'Патологическая физиология', 'Анатомия']
Ivan.add_mark(Pavel, 'Физиология', 3)
Ivan.add_mark(Pavel, 'Физиология', 2)
Ivan.add_mark(Pavel, 'Биология', 2)
Anna.add_mark(Pavel, 'Физиология', 3)
Anna.add_mark(Pavel, 'Патологическая физиология', 3)
Anna.add_mark(Pavel, 'Патологическая физиология', 5)
Anna.add_mark(Pavel, 'Патологическая физиология', 5)
Anna.add_mark(Pavel, 'Патологическая физиология', 5)
print(Pavel.grades)
#Pavel.info()