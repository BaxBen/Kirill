n = str(input("Введите пол (м/ж): "))
v = int(input("Введите возраст: "))
r = int(input("Введите количество расстояний R-R, которое необходимо проанализировать: "))
b = 0
for i in range(r):
    a = float(input(f"Введите {i + 1}-е расстояние R-R в мм: "))
    b += a
time_s = (b / 25) / r
css = round((60 / time_s))
if v >= 20 and v <= 40:
    if n == 'м':
        if css >= 60 and css <= 75:
            diagnez ='Норма.'
        elif css < 60:
            diagnez = 'Брадикардия.'
        elif css > 75:
            diagnez = 'Тахикардия.'
    elif n == 'ж':
        if css >= 65 and css <= 80:
            diagnez = 'Норма.'
        elif css < 65:
            diagnez = 'Брадикардия.'
        elif css > 80:
            diagnez = 'Тахикардия.'
elif v >= 40 and v <=60:
    if n == 'м':
        if css >= 70 and css <= 85:
            diagnez = 'Норма.'
        elif css < 70:
            diagnez = 'Брадикардия.'
        elif css > 85:
            diagnez = 'Тахикардия.'
    elif n == 'ж':
        if css >= 75 and css <= 90:
            diagnez = 'Норма.'
        elif css < 75:
            diagnez = 'Брадикардия.'
        elif css > 90:
            diagnez = 'Тахикардия.'
elif v < 20 or v > 60:
    if css >= 60 and css <= 80:
        diagnez = 'Норма.'
    elif css < 60:
            diagnez = 'Брадикардия.'
    elif css > 80:
        diagnez = 'Тахикардия.'
print(f'ЧСС составляет {css} уд/мин. {diagnez}')
