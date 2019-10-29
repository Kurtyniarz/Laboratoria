def norecursive(word):
    return word == word[::-1]


def recursive(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return recursive(word[1:-1])


a = str(input('Podaj slowo: '))

if norecursive(a):
    print('(bez rekurencji)Jest palindromem.')
else:
    print('(bez rekurencji)Nie jest palindromem.')

if recursive(a):
    print('(rekurencja)Jest palindromem.')
else:
    print('(rekurencja)Nie jest palindromem.')
