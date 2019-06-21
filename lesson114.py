# Tuples are more efficient ( 튜플이 더 효율적입니다. )
# Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terrms of memory use and performance than lists.
# 파이썬은 튜플 구조를 수정할 필요가 없으므로 목록보다 메모리 사용 및 성능 측면에서 더 간단하고 효율적입니다.
# So in our program when we are making 'temporary variables' we prefer tuples over lists
# 그래서 우리 프로그램에서 '임시 변수'를 만들 때리스트보다 튜플을 선호합니다.


# 튜플은 제한이 있는 리스트이다.
# 그런데 외 튜플을 사용할까요?
# 더 효율적이기 때문이다.
# 튜플은 build 과정이 없다.
# 파이썬 내부에서 이미 알고 있다. 
# 튜플은 절대 변경되지 않는 다는 것을
# 왜냐하면 우리가 튜플을 만들 때 이미 바꿀 일이 없다고 공언을 했기 때문이다.
# 그러니 파이썬은 보다 효율적으로 메모리를 활용할 수 있다.
# 그리고 또 튜플을 사용하기 좋은 때가
# 임시로 사용하는 변수를 만들 때이다.
# 어차피 임시로 사용하고 버리는 변수이닌까
# 간단하고 깔끔하게 사용할 수 있다.

# 반대로 리스트 같은 경우에는 
# 보다 다양한 것들을 구축하는데 쓰인다.