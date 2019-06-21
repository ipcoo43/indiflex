# Spam confidence
# 숫자를 다 찾은 다음. 그 중에서 가장 큰 값을 구한다.

import re
# 파일에서 줄을 읽어 들이고
hand = open('mbox-short.txt')
numlist = list()
# for 반복문을 만들어 줄을 읽어오고
# 파일에 있는 모든 줄에 대해 block을 반복한 것이다.
for line in hand:
	# 줄 끝의 \n을 제거하고
	line = line.rstrip()
	# 정규식을 이용해 필요한 줄만 가져 온다.
	# ^X-DSPAM-confidence:로 시작하는 것만 보겠다.
	# 엄격한 기준을 설정하는 것이다.
	# ^X-DSPAM-confidence:로 시작하지 않으면 보지도 않을 것이다.
	#  ([0-9.]+) 공백이 하나 있고 그리고 ()로 추출을 시작한다
	# 숫자나 .을 포함해서 가장 긴 문자열을 가져오고
	# []는 문자하나, 그리고 +는 하나 이상이라는 뜻
	# 탐욕적이게 추출하다가 멈춘다
	# 만약에 특정 줄이 이 패턴을 만족시키지 못하면 작동하지 않는다.
	stuff = re.findall('^X-DSPAM-confidence: ([0-9.]+)', line)
	# 가장 먼저 매치되는 것을 보겠다
	# 리스트에 아이템이 몇 개인지 보고
	# 1이 아니면 continue
	# 밑의 과정은 수행하지 않는다
	if len(stuff) != 1:
		continue
		# 계속 진행하다가 매치되는 순간 밑의 코드를 실행한다.
	# 모든 줄이 생략되고 그러다가 패턴을 만족하는 게 나오면 
	# 숫자를 구해 부동 소수점으로 바꿔주고
	num = float(stuff[0])
	# 리스트에 넣어준다.
	# 리스트에 정보가 저장된다.
	# 프로그램이 돌아갈수록 리스트도 점점 커지게 된다.
	numlist.append(num)
	# 최댓값을 구한다.
print('Maxinum:',max(numlist))
