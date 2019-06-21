# String Parsing Examples
# 호스트 이름을 찾고자 한다. 이메일 네임이 호스트 이름이다.
# 문자열에서 @을 찾으면 된다.

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:15 2008'
# find()가 @가 21번 위치에 있다는 걸 알려 준다
atpos = data.find('@')
print(atpos)  # 21

# 그 뒤에 공백을 찾는데, 공백은 31번에 있다.
sppos = data.find(' ',atpos)
print(sppos)  # 31

# 이제 추출을 @뒤에서 시작해서 공백 전까지로 지정할 수 있다.
# atpos + 1 : @뒤에서 시작
# sppos : 공백 전까지
# host가 두 값을 받아서 슬라이싱 한다
host = data[atpos + 1 : sppos]
print(host)  # uct.ac.za

# 이렇게 호스트 정보가 추출된다.