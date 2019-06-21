# 파일을 읽고 그 안의 모든 단어를 세는 동작을 한다.
# 사용자에게 파일을 물어보고
name = input('Enter file: ')
# 파일을 열고
handle = open(name)

# 빈 딕셔너리를 생성한다.
counts = dict()
# 반복 변수로 파일의 문장을 차례로 받는다.
# 한 줄, 한 줄 처리하고  
for line in handle:
    # 해당 문장을 단어 단위로 나눌 것이다.
    # 따라서 words는 한 줄을 자른 단어가 담긴 리스트이다.
    # 모든 줄에 대해 같은 동작을 한 것이다.
    words = line.split()
    # 그 다음 반복 변수 word를 사용하여 
    # 각 줄의 단어에 대해 살펴볼 것이다.
    # 각 줄의 단어들을 돌며
    # 히스토그램을 만들 것이다.
    # 이 for 문은 모든 줄에 대해서만이 아니라
    # 각 줄의 모든 단어에 대해 실행된다.
    # 모든 줄에 대해 중첩된 루프를 적용하여
    # 각 줄을 단어 단위로 나누고 
    # 타자기 처럼 다음 줄로 간다.
    # 한 줄을 처리하여 히스토그램을 만들고
    # 다음 줄로 가서 같은 일을 한다.    
    # 마치 바깥 루프는 아랫줄로 계속 내려가고
    # 안쪽의 루프는 옆으로 가는 느낌이다.
    # 최족정으로 마지막 줄에서는 
    # 파일의 모든 단어가 담겨있을 것이고
    # 그것을 가지고 히스토그램 만들기를 한다.
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# 히스토그램이 변수 counts에 만들어져 있다.
# 이제 가장 많이 나온 단어를 찾아야 한다.
# 딕셔너리에서 가장 큰 값을 가진 키와 값 쌍을 찾고 싶다.
# 어떤 것이 가장 큰 값이며
# 그 값을 가진 단어는 무엇인지 알아야하므로
# 처음에는 None이로 초기화 한다.

bigcount = None
bigword = None
# for 루프는 None부터 비교하기 시작 한다.
# 2개의 반복 변수와 for문 형식을 이용하여
# items() 메소드가 있으므로
# word, count가 키와 값 쌍을 돌 것 이다.
# 그 값이 무엇이든 루프를 이용하여
# 키와 값 쌍을 순서대로 받을 것이다.
for word,count in counts.items():
    # bigcount가 현재 가장 큰 값인지 확인 한다
    # 값이 None이라면 아직 아무것도 못 봤거나
    # 방금 읽은 count 값이 
    # 지금까지의 bigcount 값보다 큰 경우이다.
    if bigcount in None or count > bigcount:
        # 그러면 이 count 값이 
        # 이 자료 집합안에서 최고 기록임을 인지하고
        # bigcount 값을 바꾼다.
        # word의 값이 bigword에 담기고
        # count의 값이 bigcount에 담긴다.
        bigword = word
        bigcount = count
print(bigword, bigcount)

# 최대값을 찾는 루프
# 가장 큰 값이 몇인지 기록하고
# 그 값에 해당되는 단어는 무엇이지
# 기록하는 기능이 들어가 있는 것이다.

# Dictionaries Summary
# 컬렉션이 무엇인지 이해하기 위해
# 리스트와 디셔너리를 보는 것이 좋다.
# 하나 이상의 대상을 자기 내부에 포함하여 다룬다.
# get() method
# 반복문에서 딕셔너리에 메소드를 적용

