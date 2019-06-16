# 변수 Variables (문자열)
# Array of Character
# Array : 'abc'
# a,b,c는 다른 메모리를 잡고 있다
# 다른 공간의 메모리 모아 둔것
# 파이썬은 string,character 모두 str 이다,
# 파이썬은 Array가 없다
# S='abc' S[0],S[1],S[2] 각각 메모리를 갖고 S에 연결되어 있는 모임

'Hello'"World"
print('Hello'"world" )
print('Hello',"world" )
message = 'Hello World'
message[0:7]
message[:7]
message[:-7]
len(message)
message[7:len(message)]
message.split(' ')
x,y,z = 10,20,30
print(x,y,z)
first, second = message.split(' ')
first + '' + second
first * 3 + second
first < second
f'Your name is {"길동"}'
f'Num is {23:05d}'