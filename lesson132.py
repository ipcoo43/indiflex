# Fine-Trnning String Extraction

# '^From (\S+@\S+)' ()를 사용하고 있다.
# From으로 시작해야하고 
# 그 다음 공백이 나오고
# 하나 이상의 문자가 나오고 
# @가 나오고 
# 다시 하나 이상의 문자가 나온다
# 그러면 From이 없으면 만족하지 않다
# From을 시작해야만 하고 공백도 있어야 한다.
# 공백 아닌 문자가 나온고, 그리고 @까지 매칭되고, 공백을 만나면 멈춘다.
# From은 빼고 stephen.marquard@uct.ac.za만 원한다.
# 그래서 ()를 사용해야 한다.
# ()는 코드가 아니다. 정규식에 포함되지 않는다는 뜻이다.
# 추출 시작점과 끝점을 지정해주는 역할만 한다.
# ()를 치지 않으면 From 전체를 돌려받았는데
# '^From (\S+@\S+)' ()를 사용하면 From을 조건에 넣으면서도 추출은 ()만 할 수 있다.
# 돌려 받는 부분은 변하지 않게 지정해 주고 
# 어떤 걸 리턴 받을지 정해줄 수도 있다.
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14 2008'
y = re.findall('\S+@\S+',x)
print(y)  # ['stephen.marquard@uct.ac.za']

y = re.findall('^From (\S+@\S+)',x)
print(y) # ['stephen.marquard@uct.ac.za']