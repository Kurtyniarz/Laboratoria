tab = []
print('Podaj tyle liczb ile chcesz. Aby przestac wcisnij enter przy pustym polu')

czypetla = True

while czypetla:
    try:
        a = float(input())
        tab.append(a)
    except ValueError:
        czypetla = False

suma = 0

for n in tab:
    suma += n

avg = suma/len(tab)

print('Srednia liczb:', avg)

if avg % 2 == 0:
    print('Srednia jest parzysta')
else:
    print('Srednia jest nieparzysta')

