import dbm

try:
    with dbm.open('cache', 'c') as db:
        db[b'baza'] = b'Witaj w bazie danych'
        db['costam'] = 'kolejna dana zapisana w bazie'
        db['jeszczeinnadana'] = 'ostatni zapis w bazie'

        print(db.get('baza'))
        print(db.get('costam'))
        print(db.get('jeszczeinnadana'))
except dbm.error as error:
    print(error)
