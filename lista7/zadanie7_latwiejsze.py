# Aplikacja blog
import pickle
import time


def wypisz_blog():
    try:
        plik = open('baza.txt', 'rb')
        odszyfrowane = pickle.load(plik)
        plik.close()
        for wpis in reversed(odszyfrowane['wpisy']):
            print(f"Wpis: {wpis['opis']}, data: {wpis['data']}")
    except EOFError:
        print('Plik jest pusty')


def zapisz_wpisz(wpis):
    try:
        plik = open('baza.txt', 'rb')
        odszyfrowane = pickle.load(plik)
        plik.close()
        odszyfrowane['wpisy'].append({
            'opis': wpis,
            'data': str(time.ctime(time.time()))
        })
        plik = open('baza.txt', 'wb')
        pickle.dump(odszyfrowane, plik)
        plik.close()
        main()
    except EOFError:
        baza = {}
        baza['wpisy'] = []
        baza['wpisy'].append({
            'opis': wpis,
            'data': str(time.ctime(time.time()))
        })
        plik = open('baza.txt', 'wb')
        pickle.dump(baza, plik)
        plik.close()
        main()


def main():
    wypisz_blog()
    a = str(input('Dodaj nowy wpis: '))
    zapisz_wpisz(a)


if __name__ == '__main__':
    main()
