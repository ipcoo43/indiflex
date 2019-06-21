# wild-card Characters

# ^X.*:
# ^ : Match the start of the line ( 한줄의 시작을 뜻하고 ) 
# X : 그냥 X이고
# .(dot) : Match any character ( 임의의 아무 문자와도 매칭되는 와일드 카드 이다 )
# *(asterisk) : Many times

# 정규식 중 몇 가지 문자는 앞에 나오는 문자에 영향을 주는데
# ^X.*: 은 X로 시작하고 뒤에는 아무 문자나 몇 번와도 상관 없다
# :으로 끝나는 문자열이라는 뜻이다.

# 확장되는 도장같다.
# X가 맨 앞에 있고
# 문자 몇 개 더 오고
# 그 다음 :이 나온다
# X나오고 아무 문자나 나오고 :가 나온다
# X-sieve: CMU Sieve 2.3
# X 아무 문자 :
# X-DSPAM-Result : Innocent