#def IMT(m, h):
#    h = h / 100
#    imt = m / h**2
#    imt = round(imt, 1)
#
#    if imt < 16:
#        return(imt, 'Выраженный дефицит массы тела')
#    elif imt <= 18:
#        return(imt, 'Дефицит массы тела')
#    elif imt <= 24:
#        return(imt, 'Нормальная масса тела')
#    elif imt <= 29:
#        return(imt, 'Избыточная масса тела (предожирение)')
#    elif imt <= 34:
#        return(imt, 'Ожирение первой степени')
#    elif imt <= 39:
#        return(imt, 'Ожирение второй степени')
#    elif imt > 40:
#        return(imt, 'Ожирение третьей степени')
#
#imt, text = IMT(80,177)
#print(f'Ваш индекс массы тела составляет {imt}. {text}.')

def IMT(m, h):
    h = h / 100
    imt = m / h**2
    imt = round(imt, 1)

    if imt < 16:
        return(imt, 'Выраженный дефицит массы тела')
    elif imt <= 18:
        return(imt, 'Дефицит массы тела')
    elif imt <= 24:
        return(imt, 'Нормальная масса тела')
    elif imt <= 29:
        return(imt, 'Избыточная масса тела (предожирение)')
    elif imt <= 34:
        return(imt, 'Ожирение первой степени')
    elif imt <= 39:
        return(imt, 'Ожирение второй степени')
    elif imt > 40:
        return(imt, 'Ожирение третьей степени')

imt, text = IMT(80,177)
print(f'Ваш индекс массы тела составляет {imt}. {text}.')