import re

str = '600-700-8001'

compiled = re.compile('(.*)-(.*)-(.*)').match(str)


print(compiled.group(1), compiled.group(2), compiled.group(3))
