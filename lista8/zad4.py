import re

str = '600-700-8001'

compiled = re.compile('(.*)-(.*)-(.*)')
return_value = compiled.match(str)

print(return_value.group(1) + return_value.group(2) + return_value.group(3))
