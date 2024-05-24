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
        if curses in lector.lectures:
            if curses in self.courses:
                if curses not in lector.grades:
                    lector.grades[curses] = []
                lector.grades[curses].append(mark)
            else:
                print("Действие отменено")
        else:
            print("Действие отменено")


class Lectors(Person):
    def __init__(self, fam, im, ot, birthday, experience):# указать входные параметры для конструктора
        super().__init__(fam, im, ot, birthday)
        self.experience = experience
        self.lectures  = []
        self.grades = {}
    
    def lecture_and_mark(self):
        for lecture, mark in self.grades.items():
            avg = sum(mark)/len(mark)
        return(f'{lecture} - {round(avg, 1)}')

    def info(self):
        print(f'Информация по преподавателю {self.fam} {self.im:.1}.{self.ot:.1}.')
        print(f'Дата рождения - {self.birthday}')
        print(f'Стаж - {self.experience}')
        if self.lectures:
            print(f"Список читаемых лекций - {', '.join(self.lectures)}")
        self.display_grades()
    def display_grades(self):
 
        if self.grades:
            print("Имеет следующий рейтинг по предметам:")
            for subject, grades in self.grades.items():
                if grades:
                    avg_grade = round(sum(grades) / len(grades), 1)
                    print(f"{subject} - {avg_grade}")

	
	
	
Ivan = Students('Иванов', 'Иван', 'Иванович', '01.01.2000')
Ivan.add_curse('Анатомия')
Ivan.add_curse('Физиология')
Ivan.add_curse('Биология')
Pavel = Lectors('Кузнецов', 'Павел', 'Владимирович', '01.12.1971', 9)
Pavel.lectures = ['Физиология', 'Патологическая физиология']
Ivan.add_mark(Pavel, 'Анатомия', 5)
Ivan.add_mark(Pavel, 'Физиология', 3)
Ivan.add_mark(Pavel, 'Физиология', 2)
Ivan.add_mark(Pavel, 'Физиология', 2)
Pavel.info()