import random

colors = ["blue", "green", "red", "yellow", "black", "white"]
code = []

lenCode = 0
while lenCode < 4:
    code.append(random.choice(colors))
    lenCode += 1

#print(code)

print("Odgadnij kod i zostań Mistrzem Intelektu!\n"
      "Twoim zadaniem jest jak najszybsze odgadnięcie kodu, który jest kombinacją ustawienia w szeregu, 4 spośród 6 kolorów, z możliwymi powtórzeniami.\n"
      "Wprowadź swoją pierwszą kombinację, a otrzymasz podpowiedzi, które przybliżą Cię do odgadnięcia kodu. Czas Start! ")

userCode = []
i = 0
while i < 4:
    part = input("Podaj kolor\n")
    userCode.append(part)
    i += 1

#print(userCode)















