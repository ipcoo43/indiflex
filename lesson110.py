# Tuples : 콜렉션 타입
# Tuples are like lists ( 튜플은 목록과 같습니다. )
# Tuples are another kind of sequence that functions much like a list
# 튜플은 목록과 매우 유사한 일련의 시퀀스입니다.
# - they have elements which are indexed starting at 0
# 그들은 0에서 시작하여 색인 된 요소를 가지고있다.

# 튜플은 리스트와 비슷한다. 리스트의 다른 버젼으로 생각한다

# 튜플은 대괄호가 아닌 소괄호를 쓴다는 게 다른 점이다.
# 0,1,2로 위치가 배정됩니다.
x = ('Glenn','Sally','Joseph')
# x[2] 세번째 요소가 된다.
print(x[2])
# 튜플 선언
y = ( 1, 9, 2 )
# 출력하면 소괄호를 쓰고 있어 튜플임을 알 수 있다.
print(max(y))
# 튜플을 for ~ in 뒤에 쓰면
# 튜플을 순회 한다.
# 튜플은 순서를 보존하기 때문에 
for iter in y:
    print(iter)
    # 1, 9 ,2 순서대로 나오게 된다.
# 원소를 순서대로 출력하기 때문에
# 리스트건 튜플이건 같은 역할을 한다.