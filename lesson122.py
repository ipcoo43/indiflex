# Even Shorter Version
# list comprehension creates a dynamic list.
# In this case, we make a list of reversed tuples and then sort it.
# 람다를 배우게되는데, closed form이라고 부르는 걸 만든다
# 그걸 쓰면 모든 것을 한 구문으로 해결할 수 있다.
# 여기 보이는 한 줄 짜리 코드가 
# 이전의 프로그램의 절반하는 역할을 수행한다.

c = {'a':10, 'b':1, 'c':22}
# print()가 맨 마지막에 실행된다.
# 그 다음 sorted()가 있다.
# 그리고 sorted()는 리스트를 입력값으로 받고 있다.
# 리스트 표현식이 있다.
# sorted() 결과를 print()하고 있는 것이다.
# [(v,k) for k,v in c.items()]을 list comprehension 이라고 한다
# []는 파이썬에게 '이건 리스트다'하고 얘기해주는 것이다.
# 무엇인가를 나열하거나 상수를 가지는게 아니다.
# 쉼표 하나 둘 세이나 append()를 쓴 것도 아니다.
# 그냥 어떤 표현을 넣어 두었다.
# 그리고 그 표현에 의해서 리스트의 원소가 결정된다.
# 리스트가 두 개의 튜플로 돼 있다.
# (v,k)로 되어 있다는 사실이 내포되어 있다.
# c.items()에 있는 모든 k,v에 대해 for 루프처럼 반복하게 된다.
# 이걸 도장처럼 리스트에 찍어 내다.
# 이걸 계속 반복해서 리스트를 만들어 낸다.
# 리스트가 만들어짐과 동시에 sorted()에 의해 정렬된다.
# 값을 어딘가에 저장하지 않고
# 프로그래머가 설정한 도장찍기 방식에 따라
# 다른 변수나 값의 저장 없이 쭉 리스트를 만들어 낸다.
# 그리고 리스트는 sorted()에 들어 가고 정렬되어져 나온다.
# 여기서는 reverse=True도 사용하지 않는다.
# 그런데 키를 기준으로 오름차순 정렬이 되어 있다.
# 단 한문장으로 모두 처리 한다.
print(sorted([(v,k) for k,v in c.items()]))