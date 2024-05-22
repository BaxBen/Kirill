class Person:
    def __init__(self, fam, im, ot, birthday):
        self.fam = fam
        self.im = im
        self.ot = ot
        self.birthday = birthday
 
class Students(Person):
    def __init__(self, fam, im, ot, birthday):
        super().__init__(fam, im, ot, birthday)
        self.curse = []
    def add_curse(self, curse):
        self.curse.append(curse)
 
    def add_mark(self, lector, curse, mark):
        if curse in self.curse:
            if curse not in lector.grades:
                lector.grades[curse] = []
            lector.grades[curse].append(mark)
        else:
            print("Действие отменено")
        if curse not in lector.lectures:
            print("Действие отменено")
 
class Lectors(Person):
    def __init__(self, fam, im, ot, birthday, experience):
        super().__init__(fam, im, ot, birthday)
        self.experience = experience
        self.lectures = []
        self.grades = {}
        self.srgr=float()
 
    def add_cursed(self, curse):
        self.cursed.append(curse)
        print(add_cursed)
 
    def info(self):
        print(f"Информация по преподавателю {self.fam} {self.im[:1]}.{self.ot[:1]}.")
        print(f"Дата рождения - {self.birthday}")
        print(f"Стаж - {self.experience}")
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
Pavel.info()