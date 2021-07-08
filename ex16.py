# ex) 수학문제
# 리스트 - 방법 1
# quiz = ['3+2 ?','5÷2의 몫?','10²×2?',' 1-(10÷4의 나머지)?',' 2⁴?','4÷2?']
# answer = [5,2,8,200,-1,16,2]
# point = [3,5,3,5,5,3,3]
#
# asw = []
# cnt = len(quiz)
# for i in range(cnt):
#    print(f'문제 {quiz[i]}')
#    asw.append(input('정답을 입력하세요 '))
#
# good = 0
# jumsu = 0
# for i in range(cnt):
#    if int(asw[i]) == answer[i]:
#       good += 1
#       jumsu += point[i]
#
# print('-'*30)
# print(f'정답 갯수 : {good}\n'
#       f'오답 갯수 : {cnt-good}\n'
#       f'총 점수 : {jumsu}')
# print('-'*30)

# 리스트 - 방법 2
# quiz = ['3+2 ?','5÷2의 몫?','10²×2?',' 1-(10÷4의 나머지)?',' 2⁴?','4÷2?']
# answer = [5,2,8,200,-1,16,2]
# point = [3,5,3,5,5,3,3]
# good = 0
# jumsu = 0
#
# cnt = len(quiz)
# for i in range(cnt):
#    print(f'문제 {quiz[i]}')
#    asw = input('정답을 입력하세요 ')
#
#    if int(asw) == answer[i]:
#       good += 1
#       jumsu += point[i]
#
# print('-'*30)
# print(f'정답 갯수 : {good}\n'
#       f'오답 갯수 : {cnt-good}\n'
#       f'총 점수 : {jumsu}')
# print('-'*30)

# 리스트 - 방법3

quiz = [['3+2?',5,3],['5÷2의 몫?',2,5],['10²×2?',200,5],[' 1-(10÷4의 나머지)?',-1,5],['2⁴?',16,3],['4÷2?',2,3]]

cnt = len(quiz)
good = 0
jumsu = 0

for q in quiz:
   print(f'문제 {q[0]}')
   asw = input('정답을 입력하세요 ')

   if int(asw) == q[1]:
      good += 1
      jumsu += q[2]

print('-'*30)
print(f'정답 갯수 : {good}\n'
      f'오답 갯수 : {cnt-good}\n'
      f'총 점수 : {jumsu}')
print('-'*30)

# 튜플 버전
jungdap = ('5','2','8','200','-1','16','2')
count = 0
score = 0

print('문제 : 3+2')
answer = input('정답을 입력하세요')
if answer == jungdap[0] :
   count += 1
   score += 3

print('문제 : 5÷2의 몫')
answer = input('정답을 입력하세요')
if answer == jungdap[1] :
   count += 1
   score += 5

print('문제 : 10-2')
answer = input('정답을 입력하세요')
if answer == jungdap[2] :
   count += 1
   score += 3

print('문제 : 10²×2')
answer = input('정답을 입력하세요')
if answer == jungdap[3] :
   count += 1
   score += 5

print('문제 : 1-(10÷4의 나머지)')
answer = input('정답을 입력하세요')
if answer == jungdap[4] :
   count += 1
   score += 5

print('문제 : 2⁴')
answer = input('정답을 입력하세요')
if answer == jungdap[5] :
   count += 1
   score += 3

print('문제 : 4÷2')
answer = input('정답을 입력하세요')
if answer == jungdap[6] :
   count += 1
   score += 3

print('-'*30)
print(f'정답 개수:{count}')
print(f'오답 개수:{len(jungdap) - count}')
print(f'Total Score:{score}')
print('-'*30)