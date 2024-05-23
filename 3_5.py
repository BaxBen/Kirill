p = 'да'
while p == 'да':
    n = str(input("Введите пол (м/ж): "))
    ag = int(input("Введите возраст (года): "))
    w = int(input("Введите вес (кг): "))
    cr = int(input("Введите клиренс креатинина сыворотки (ммоль/л): "))
    skf = int((140 - ag) * w / (cr * 72))
    if n == "ж":
        skf = skf * 0.85
        print(f'СКФ = {round(skf)}')
    else:
        print(f'СКФ = {round(skf)}')
    
    if skf > 90:
        print(f"Нормальная СКФ.")
    elif skf <=89 and skf >= 60:
        print(f"Повреждение почек с умеренным снижением СКФ.")
    elif skf <= 59 and skf >= 30:
        print(f"Средняя степень снижения СКФ.")
    elif skf <= 29 and skf >= 15:
        print(f"Выраженная степень снижения СКФ.") 
    elif skf < 15:
        print(f"Почечная недостаточность.")
    p = str(input("Рассчитать еще раз? (да/нет):"))
    