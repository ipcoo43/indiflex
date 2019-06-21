# Retriving lists of keys and values
# 키 및 값 목록 검색
# You can get a list of keys, vlues, or items(both) from a dictionary
# 사전에서 키, 값 또는 항목 (구입 한 항목)의 목록을 가져올 수 있습니다.
# 기존의 딕셔너리와 동일한 키를 가지며 키로만 구성 리스트를 얻는다.

jjj = { 'chuck':1, 'fred':42, 'jan':100}
# 기존의 딕셔너리와 동일한 키를 가지며 키로만 구성되어 있다.
print(list(jjj))
# 다른 방법으로 keys 메소드를 이용하여 키로 구성된 리스트를 얻을 수 있다.
print(jjj.keys())
# jjj.keys()라는 표현을 통행 키로 구성된 리스트를 주는 똑깥은 일을 한다.
print(jjj.values())
# 딕셔너리에서 값만 달라고 할 수도 있다.

# 나오는 순서를 예측 할 수 없다
# 각각의 키와 값을 물어보는 위 두개의 구문의 경우
# 나오는 나오는 순서는 예측할 수 없지만 둘은 같은 순서로 나온다
# 세 번째 방법은 items() Method 이다.
print(jjj.items())
# 원소를 직접 물어보는 것이다.
# 딕셔너리 원소를 달라고 하면 리스트를 주는데
# 이는 우리가 다루는 첫 번째 복합적인 자료 구조 형태이다.
# 리스트 안에 세 개의 원소가 있고
# 각 원소는 두 개의 원소로 구성된 튜플로 되어 있다.


