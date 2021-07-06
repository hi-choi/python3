# 반복문
# 1~10까지 정수 출력
for i in range(1, 10+1):
    print(i)

# 2~10 사이 짝수 출력
for i in range(2,10+1,2):
    print(i)

# 메일 발송
num = int(input('메일 발송 횟수를 입력하세요.'))
for i in range(1,num+1):
    print('메일 발송')

# 3의 배수
for i in range(1,10+1):
    if i % 3 == 0 :
        print('3의 배수!')
    else:
        print(f'num={i}')

# 구구단
dan = int(input('몇번째 단을 출력하시겠습니까?(1-9'))
for i in range(1,10):
    print(f'{dan}*{i}={dan*i}')

# 2~10 사이 짝수 출력
for i in range(2,10+1,2):
    print(i , end=' ')

# 1~10 합
sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)

# ex1
for i in range(1,6,1):
    print('Hello, World!')

for i in range(1,101,1):
    if(i % 3 == 0 and i % 7 == 0) : print(i, end=' ')

min = 100
print('3과 7의 공배수', end=' ')
for i in range(100,1,-1):
    if(i % 3 == 0 and i % 7 == 0) :
        if min >= i: min = i
        print(i, end=',')
print(f'\n최소공배수{min}')

for i in range(-10, 1, 1) :
    print(i, end=',')

# 1 ~ 10까지 출력
for i in range(10):
    print(i+1)

# 반복문에 range 대신 문자열 사용
for ch in 'Hello':
    print(ch, end=',')

# ex) 50보다 작은 7의 배수
for num in range (7,50,7):
    print(num ,end=',')

# 1~10 까지 출력
num = 1
while num < 10+1:
    print(num)
    num += 1

# ex) 1~30 까지 정수 중 홀수, 짝수 구분
num =1
while num <= 30:
    if num%2 == 0:
        print(f'짝수:{num}')
    else:
        print(f'홀수:{num}')
    num=num+1

# ex) 구구단 3단
i= 1
dan =3
while i < 9+1:
    print(f'{dan}*{i}={dan*i}')
    i +=1

# ex) 0~100 정수 중 3과 8의 공배수와 최소공배수
num = 1
min = 999
while num < 100+1:
    if num % 3 == 0 and num % 8 == 0:
        print(f'공배수 : {num}')
        if min > num : min = num
    num += 1
print(f'최소공배수 : {min}')

# 게임 진행과 종료
flag = True
while flag:
    code = int(input('1:진행, 2:종료 '))
    if code == 1: print('게임 진행')
    else:
        flag = False
        print('게임 종료')

# 1~50까지 정수 중 3의 배수 더하기
sum = 0
for i in range(1,50+1):
    if i % 3 != 0: continue
    sum += i
print(sum)

# 정수를 1부터 차례대로 더하는 과정에서
# 정수의 합이 500이 넘었을 때는 언제인지 구하시오.
sum = 0
for i in range(1,100+1):
    sum += i
    if sum >= 500:
        print(i)
        break
print(sum, i)

# for-else
# for문의 업무를 끝낸 후 완료 메시지 출력
# 1~10까지 정수의 총합을 구하고
# 반복이 끝나는 경우 완료 메세지 출력
sum = 0
for i in range(10):
    sum+=(i+1)
else:
    print(f'총합 계산 끝! : {sum}')


# ex) 삼각형 넓이 구하기
width = 2
height = 3
while(True):
    area = width*height/2
    if (area > 150):
        break;
    print(f'삼각형의 넓이 : {area:.1f}')
    width += 2
    height += 3

# ex) 1~100 중 5,7의 배수를 제외한 값 구하기
for i in range(1,101):
    if i%5 == 0 : continue
    elif i%7 == 0 : continue
    else :
        print(f'{i}', end=' ')

# ex)
num = 0
while True:
    if (num >30) : break;
    print(num)
    num += 1


# 중첩 반복문
# 구구단 출력
for j in range (1,10):
    for i in range (1, 10):
        print(f'{j:2d} x {i:2d} = {i * j:2d} \t', end='')
    print()
print()





