import urllib.request, urllib.parse, urllib.error
def copy_file():
    urllib.request.urlretrieve('https://raw.githubusercontent.com/zahoff/task11/main/11_01pulse/pulse001.txt', 'pulse001.txt')

copy_file() #После выполнения данной функции в рабочей папке появится файл pulse001.txt для анализа

pulse_now = input('Пульс сейчас ')
with open('pulse001.txt', 'a') as file:
    file.write(pulse_now)

with open('pulse001.txt', 'r') as file:
    sum_pulse = 0
    list_pulse = file.read().split()
    for i in list_pulse:
        sum_pulse += int(i)
    avg_pulse = sum_pulse/len(list_pulse)
    avg_pulse = round(avg_pulse)
print(f'Средний пульс пациента составляет {avg_pulse} уд/мин')
