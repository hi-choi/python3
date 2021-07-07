# 딕션어리
ages = {'박찬호':48, '박지성':40, '박세리':50, '이승엽':43}
type(ages)

person = {'이름':'홍길동', '나이':25,'몸무게':88.8,
          '주소':'서울 종로구 삼일대로','취미':['운동','독서','영화감상']}

sungjuk = {'C/C++':'A','Java':'B+','네트워킹':'C', '보안':'A', '해킹':'F','시스템':'C+'}

# 홍길동의 나이와 취미 조회
person['나이']
person['취미']

# 홍길동의 혈액형 추가
# dict에 새로운 항목을 추가할때는
# 새로운키와 값으로 정의해야함
person['혈액형'] = 'A'
person

# dict에 기존 키와 값으로 구성한 항목을
# 추가하려하면 기존키에 저장된 값이 변경됨
person['혈액형'] = 'O'
person

# dict에서 항목 삭제 : pop
person.pop('몸무게')
person

dellist = ['나이','취미']
for key in dellist:
    person.pop(key)

person

# dict 모든 항목 출력
person = {'이름':'홍길동', '나이':25,'몸무게':88.8,
          '주소':'서울 종로구 삼일대로','취미':['운동','독서','영화감상']}

for key in person.keys():
    print(person[key])

# dict의 키와 값 모두 가져오기 : items
person.items()


# ex) 중간고사 성적 관리 프로그램
midsj = {'C/C++':'A','Java':'B+', '모바일' : 'C', '보안':'A+', '해킹':'F','시스템':'C+'}

# 조회
midsj['Java']
midsj['시스템']

# 삽입
midsj['파이썬'] = 'A'
midsj['OS'] = 'A+'

# 수정
midsj['Java'] = 'F'
midsj['시스템'] = 'A'

# 출력
for key in midsj:
    print(f'{key} : {midsj[key]}')

for k,v in midsj.items():
    print(f'{k} : {v}')

# 딕셔너리 for 축약문
# 이름과 성적 리스트를 dict 객체로 재생성하시오
name = ['혜교','지현','수지'] # 키
grd = ['수','양','미']  # 값
sj = {}

# 반복문을 사용하지 않음
sj[name[0]] = grd[0]
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]


# 반복문을 사용해서 코드를 줄임
for i in range(3):
    sj[name[i]] = grd[i]

# dict 컴프리헨션
# {키/값 표현식 for 키, 값 in zip(반복가능객체1, 반복가능객체2) }
sj2 = {key:val for key, val in zip(name, grd)}
print(zip(name,grd))

# zip: 여러개의 데이터를 하나로 합쳐서
# iterable한 객체로 생성해 줌 - 개별 객체는 튜플로 반환
for pair in zip(name, grd):
    print(pair)




# ex) 회원가입
member = {}
while(True):
    option = int(input('1. 회원가입, 2. 프로그램 종료'))
    if option == 1 :
        userid = input('아이디를 입력하세요 : ')
        passwd = input('비밀번호를 입력하세요 : ')
        member[userid] = passwd
    else :
        break

print('-'*30)
print('아이디 : 비밀번호')
print('-'*30)
for key in member:
    print(f'{key} : {member[key]}')
print('-'*30)

# ex) 로또
import random
comlotto = []
mylotto = []
samenumber = []
print('1부터 45가지의 정수 6개를 입력하세요.')
for i in range(6):
    comlotto.append(random.randrange(1,46))
    mylotto.append(int(input(f'Number{i+1} : ')))

print(f'이번주 로또 번호 {comlotto}')
print(f'내가 선택한 번호 {mylotto}')

count = 0
for i in range(len(comlotto)):
    for j in range(len(mylotto)):
        if comlotto[i] == mylotto[j] :
            count+=count
            samenumber.append(comlotto[i])

print(f'일치하는 숫자 {samenumber}')