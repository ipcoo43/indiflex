import re

souce_a = "dodo/mimi/solsol/lala,sisis"
# \/+ -> 해당 규칙을 반복하라
mat_1 = re.compile('\/+')
print(mat_1.split(souce_a))
# ['dodo', 'mimi', 'solsol', 'lala,sisis']