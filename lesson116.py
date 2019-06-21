# Tuples and Deictionaries ( 튜플 및 딕셔너리 )
# The items() method in dictionaries returns a list of (key,value) tuples
# 사전의 items () 메서드는 (키, 값) 튜플의 목록을 반환합니다.

# 튜플은 딕셔너리와 관련이 있다.

# 빈 딕셔너리를 만들어 d에 넣어주고
# 그러면 d는 키와 값을 담을 수 있는 공간이 생성된다.
d = dict()
# 'csev'를 key로 2를 값으로 넣어주고
d['csev'] = 2
# 'cwen'를 key로 4를 값으로 넣어주고
d['cwen'] = 4

# 그러면 이 딕셔너리에
# 'csev'와 2, 'cwen'과 4사이에 연관된 매핑이 만들어진다.

# 키와 값의 쌍으로 루프를 돌리게 되면 어떻게 될까요?
# 반복변수 (k,v)는 튜플이다.
# 이제 키가 없을 때까지 튜플에 할당된다.
# 첫 번째가 키이고, 두 번재가 값이다.
# k,v는 여기서 연속적으로 키와 값을 받으며 루프를 돌게 된다.
# 두번 돈다. k,v가 'csev',2가 되고, 다시 'cwen',4가 되고
# 순서는 원래 순서 대로 돈다.
for (k,v) in d.items():
    print(k, v)

# 근데 만약에 딕셔너리에 뭐가 있는지 궁금하다면
# 딕셔너리에 내장된 items() 메서드를 사용한면 된다.
# d.items()을 사용하고 튜플의 값을 받아온 뒤
tups = d.items()
# 출력 한다
print(tups)

# 결국 이건 특별한 종류의 클래스이고
# 일종의 튜플로 이루어진 리스트라고 보면 된다.
# dict_items([('csev', 2), ('cwen', 4)])
# ('csev', 2)은 0번이고
# ('cwen', 4)은 1번이다.
# 튜플이 2개인 리스트이다.
# k, v는 d.items()을 반복하며 계속 루프를 돌아서 나온다.
