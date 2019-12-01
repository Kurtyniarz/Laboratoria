import re

str = 'labpyt2019@gusun_tomail.pl'
mo = re.search('(.*)usun_to(.*)', str)
print(mo.group(1) + mo.group(2))

