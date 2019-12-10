import os
import re


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


findPathsN()

