class liczba_losowa:
    def losuj01(self):
        from random import random
        return print(random())


class inna_losowa(liczba_losowa):
    def __init__(self, option):
        self.run(option)

    def run(self, option):
        if option == 1 or option == '1':
            self.losuj01()
        elif option == 2 or option == '2':
            self.randomInt()
        elif option == 3 or option == '3':
            self.randomFloat()

    def randomInt(self):
        from random import randint
        value = randint(0, 10)
        print(value)

    def randomFloat(self):
        from random import gauss
        value = gauss(0, 10)
        print(value)


newLiczba_Losowa = liczba_losowa()

print('-----------------------')
print('Liczba losowa [0,1]')
newLiczba_Losowa.losuj01()
print('-----------------------')
print('Wybierz operacje:')
print('1.Podstawowa')
print('2.Calkowita losowa')
print('3.Zmiennoprzecinkowa losowa')
try:
    opcja = int(input(''))
    newInna_Losowa = inna_losowa(opcja)
except ValueError:
    print('Zly format.')

