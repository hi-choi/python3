# ex) 버스 전용차로 단속 프로그램
print('1. 월~금, 2.토요일, 3.공휴일')
day=int(input('요일을 선택하세요.'))
if day == 1 :
    print('버스 전용차로 단속 중이니다.\n 1.버스, 2.승용차')
    kind = int(input('차종을 선택하세요'))
    if kind == 1 : print('버스입니다.')
    else :  print('버스 전용차로 위반입니다.')
else : print('토요일 및 공휴일은 단속하지 않습니다.')

# ex) 마스크 구매가능 요일 출력
year = int(input('출생 연도 끝자리 입력 : '))
age = int(input('만 나이 입력:'))
if age <65 :
    if year == 1 or year == 6 : print('월요일 구매 가능합니다.')
    elif year == 2 or year == 7 : print('화요일 구매 가능합니다.')
    elif year == 3 or year == 8 : print('수요일 구매 가능합니다.')
    elif year == 4 or year == 9 : print('목요일 구매 가능합니다.')
    else: print('금요일 구매 가능합니다.')
else :
    print('언제든지 구매 가능합니다.')

# ex) 차량 2부제
from _datetime import datetime as dt
car = int(input('차량 번호 4자리를 입력하세요'))
day = dt.now()

if day.day % 2 == 0:
    print('오늘 입차 : 번호가 짝수인 차량')
    if car % 2 == 0:
        print('귀하의 차량은 입차 가능합니다.')
    else:
        print('귀하의 차량은 입차 불가능합니다.')
else :
    print('오늘 입차 : 번호가 홀수인 차량')
    if car % 2 == 0:
        print('귀하의 차량은 입차 불가능합니다.')
    else:
        print('귀하의 차량은 입차 가능합니다.')

