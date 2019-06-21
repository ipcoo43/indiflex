# The top 10 most common words (가장 많이 나오는 단어 10개 뽑아내기)
# 파일을 읽어 fhand에 저장한다
fhand = open('romeo.txt')
# 갯수를 세서 counts에 저장할 딕셔너리를 만든다
counts = dict()
# 줄마다 단어가 있게죠?
# for 루프로 한 줄 씩 파일을 읽어 온다.
for line in fhand:
	# split()을 통해 띄어쓰기를 기준으로 나눈다
	words = line.split()
	# 그리고 다시 for 루프는 split()된 단어들에 대해 돈다
	# 한 줄씩 루프를 돌고, 또 그 한 줄에서 한 단어씩 루프를 돈다
	# 그리고 다시 다음 줄로 가고 다음줄의 단어를 순회하는 것이다.
	for word in words:
		# 결국 이 줄은 단어를 세어서  counts.get(word, 0)에 1을 저장하고
		# 히스토그램이 생성되는 것이다.
		counts[word] = counts.get(word, 0) + 1

# 자 코드의 이 시점에서는 지금 단어별로 갯수만 세고 있다.
# 정렬되지 않았다. 순서를 구해야 한다.
# 튜플로된 리스트를 만들겠다.

lst = list()
for key,val in counts.items():
	# 값과 키의 순서를 바꾸어서 튜플을 만들어 주고
	newtup = (val, key)
	# 이렇게 만들어진 튜플을 리스트에 넣어 준다.
	lst.append(newtup)
	# 그 결과 튜플로된 리스트가 만들어진다.
	# 이 튜플은 값과 키의 순서로 되어 있다.
	# (value, key) 

# lst변수에는 쓸모있는 데이터가 들어가 있다.
# sorted를 사용하면 된다.
# reverse=True를 통해서 내림차순으로 정렬하고
# 그리고 다시 리스트에 돌려 준다.
lst = sorted(lst, reverse=True)

# 값과 키를 출력하는게 아니라
# 가장 높은 값부터 출력이 된다.
# lst[:10] 범위를 지정해서 앞에서부터 10개만 출력 한다.
# 값과 키를 뽑아서 일련의 과정을 반복한는데
for val,key in lst[:10]:
	# 출력할 때는 또 뒤집어 준다.
	# 키와 값의 형태로 출력이 된다.
	print(key,val)