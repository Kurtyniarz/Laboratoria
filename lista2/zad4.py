kraje = ['Holandia', 'Islandia', 'Rosja', 'Belgia', 'Wlochy', 'Czechy', 'Jamajka']
miasta = ['Amsterdam', 'Reykjavik', 'Moskwa', 'Bruksela', 'Rzym', 'Praga', 'Kingston']

print('Najbardziej chcialby odwiedzic ' + kraje[6] + ', ktorego stolica jest ' + miasta[6])

print('Reszta kraji: ')

for i in range(0, (len(kraje) - 1)):
    if i == 6:
        continue
    print('Panstwo: ' + kraje[i] + ', stolica: ' + miasta[i])
