import os
import re


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


findPaths()
