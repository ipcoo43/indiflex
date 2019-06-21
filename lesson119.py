# Using sorted() 
# We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequence
# 시퀀스를 매개 변수로 사용하고 정렬 된 시퀀스를 반환하는 내장 함수 sorted를 사용하면 훨씬 더 직접적으로 이 작업을 수행 할 수 있습니다.

d = {'a':10, 'b':1, 'c':22}
# sorted에서는 키를 기준으로 정렬된 값이 나온다
t = sorted(d.items())
print(t)
# [('a', 10), ('b', 1), ('c', 22)]

# 반복 변수(k,v)는 sorted안의 키와 값이다.
# 꺼내 오기 전에 sorted를 통해 정렬하고, d.items()에서 꺼내온다.
# a,b,c가 매번 차례대로 나오게 된다.
# v는 key인 k에 대응되는 값을 가져와서 정렬된다.
for k,v in sorted(d.items()):
    print(k, v)
