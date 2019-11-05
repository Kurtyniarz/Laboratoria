import math


class LogExp:
    definicja = 'log(x, podstawa) - Zwraca logarytm z X o podstawie "podstawa". Jeśli nie jest podana, będzie to logarytm o podstawie 10.'

    def __init__(self, a):
        if a == 0 or a == '0':
            self.a = 10
        else:
            self.a = a

    def defi(self, x):
        print(self.definicja)
        print(math.log(x, self.a))


def main():
    a = int(input('Podaj konstruktor(podstawe logarytmu): '))
    newLogExp = LogExp(a)
    x = int(input('Podaj liczbę, którą chcesz zlogarytmować: '))
    newLogExp.defi(x)


if __name__ == '__main__':
    main()
