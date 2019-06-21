# Two Iteration Variables! (두 개의 반복 변수!)

# we loop through the key-value pairs in a dictionary using *two" iteration variables
# * 두 개의 반복 변수를 사용하여 사전에서 키 - 값 쌍을 반복합니다.
# Each iteration, the first variable is the key and the second variable is the corresponding value for the key
# 각 반복에서 첫 번째 변수는 키이고 두 번째 변수는 키에 해당하는 값입니다.

jjj = {'chuck':1, 'fred':42, 'jan':100}

for aaa, bbb in jjj.items():
    # items Method가 준 리스트의 모든 원소들은 키와 값 쌍으로 되어있으므로
    # 두개의 반복 변수를 사용하였다.
    # 두 반복 변수(aaa,bbb)는 값을 받는 일을 진행한다.
    # 각각 키와 값을 받는다
    # 키와 값이 동시에 지나가는 것과 같다.
    print(aaa, bbb)
    # 키와 값의 쌍을 출력 한다.

# items() Method : 키와 값의 쌍으로된 리스트를 반환
# 반복 변수 2개와 items()은 서로 연관되어 있다.
