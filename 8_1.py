OAK = {'WBC': 13.3, 'RBC': 4.32, 'HGB': 127, 'HTC': 34.1, 'MCV': 78.9, 'MCH': 29.4, 'MCHC': 372, 'PLT': 292}
print(len(OAK))
print('Эритроциты', OAK['RBC'])
if OAK['HTC'] < 32.5:
    print('Гематокрит ниже нормы')
elif OAK['HTC'] >= 32.5 and OAK['HTC'] <= 41:
    print('Гематокрит норма')
elif OAK['HTC'] > 41:
    print('Гематокрит выше нормы')
OAK['MPV'] = float(input())
if OAK['MPV'] < 9.4:
    print('Средний объем тромбоцитов ниже нормы')
elif OAK['MPV'] > 12.4:
    print('Средний объем тромбоцитов выше нормы')
else:
    print('Средний объем тромбоцитов норма ')
OAK['WBC'] = 9.3
print(OAK)