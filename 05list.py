# 파이썬 리스트
attendList = ['A','B','C','D','E']
print(attendList)

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)

complex = [1,2.0,3.14,40,'5',"6"]
print(complex)

for data in numbers: #iterable
    print(data)
for data in complex: #iterable
    print(data)

len(numbers)
len(complex)

msg = 'Hello, World!!'
print(len(msg))

msg = input('메시지를 입력하세요')
print(f'입력한 문자열의 길이 : {len(msg)}')

print(len(['Hello, Python!!']))
print(len('Hello, Python!!'))

# 리스트의 모든 항목 조회
print(complex[0])
print(complex[1])
print(complex[2])
print(complex[3])
print(complex[4])
print(complex[5])

for i in range(len(complex)):
    print(complex[i])

for item in complex:
    print(item)

for idx, item in enumerate(complex):
    print(f'{idx},{item}')

sports = ['baseball','basketball','tennis','golf','soccer']
print(sports.index('soccer'))
print(sports[len(sports)-1])

lang = ['c/c++','c#','python','java']
lang.index('python')


# append : 끝에 추가
hobby = ['독서','등산','요리']
hobby.append('배구')
print(hobby)

# insert : 지정한 위치에 추가
number = [1,2,3,4,5,7,8,9]
number.append(10)
number.insert(5,6)
number.index(5,6)
print(number)

#
weather = ['The','weather','very']
weather.insert(2, 'is')
weather.insert(4,'cold')
print(weather)

# 성적처리 프로그램
# 3명 버전
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []

for i in range (1,4):
    name = input('이름은? ')
    names.append(name)
    kor = int(input('국어점수는? '))
    kors.append(kor)
    eng = int(input('영어점수는? '))
    engs.append(eng)
    mat = int(input('수학점수는? '))
    mats.append(mat)
    tot = kor+eng+mat
    tots.append(tot)
    avg = tot/3
    avgs.append(avg)
    if avg//10 >= 9 : grd = '수'
    elif avg//10 == 8 : grd = '우'
    elif avg//10 == 7 : grd = '미'
    elif avg//10 == 6 : grd = '양'
    else : grd = '가'
    grds.append(grd)

for i in range (3):
    print(f'이름 : {names[i]}, 국어 : {kors[i]}, 영어 : {engs[i]}, 수학 : {mats[i]}')
    print(f'총점 : {tots[i]}, 평균 : {avgs[i]}, 학점 {grds[i]}')

# 리스트 수정
hobby
hobby[1] = '여행'
hobby

# 리스트 삭제
# pop : 맨 뒤의 항목을 제거
hobby
hobby.pop()

sports
sports.pop(2)

# remove : 항목값으로 제거
lang
lang.remove('java')

# 야채 삭제
fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
fruits.remove('당근')
fruits.remove('토마토')
fruits

# 공인중개사
score = [55,35,40,70,65,30]
count = 0
sum = 0
for i in score:
    if i < 40 : count += 1
    sum += i

avg = sum/6

print(f'40점 미만 과목수 : {count}')
print(f'평균 점수 : {avg:.2f}')
if count == 0 and avg >= 60 :
    print('합격입니다.')
else:
    print('아쉽습니다. 불합격입니다.')

# 정렬하기
numbers = [5,1,3,4,2,6]
numbers.sort(reverse=True)
numbers
numbers.sort(reverse=False)
numbers

# 모의고사
jumsu = [90,100,88,85,95,82,70,75,100,92,78,80,75,95,90,100,84]
jumsu.sort(reverse=True)
jumsu

# 문자 정렬(한글)
names = ['김길동', '박길동','이길동','정길동','홍길동']
names.sort(reverse=True)
names
names.sort(reverse=False)
names
# 문자 정렬(영여)
units = ['scv','marine','firebat','ghost','dropship','battlecruiser','valkyrie']
units.sort(reverse=True)
units
units.sort(reverse=False)
units

# 리스트 슬라이싱
alphabet = ['a','b','c','d','e','f','g','h','i','j']
alphabet.reverse()
alphabet
alphabet[2:5] # 2~4
alphabet[0:4] # 0~3
alphabet[3:8] # 3~7
alphabet[5:]  # 5~끝
alphabet[3:9] # 3~8
alphabet[6:] # 6~끝
alphabet[-4:] # 오른쪽을 기준으로 왼쪽으로 4번째 요소에서 시작

#  a  b  c  d  e
#  1  2  3  4  5
# -5 -4 -3 -2 -1

# a, b, c, d 추출
alphabet[0:4]
alphabet[:4]
alphabet[:-6]

# d,c,b,a 추출
alphabet[3::-1]
alphabet[-7::-1]
alphabet[-7:-11:-1]


# g,h,e,d 추출
alphabet[:]




