import re

pattern = 'aza'
str1 = 'aza1103bbb'

match1 = re.match(pattern,str1)
print(match1.group()) # 'aza'