# 로또 당첨 게임
import random as r

# def readLotto(): # 사용자에게 로또 입력받음
#     magic = []
#     for i in range(6):
#         val = input(f'1 ~ 45사이 정수 하나를 입력하세요 ({i+1}/6): ')
#         magic.append(int(val))
#
#     return magic
#
# def makeLotto(): # 컴퓨터가 로또 생성함
#     magic = []
#     for i in range(6):
#         magic.append(r.randint(1,45))
#     return magic

def Lotto654():
    magic = readLotto()
    lotto = makeLotto()
    wins = []
    for v in magic:
        if lotto.count(v) != 0 : wins.append(v)
    print(f'내 로또 번호 : {magic}')
    print(f'이번 로또 번호 : {lotto}')
    print(f'일치하는 숫자 : {wins}')


# 중복 제거한 값
def readLotto(): # 사용자에게 로또 입력받음
    magic = []
    i = 0
    while len(magic) < 6:
        val = int(input(f'1 ~ 45사이 정수 하나를 입력하세요 ({i+1}/6): '))
        if magic.count(val) == 0: # 입력한 정수가 magic 리스트에 존재하는지 검사
            magic.append(int(val))
            i+=1

    return magic

def makeLotto(): # 컴퓨터가 로또 생성함
    magic = []
    while len(magic) < 6:
        val = r.randint(1,45)
        if magic.count(val) == 0:
            magic.append(val)
    return magic
