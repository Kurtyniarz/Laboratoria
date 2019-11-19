class Student:
    def __init__(self, imie, nazwisko, rok, grupa, nr_albumu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok = rok
        self.grupa = grupa
        self.nr_albumu = nr_albumu

        self.wypisz_studenta()

    def wypisz_studenta(self):
        print(f'Imie: {self.imie}')
        print(f'Nazwisko: {self.nazwisko}')
        print(f'Rok: {self.rok}')
        print(f'Grupa: {self.grupa}')
        print(f'Numer Albumu: {self.nr_albumu}')
        print(f'\n\n')

    def zmien_rok(self, rok):
        self.rok = rok
        self.wypisz_studenta()

    def zmien_grupa(self, grupa):
        self.grupa = grupa
        self.wypisz_studenta()

    def zmien_album(self, nr_albumu):
        self.nr_albumu = nr_albumu
        self.wypisz_studenta()

student1 = Student('Jan', 'Kowalski', '2019', 'A', '123456')

student1.zmien_grupa('B')

