class Person:
    def __init__(self, fam, im, ot, birthday):# указать входные параметры для конструктора
        self.fam = fam
        self.im = im
        self.ot = ot
        self.birthday = birthday # описать конструктор


class Students(Person):
    def __init__(self, fam, im, ot, birthday, courses ):# указать входные параметры для конструктора
        super().__init__(fam, im, ot, birthday)
        self.courses = courses
        pass # описать конструктор

    def add_curse(...):# указать входные параметры
       pass # Описать функцию

    def add_mark(...):# указать входные параметры
        pass# Описать функцию

class Lectors(Person):
    def __init__(self, ...):# указать входные параметры для конструктора
        pass # описать конструктор

    def info(self):
        pass# Описать функцию