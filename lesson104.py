import re
source_a = 'dodo/mini//solsol///lala,sisi'

mat_1 = re.compile('\/+')
print(mat_1.split(source_a))
# ['dodo', 'mini', 'solsol', 'lala,sisi']

mat_2 = re.compile('\/+|\,+')
print(mat_2.split(source_a))
# ['dodo', 'mini', 'solsol', 'lala', 'sisi']

# complie 메소드와 split을 한 줄로 코딩
print(re.split('\/+|\,+',source_a))
# ['dodo', 'mini', 'solsol', 'lala', 'sisi']