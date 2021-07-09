# 파일 다루기


# 입력한 성적데이터를 파일에 저장
fname = 'D:/test/sungjuk.txt'

name = input('이름은?')
kor = int(input('국어는?'))
eng = int(input('영어는?'))
mat = int(input('수학은?'))

f = open(fname,'w')
#data = 'Hello, World!!'
data = f'{name} {kor} {eng} {mat}' # 파일에 기록할 내용을 문자열로 작성
f.write(data)
f.close()

# 기록한 성적데이터를 파일로부터 읽어오기
f = open(fname, 'r')
data = f.read()
print(data)
f.close()


def saveMemo(memo):
    fname = 'D:/test/myMemo.txt'
    f = open(fname, 'a') # 추가append 모드로 파일 초기화
    f.write(memo+"\n")
    f.close()

def memoMain():
    memo = input('메모를 입력하세요.')
    saveMemo(memo)

memoMain()

# py3방식으로 파일 다루기
# 기존 파일입출력 코드에서 불편한 점은
# 파일작업후에는 반드시 close를 해야한다는 것
# with문을 사용하면 명시적으로 close를 사용하지 않아도 된다.
with open(fname, 'w') as f:
    f.write('blablabla~')

# 파일에서 데이터 읽어오기
fname = 'D:/test/employees.csv'
with open(fname) as f:
    data = f.read()    # 모든 데이터를 한번에 다 읽어옴
    print(data)

with open(fname) as f:
    data = f.readline()  # 데이터를 한줄 읽어옴
    print(data)

with open(fname) as f:
    data = f.readlines()  # 모든 데이터를 라인단위로 읽어옴
    print(data)           # 읽어온 결과는 list형식


# employees.csv 에서 사번, 이름, 입상일, 급여를 출력하세요
with open(fname) as f:
    f.readline() # 첫줄은 읽기만함, 처리X
    while True:
        line = f.readline()
        if not line: break # 읽을 데이터가 없는 경우 작업 중단
        data = line.split(',') # 문자열을 ,로 분리해서 리스트로 저장

        empno = data[0]
        name = data[1]
        hdate = data[5]
        sal = int(data[7])

        emp = f'{empno} {name} {hdate} {sal:,}'
        print(emp)

# 타이타닉 데이터셋을 이용해서
# 승객이름name, 성별sex, 나이age, 승선위치embarked, 사망여부survivied 등을
# 추출해서 출력하세요
# 단, survived가 0이면 '사망', 1이면 '생존'이라 출력함
# embarked가 S이면 'southampthon', C이면 'cherbourg'이라
# Q라면 'queenstown'이라 출력함

fname = 'D:/test/titanic3b.csv'
with open(fname) as f:
    f.readline() # 첫줄은 읽기만함, 처리X
    while True:
        row = f.readline()
        if not row: break;
        data = row.split(',')
        #name = data[2]
        sex = data[2]
        age = data[5]
        pos = data[9]
        live = data[1]

        if pos == 'S' : pos = 'southampton'
        elif pos == 'Q' : pos = 'queenstown'
        elif pos == 'C' : pos = 'cherbourg'

        if live == '0': live = '사망'
        elif live =='1' : live ='생존'

        if age == '': age ='0'
        result = f'{sex} {age} {pos} {live}'
        print(result)

        # line = f.readline()
        # if not line: break # 읽을 데이터가 없는 경우 작업 중단
        # data = line.split(',') # 문자열을 ,로 분리해서 리스트로 저장
        #
        # name = data[2]
        # sex = data[3]
        # age = data[4]
        # embarked = data[11]
        #
        # if int(data[1]) == 0 : survived = '사망'
        # else : survived = '생존'
        #
        # emp = f'{name} {sex} {age} {embarked} {survived}'
        # print(emp)
        #
        #
