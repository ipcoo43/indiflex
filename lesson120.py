# Sort by values instead of key ( 키 대신 값으로 정렬 )
# If we could construct a list of tuples of the form (value,key) we could sort by value
# (value, key) 형식의 튜플 목록을 만들 수 있다면 값으로 정렬 할 수 있습니다.
# We do this with a for loop that creates a list of tuple
# 튜플 목록을 생성하는 for 루프를 사용하여이 작업을 수행합니다

# 키가 아닌 값을 가지고 정렬, 자료 구조와 연관이 많다.
# 어덯게 구조를 잡아야 문제를 쉽게 접근 할지?
# 만들 자료 구조는 튜플로 된 리스트인데, 값이 처음에, 키가 뒤에 나온다
# item()을 쓰면 키의 값이 나오는데, 값이 앞에 나오길 원한다.
# 그래서 순서를 바꾸어 준다.

c = {'a':10, 'b':1, 'c':22}
tmp = list()
# c.items()에서 k,v를 꺼내 온다, 이것은 정렬이 되어 있지 않다.
for k,v in c.items():
    # tmp에 items()에서 나온 튜플을 넣어 준다
    # 튜플로 이루어진 리스트가 된다
    # 이 때 키와 값의 순서를 뒤집어 넣는다.
    # 값이 앞에, 키가 뒤에 가도록 (v,k)로 넣어서 리스트를 만든다
    tmp.append((v,k))

# 정렬 할 수 있는 자료 구조로 바뀌었다.
print(tmp)
# [(10, 'a'), (1, 'b'), (22, 'c')]

# 인메모리 변수에 저장되어 있는 리스트가 나온다
# 값이 첫 번째 있어서 sorted 할 수 있다.
# sorted() 리스트가 어떻게 만들어 졌는지 상관없이 정렬
# reverse=True를 해주면 내림차순으로 나오게 된다.
# 가장 큰 값이 맨 앞에 오고 tmp에 넣어 준다.
# 값의 내림차순으로 출력된다.
tmp = sorted(tmp, reverse=True)
print(tmp)
# [(22, 'c'), (10, 'a'), (1, 'b')]
# (값,키) 내림차순의로 정렬된다.

# 임시로 리스트하나 만든 것이 과정을 간략하게 만들어 준다