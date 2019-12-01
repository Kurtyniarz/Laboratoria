import re

str = '(111-22-33)'
formated = re.sub('[^0-9]+', '', str)
print(formated)