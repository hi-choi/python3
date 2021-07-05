import keyword

myName = 'Karla'
myMajor = '컴퓨터'

print(myName)
print(myMajor)

myName = 100
myName = True
myName = False
myName = 3.141519

# 예제
intro = 'Hello'
print(intro)
intro='안녕하세요.'
print(intro)

nickname = 'Ms.Song'
print(nickname)

print(keyword.kwlist)
#print(keyword.softkwlist)  # v3.9 추가

myName = 'song'

#java와 달리 저장할 수 있는 숫자 크기의 제약이 적음
bigint = 12345678901234567890123456789012345678901234567890
print(bigint)

#실수 정의
bigfloat = 1.12345678901234567890
print(bigfloat)

#형변환
a=123
b='456'

a=a+1
#b=b+1 #에러

#type함수 - 변수에 저장된 데이터가 어떤 자료형인지 알기 위해 사용
print(type(123))
print(type('123'))
print(type(True))

#다중 선언
x = 1
y = 1
z = 1

x=y=z=10

#자릿수 구분
million1 = 1000000
million2 = 1_000_000
num = 1_2_3 #자릿수가 맞지 않으므로 123으로 인식됨

#논리값 확인 : bool
bool(True)
bool(1)
bool(100)
bool(-100)
bool(0)

#자료형 변환
str(123)

#값입력받기
#name= input('이름을 입력하세요 ')
#print(name)

# 성적처리 프로그램
# 이름, 국어, 영어, 수학을 입력받아 출력
name = input('이름을 입력하세요 ')
kor = input('국어점수를 입력하세요 ')
eng = input('수학점수를 입력하세요 ')
mat = input('영어점수를 입력하세요 ')
print('이름 :' + name)
print('국어 :' +kor)
print('영어 :' +eng)
print('수학 :' +mat)




