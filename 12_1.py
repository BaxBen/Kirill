class Person:
    def __init__(self, fam, im, ot, birthday):# указать входные параметры для конструктора
        self.fam = fam
        self.im = im
        self.ot = ot
        self.birthday = birthday # описать конструктор


class Students(Person):
    def __init__(self, fam, im, ot, birthday, courses ):# указать входные параметры для конструктора
        super().__init__(fam, im, ot, birthday)
        self.courses = []
         # описать конструктор

    def add_curse(self, curses):# указать входные параметры
       self.courses.append(curses)
     # Описать функцию

    def add_mark(self):# указать входные параметры
        if 
        pass# Описать функцию

class Lectors(Person):
    def __init__(self, fam, im, ot, birthday, experience):# указать входные параметры для конструктора
        super().__init__(fam, im, ot, birthday)
        self.experience = experience
        self.lectures  = []
        self.grades = {}
        pass # описать конструктор

    def info(self):
        print(
            ''' '''
        )
        pass# Описать функцию