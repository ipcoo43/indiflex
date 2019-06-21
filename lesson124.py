# Using re.search() like find()

# From:이 들어가는 줄을 찾고 있다.
# 우선 파일을 열고
hand = open('mbox-short.txt')
# 파일을 전부 순회 한다.
for line in hand:
	# 줄들의 \n을 제거하고
	line = line.rstrip()
	# From:이 들어간 줄을 뽑아 낸다
	# line.find가 0보다 크면 출력하겠다.
	# 만약에 해당 문자열이 없다면 -1을 리턴하기 때문이다.
	# line.find() 좀 더 객체 지향적이다.
	if line.find('From:') >= 0:
		print(line)
# 모든 줄을 쭉 읽고 한 바퀴를 돌면서 출력 한다.
# 건초더미에서 바늘찾기 이다.

# 정규식을 사용하기 위해 라이브러리를 가져왔다.
import re
# 파일을 열고
hand = open('mbox-short.txt')
# 한 줄을 읽어 들이고
for line in hand:
	# 읽어 들이면서 \n은 제거하고
	line = line.rstrip()
	# re.search()를 사용하려면 라이브러리는 꼭 있어야 한다.
	# re.search()는 문자열 줄에서 지정된 문자열을 찾는다.
	# line은 찾을 대상이다.
	# re.search()는 line을 매개 변수로 넘겨 준다.
	if re.search('Form:', line):
		print(line)

# 두 방식은 잠시 동안 모든 줄을 돌면서 
# 조건에 맞는 줄을 찾게 되면 매칭되는 줄을 출력한다.
# line.find()가 하는 역할을 re.search()가 했다.