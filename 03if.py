# if문
num = int(input('숫자를 하나 입력하세요'))
if (num >10):
    print('num은 10보다 크다')

# ex) 속도위반 경고하기
speed = int(input('제한 속도를 입력하세요'))
if (speed > 50) :
    print('속도 위반입니다.')
    print('주의하세요~')

# 합격/불합격 출력 : if ~ else
score = int(input('점수를 입력하세요'))

if (score >= 80):
    print('합격입니다')
else :
    print('아쉽습니다. 다시 도전해주세요.')

# 실행문이 아직 정해지지 않은 경우 pass 키워드로 대체 작성 가능
# if (score >= 80):
#     pass
# else :
#     pass

# ex) 자동 온도 조절 장치 만들기
temp = int(input('기계 온도를 입력하세요.'))
if (temp>=40):
    print('팬(Fan) 가동')
else :
    print('팬(Fan) 중지')

# 입력받은 정수를 3으로 나눠 소수점 첫째자리가 0.5이상인 경우
# 반올림해서 출력하고 그렇지 않은 경우 그대로 출력하는 프로그램
num = int(input('정수를 하나 입력하세요.'))

result = num/3

if (result - int(result) >=0.5):
    result = int(result)+1 #소수이하자리 버린후 올림
else:
    result = int(result)  # 소수이하자리 버림

print(f'결과 : {result}')

# ex
mileage = int(input('보유한 마일리지를 입력해주세요.'))
if mileage >=1000:
    print('마일리지 사용가능')
else:
    print('마일리지 사용불가')
    
# 성적처리
jumsu = int(input('점수를 입력하세요 '))

if 60 <= jumsu <70:
    print('양')
elif 70 <= jumsu < 80:
    print('미')
elif 80 <= jumsu < 90:
    print('우')
elif 90 <= jumsu < 100:
    print('수')
else:
    print('가')

# ex) 자동 주문 시스템
print('Good morning. Nice to meet you.\n Where are you from?\n Please select a number\n')
print('1. 대한민국 2. USA 3. 中國')
num = int(input())
if num == 1 : print('주문하시겠어요?')
elif num == 2 : print('Would you like to order?')
elif num == 3 : print('您要訂購嗎？')
else : print('Would you like to order?')

# ex) 국가재난지원금
count = int(input('인원수를 입력하세요'))
if count == 1 : money = 400_000
elif count == 2 : money = 600_000
elif count == 3 : money = 800_000
else : money = 1_000_000
print(f'{money:,.1f}원 지원')

# ex) BMI
bmi = int(input('BMI 지수를 입력하세요'))
if bmi >30 : print('고도 비만')
elif bmi >25 : print('비만')
elif bmi >23 : print('과체중')
elif bmi >18.5 : print('정상체중')
else : print('저체중')

