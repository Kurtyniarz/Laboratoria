import os
import re


# JAK PANI ZAPYTA CZEMU OS.WALK, A NIE OS.PATH.WALK, TO DLATEGO,
# ZE KURWA OS.PATH.WALK JUZ NIE ISTNIEJE. JA NIE WIEM SKAD ONA BIEZRE TE POMYSLY
# OGOLEM POPRAWNE ZADANIE TO JEST TA PIERWSZA WERSJA, TA DRUGA ZOSTAWIAM

# Using os.path.walk / os.walk
def findPathsN():
    paths = []
    for root, dirs, files in os.walk('./'):
        for name in files:
            if re.search("(.*?)praca(.*?)pdf$", name):
                if root == './':
                    paths.append(f'{root}{name}')
                else:
                    paths.append(f'{root}/{name}')

    for f_path in paths:
        print(f_path)


# Using without os.path.walk / os.walk
def findPaths():
    main_catalog = os.listdir('./')
    needed_paths = []

    dirs_only = []
    for name in main_catalog:
        if os.path.isdir(name):
            dirs_only.append(name)
        if re.search("(.*?)praca(.*?)pdf$", name):
            needed_paths.append(f'./{name}')

    for d_name in dirs_only:
        catalog = os.listdir(f'./{d_name}')
        for f_name in catalog:
            if re.search("(.*?)praca(.*?)pdf$", f_name):
                needed_paths.append(f'./{d_name}/{f_name}')

    for f_path in needed_paths:
        print(f_path)


findPathsN()
# findPaths()
