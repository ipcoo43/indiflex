# The Double split pattern

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:15 2008'
# Double split pattern 이다.
# 우선 line을 읽어 들이고
# 공백을 기준으로 단어를 나누어 준다.
words = line.split()
# 1번 위치에 있는게 이메일 주소인 것이다.
# 이메일 주소를 추출하고
# email에 담아주면 된다.
email = words[1]
# 그리고 다시 split()를 해준다
# 이 번에는 @을 기준으로 한다.
# @를 기준으로 나눠진다.
pieces = email.split('@')
# pieces[1]이 호스트가 된다.
print(pieces[1])

# 장점은 추적할 필요가 없다.