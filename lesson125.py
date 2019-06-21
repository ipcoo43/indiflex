# Using re.search() like startswith()
# 정규식에는 특별한 문자가 있다.

# 파일을 열고
hand = open('mbox-short.txt')
# 한 줄씩 순회하며
for line in hand:
	# 줄 끝에 \n을 제거하고
	line = line.rstrip()
	# find()를 사용하지 않고
	# startswith()을 통해 'From:'으로 시작하는 문장의 처음에 나오는 것만 찾겠다.
	if line.startswith('From:'):
		print(line)

import re
# 파일을 열고
hand = open('mbox-short.txt')
# 한 줄씩 순회하며
for line in hand:
	# 줄 끝에 \n을 제거하고
	line = line.rstrip()
	# re.search()를 통해서 'From:'으로 시작하는 단어만 찾겠다
	if re.search('^From', line):
		print(line)

# re.search('^From', line)
# 정규식을 보면 첫 번째 매개 변수만 넣어주면 된다
# 줄의 시작을 의미하는 ^을 넣어 준다.
# ^은 줄의 시작을 의미하는 가상의 문자
# 이건 이렇게 시작하는 문자열이라는 뜻이다.
# 처음에 나오는 경우만 찾고 중간에 나오는 경우는 무시 한다.
# line은 검색 대상이다.
# ^From은 시작하는 부분에서 살펴볼 대상이라는 뜻 이다.
# 이러면 맨 앞이 from:인 line만 찾아내서 출력 한다.

# 두 구문의 차이는 일반함수를 사용했냐, 정규식을 사용했냐 일 뿐이다.