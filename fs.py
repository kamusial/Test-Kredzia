#from f1 import PLNtoUSD
import f1
from f2 import czyzdolny
from f3 import inwest


x = int(input('Ile masz PLN? '))
x = f1.PLNtoUSD(x)
print(f'Masz {x} USD')

tmp = input('Czy jestes facetem?  T/N ')
if tmp == 'T' or tmp == 't' or tmp == 'Tak':
    plec = True
else:
    plec = False
wiek = int(input('Podaj wiek '))
sprawnosc = int(input('Podj sprawnosc 0 - 10 '))

if czyzdolny(plec, wiek, sprawnosc) == True:
    inwest(x)
else:
    print('Nie inwestuj')
