# 정수 + 정수 = 정수
num1 = 10
num2 = 20
num3 = num1 + num2
num3

# 실수 + 실수 = 실수
num1= 30.5
num2 = 50.5
num3 = num1+num2

# 정수 + 실수 = 실수
num1 = 10
num2 = 30.5
num3 = num1 + num2


# 예제1 - 1분기 매출 구하기
one = int(input('1월 매출을 입력해주세요.'))
two = int(input('2월 매출을 입력해주세요.'))
three = int(input('3월 매출을 입력해주세요.'))

print('1월 매출 : {0}'.format(one))
print('2월 매출 : {0}'.format(two))
print('3월 매출 : {0}'.format(three))
print('1분기 전체 매출 : {0} 원'.format(one+two+three))

num1 = 3.14
num2 = 0.25
num3 = num1 + num2
float(num3)
int(num3)

#ex2 - 1분기 수익 계산하기
sale = int(input('1분기 매출을 입력해주세요.'))
buy = int(input('1분기 매입을 입력해주세요.'))
print('1분기 매출 : {0}'.format(sale))
print('1분기 매입 : {0}'.format(buy))
print('수익 : {0} 원'.format(sale+buy))

#ex3 - 방 너비 구하기
width = int(input('방의 가로 크기를 입력해주세요.'))
height = int(input('방의 세로 크기를 입력해주세요.'))
print('가로 길이 : {0}'.format(width))
print('세로 길이 : {0}'.format(height))
print('방의 너비 :  {0}㎠'.format(width*height))

# 문자열 곱하기
str1 = 'Hello, World!!'
str1 *3

#ex4 - 신체질량지수(BMI 구하기)
# < 18.5 : 저체중
# < 23 : 정상
# < 25 : 과체중
# < 30 : 비만
# > 30 : 고도비만
weight = int(input('몸무게(kg)을 입력해주세요.'))
height = int(input('신장(m)을 입력해주세요.'))
height = height /100
bmi = weight / (height * height)
#print('몸무게(kg) : {0}'.format(weight))
#print('신장(m) : {0}'.format(height))
#print('BMI : {0}'.format(bmi))
print('BMI : {0:.2f}'.format(bmi))
print(f'BMI : {bmi:.2f}') # f-string : py 3.6부터 지원

# print 출력 속도 : .format > % > f-string

# ex5 - 홀짝 예제 (if문 x)
coins = int(input('동전 수를 입력해주세요.'))
isEven = coins % 2
print(f'동전의 홀짝여부 (0:짝) {isEven}')

# ex5 - 홀짝 예제 (if문 o)
coins = int(input('동전 수를 입력해주세요.'))
if coins%2 == 0 :
    print('0')
else :
    print('1')
    
# 나누기 연산 /와 //차이
10 /3 # 소수점 포함
10//3 # 소수점 제외 정수만

# ex6 - 빵 나누어 주기
bread = int(input('빵이 몇개 있는지 입력해주세요.'))
diver = int(input('나누어줄 빵의 갯수를 입력해주세요.'))

stud = bread // diver
divmod = bread % diver

print(f'{bread}개의 빵은 {diver}개 씩, {stud}명의 학생에 나눠줄 수 있고,')
print(f'{divmod}개의 빵이 남음')

# ex7 - 전염병 감염자 수 구하기
day = int(input('몇일 후의 감염자를 계산할지 입력하세요.'))
num = 2 ** day
print(f'{day}일 후 감염자 수는 {num}명 입니다.')

# ex8 - 복리 계산기
# 원금, 유치기간, 연이율을 입력받아 복리계신 후 총수령액 출력
# money = int(input(''))
# span = int(input('유치기간을 입력해주세요.'))
# rate = int(input('연이율을 입력해주세요.'))
money = 5_000_000
duration = 5
interest = 5.0

takes = money + (money * 0.05) #1년차
takes += (takes * 0.05) #2년차
takes += (takes * 0.05) #3년차
takes += (takes * 0.05) #4년차
takes += (takes * 0.05) #5년차

takes = money*((1+interest/100) ** duration)
takes
print(f'5년 후 총 수령액 : {takes}원')

# ex9 - 범버카 탑승 가능 여부
height = int(input('어린이의 신장을 입력해주세요.'))
isRide = height >= 120
print(f'탑승 가능여부 : {isRide} (True : 탑승가능)')

# ex10 - 범버카 탑승 가능 여부2
height = int(input('어린이의 신장을 입력해주세요.'))
isRide = height >=120 and height < 170
print(f'탑승 가능여부 : {isRide} (True : 탑승가능)')

# short circuit evaluation
num1 = 17
num2 = 20
(num1 < 15) and (num2 > 15) # False and True

num1 = 10
num2 = 20
(num1 < 15) or (num2 < 15) # True and False

#(num1 <5) and xyz  #py38만 지원

# 삼항 연산자
# 참일때 값 if 조건식 else 거짓일때값

num = 11
'짝수' if num % 2 == 0 else '홀수'

# ex11 - 적자/흑자 판단하기
inmoney = int(input('수입을 입력해주세요.'))
outmoney = int(input('지출을 입력해주세요.'))
result = '흑자' if inmoney >= outmoney else '적자'
print(f'수입 : {inmoney}')
print(f'지출 : {outmoney}')
print(result)

# ex12 - 윤년
year = int(input('년도를 입력해주세요.'))
isYun = '윤년입니다.' if year % 4 == 0 and year%100 != 0 or year % 400 == 0 else '윤년이 아닙니다.'
print(isYun)

# operator 모듈 사용하기
# 해당 모듈 사용시 대량의 데이터 처리 때 속도 향상이 존재함
import operator as op
op.add(10, 20)
op.sub(10, 20)
op.mul(10, 20)
op.floordiv(10, 3) # 정수 몫 : //
op.truediv(10, 3) # 실수 몫 : /
op.mod(10, 3)
op.pow(2, 30)

op.eq(10, 20)
op.ne(10, 20)
op.gt(10, 20)
op.lt(10, 20)
op.ge(10, 20)
op.le(10, 20)

x = op.eq(10, 20)
y = op.lt(10, 20)
op.and_(x, y)
op.or_(x, y)

# ex13 - 긴급재난지원금 대상자 선별
import operator as op
salary = int(input('월 소득을 입력하세요.'))
isAlready = int(input('다른 지원금을 받고 있습니까? 1번 받고 있다. 2번 받고 있지 않다.'))
x = op.le(salary, 4000000)
y = op.eq(isAlready, 2)
isYes = '수급 대상자' if op.and_(x, y) else '수급 대상자가 아닙니다.'
print(isYes)