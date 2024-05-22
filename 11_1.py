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

#list_pulse = [68, 118, 110, 61, 58, 66, 104, 106, 96, 67]
#
#def pulse(input_pulse):
#    copy = list_pulse.copy()
#    copy.append(int(input_pulse))
#    sum_pulse = sum(copy)
#    avg_pulse = sum_pulse / len(copy)
#    avg_pulse = round(avg_pulse)
#    print(f'Средний пульс пациента составляет {avg_pulse} уд/мин')
#pulse(input())