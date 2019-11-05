class liczba_losowa:
    def losuj01(self):
        from random import seed
        from random import random
        seed(1)
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
        from random import seed
        from random import randint
        seed(1)
        for _ in range(10):
            value = randint(0, 10)
            print(value)

    def randomFloat(self):
        from random import seed
        from random import gauss
        seed(1)
        for _ in range(10):
            value = gauss(0, 5)
            print(value)


newLiczba_Losowa = liczba_losowa()

newLiczba_Losowa.losuj01()
print('\n-----------------------\n')
print('Wybierz operacje:')
print('1.Podstawowa')
print('2.Kilka calkowitych losowych')
print('3.Kilka calkowitych liczb zmiennoprzecinkowych')
opcja = int(input(''))
newInna_Losowa = inna_losowa(opcja)
