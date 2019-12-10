import re

str = '111-22-33'
formated = re.sub('-', '', str)
print(formated)
