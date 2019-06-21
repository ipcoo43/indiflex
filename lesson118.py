# Sorting Lists of Tuples (튜플 목록 정렬하기)
# We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
# 튜플 목록을 정렬하여 정렬 된 버전의 사전을 얻는 기능을 활용할 수 있습니다.
# First we sort the dictionary by the key using the items() method and sorted() function
# 먼저 items () 메서드와 sorted () 함수를 사용하여 키로 사전을 정렬합니다.

# 튜플 정렬하기
# 튜플로 이루어진 리스트 생성  그리고 정렬
# 딕셔너리에서 튜플을 뽑아서 튜플로 이루어진 리스트를 만들어 정렬
# 딕셔너리를 리스트로 바꾸고 리스트를 정렬

# a는 10, b는 1, c는 22인 딕셔너리
d = { 'a':10, 'b':1, 'c':22}
# items()를 써보면 매핑된 대로 나온다
# 순서가 뒤죽박이다.
d.items()
# dict_items([('a', 10), ('b', 1), ('c', 22)])
# 여기서 sorted()를 써주는 것이다.
# 시퀀스를 받아서 정렬한 뒤에 리턴 해준다.
# 리스트를 받아서 a,b,c를 비교
# 딕셔너리이기 때문에 각 키들은 겹치지 않는다. 그래서 키로 정렬한다.
# 값은 비교하지 않는다.
# 딕셔너리는 항상 유일하고 구별할 수 있는 키를 가진다.
# sorted(d.items())라고 하면 키를 sorted 안으로 전달하고
# sorted는 쭉 정렬되어서 나오게 된다.
sorted(d.items())
#  [('a', 10), ('b', 1), ('c', 22)]

# 뒤의 값들은 고려하지않고
# 앞의 키의 값들의 오름차순으로 정렬한다.