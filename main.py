import random

colors = ['blue', 'green', 'red', 'yellow', 'black', 'white']
code = []

lenCode = 0
while lenCode < 4:
    code.append(random.choice(colors))
    lenCode += 1

#print('Kod', code)
print('Odgadnij kod i zostań Mistrzem Intelektu!\n'
      'Twoim zadaniem jest jak najszybsze odgadnięcie kodu, który jest kombinacją ustawienia w szeregu, 4 spośród 6 kolorów, z możliwymi powtórzeniami.\n'
      'Wprowadź swoją pierwszą kombinację kolorów: blue, green, red, yellow, black, white, \n'
      'a otrzymasz podpowiedzi, które przybliżą Cię do odgadnięcia kodu w kolejnych kombinacjach. Powodzenia. Czas Start! ')

userCode = []
i = 0
while i < 4:
    part = input('Podaj kolor\n')

    if part != 'blue' and part != 'green' and part != 'red' and part != 'yellow' and part != 'black' and part != 'white':
        print('Wybrano błędny kolor.')
    else:
        userCode.append(part)
        i += 1

for x in userCode:
    i = 0
    redPoint: int = 0
    while i < 4:
        if userCode[i] == code[i]:
            redPoint += 1
        i += 1

print('Sprawdzana kombinacja', userCode)
print('Ilość kolorów na swoim miejscu', redPoint)
















