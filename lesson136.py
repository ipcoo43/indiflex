# Even Coller Regex Version
# 줄을 뽑았는데, 이 줄을 택하지 않을 거라면 건너뛰기가 가능하게 한다 
# 맞는 줄을 찾으면 데이터를 뽑는다거나
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:15 2008'
# '^From .*@([^ ]*)'
# ^From 시작 해야 한다.
# 그리고 공백이 따라 나오고
# .* 아무 문자나 몇 번이든 나온 다음에 @가 나온다.
# From이 매치가 되고 공백이 나왔고 쭉 아무 문자나 나오다가 @이 나오고 추출을 시작한다
# ([^ ]*) 공백아님, 공백아님을 추출하는 것이다.
y = re.findall('^From .*@([^ ]*)',line)
print(y)

# 앞에 방법은 매치되는 줄에서 잘 작동하지만 
# 우리가 필요요 하지 않는 줄에서도 작동하고 있다.
# '^From .*@([^ ]*)'은 이런 것들을 고쳐 줄 수 있다.
# 우리가 찾고자 하는 라인만 찾을 수 있다.
# if 구문과 같은 개념이다.
# 나누는 것과 추출하는 것이 동시에 일어 난다.
# 매칭되는 문자열이 추출되는 것보다 크기 때문이다.
# 데이터를 남기지 않는 방법이다.