# Fine-Tunning Your Match

# ^X.*:
# 가끔 보다 깔금하게 데이터를 다루고 싶을 때가 있다.

# X-Sieve: CMU sieve 2.3
# X-DSPAM-Result: Innocent
# X-Plane is behind schedule: two weeks

# 기본적으로 보면 ^X.*: 에 모두 매칭 된다.
# X가 몇개의 문자와: 이 있다. 모두 매칭된다.
# X다음에 :만 오면된다고 되어 있다.

# 어떤 건 매칭시키고 어떤 건 뺄지 정확하게 해보자

# ^X-\S+:
# ^X- 한 줄의 시작에서만 비교할 거고
# X- 가 있어야 매칭이된다
# X- 로 시작하는 줄이어야 한다.
# ^X- 는 첫 두 글자가 X- 여야 한다는 뜻이다.
# \S 는 공백이 아닌 문자라는 뜻이다.
# 공백 문자만 아니면 된다.
# +는 한 번 이상 나온다는 뜻이다.
# 띄어쓰기를 제외한 문자가 한 번 이상 나올 수 있다.
# 다시 뒤에는 :이 나와야 한다
# X-로 시작하고 공백이 아닌 문자가 한 개 이상 자유롭게 나온 뒤 :이 나와야 한다.
# X-로 시작해 하나 이상의 문자가 나오고 :이 나온다

# 전체 한 줄을 불러들여서 그 줄의 어느 한 부분이라도 정해진 양식을 만족하는지 판단

