# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드집합체
# 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# 어떤 입력값을 주면 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 다른 사람과의 협업시 코드가 섞이지 않게
# 하기 위한 목적도 있음 - 모듈

def startSensor() :
    print('온도센서 작동을 시작합니다.')
    

def stopSensor() : 
    print('온도센서 작동을 중지합니다.')

startSensor()
stopSensor()

# 인치 <-> cm
def convertCM2Inch(cm) :
    inch = cm * 0.393701
    print(f'{cm:.1f}cm = {inch:.4f} inch')

num = input('길이를 입력하세요.(cm)')
convertCM2Inch(float(num))

# 이동거리
def computeDistance(time,speed) :
    distance = time * speed
    print(f'이동 거리는 {distance:.1f}km 입니다.')

time = float(input('이동 시간을 입력하세요.'))
speed = float(input('이동 거리를 입력하세요.'))
computeDistance(time,speed)


# 전역global변수와 지역local변수
num = 10 # 10

print('전역변수 num', num)
def local():
    num = 20  # 20
    print('함수내 num', num)

local()

print('전역변수 num',num)  # 10

# 함수내에서 전역변수 사용하기 : global
num = 10 # 10
print('전역변수 num',num)

def local():
    #global num # 함수내에서 전역변수를 수정할 수 있도록 함
    num = 20 # 20
    print('함수내 num',num)
print('전역변수 num',num) # 10(x) -> 20


# 웹사이트 방문 누적하기
count = 0

def countVisitor():   # 함수정의
    global count
    # global count = 0 # 전역변수는 초기화 불가

    while True:
        menu=input('1.웹사이트 방문 2.종료\n'
              '작업을 선택하세요 ')
        if menu == '1':
            count +=1
            print(f'총 방문횟수 : {count}')
        elif menu == '2':
            break;

print(f'총 방문횟수 : {count}')
countVisitor()


x = 10
y = 10
def add():
    print(x+y)

def add(x,y):
    print(x+y)

add()
add(10,10)

# 함수의 매개변수를 동적으로 정의
# 매개변수명 앞에 *로 정의해서 함수를 만들면 됨

# ex) 기존에 만든 add 함수는 2개의 매개변수만 받음
# 2개이상의 매개변수를 받아 결과를 출력하고 싶다면?
def add(x,y,z):
    print(x+y+z)

def add2(*num):
    sum = 0
    for v in num:
        sum += v
    print(sum)

add2(10,10)
add2(10,10,10,10,10)

# ex) 문자메세지(MMS/SMS 구분하기)
def computeMS(msg):
    msgSize = len(msg)
    print(f'입력하신 문자열 길이는 {msgSize}')
    if msgSize <= 100:
        print('단문메세지로 50원이 부과됩니다.')
    elif msgSize > 100:
        print('장문메세지로 100원이 부과됩니다.')

msg = input('문자열을 입력하세요. ')
computeMS(msg)

# 함수정의시 매개변수를 선언했지만
# 함수호출시 인수를 순서대로 입력하지 않을 경우
# => 인수값 앞에 매개변수명을 지정

def computeSungJuk(name, kor, eng, mat):
    tot = kor + eng + mat
    avg = tot / 3
    print(tot,avg)

computeSungJuk('혜교',98,78,65)
#computeSungJuk(98,78,65,'수지') #오류발생!
#computeSungJuk(98,78,65,name='수지') #오류발생!

computeSungJuk(kor=98,eng=78,mat=65,name='수지')
computeSungJuk(name='수지',kor=98,eng=78,mat=65)


# 매개변수를 정의했지만
# 매개변수 없이 함수 호출하고 싶다면?
# -> 매개변수 선언시 초기값을 지정함

def add3(x=10,y=10):
    print(x+y)

add3(5,5)

add3()

# ex) 사칙연산 프로그램
def compute (x,y) :
    add = x+y
    min = x-y
    mul = x*y
    div = x/y
    return add, min, mul, div

num1 = int(input('정수를 입력하세요. '))
num2 = int(input('정수를 입력하세요. '))
p,m,c,d = compute(num1, num2)
print(f'사칙연산 결과 : ({p},{m},{c},{d:.2f})')

# ex) 팩토리얼
def fact(n):
    if n > 1 :
        return n * fact(n-1)
    else :
        return 1

num = int(input('0보다 큰 숫자를 입력하세요.'))
result = fact(num)
print(result)

