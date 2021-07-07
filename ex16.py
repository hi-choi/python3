# ex) 수학문제
# 리스트 버전
quiz = ['3+2 ?','5÷2의 몫?','10²×2?',' 1-(10÷4의 나머지)?',' 2⁴?','4÷2?']
answer = []
point = []
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