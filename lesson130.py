# Non-Greedy Matching

# ^F.+?:
# F로 시작하고, 아무 문자나 오고,
# ?으로 탐욕적이지 않은 짧은 선택을 해준다
# 주로 *? 또는 +?로 쓰인다.
# *?는 0 또는 그 이상이면서 탐욕적이지 않다.
# +?는 1 또는 그 이상이면서 탐욕적이지 않다.
# 탐욕적인게 기본이고 탐욕적이지 않은게 선택 사항이다.

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)   # ['From:']