
# ex) 369게임
for i in range (1, 100):
    if(i//10 == 9 or i//10 == 6 or i//10 == 3) :   # 십의 자리가 3, 6, 9일 경우
        print(f'{i} 짝',end='')
        if(i%10==3 or i%10==6 or i%10==9):  # 일의 자리가 3, 6, 9일 경우
            print('짝',end='')
    else:                                           # 십의 자리가 3, 6, 9 이외일 경우
        if(i%10==3 or i%10==6 or i%10==9): # 일의 자리가 3, 6, 9일 경우
            print(f'{i}짝', end='')
        else:
            print(i, end='')
    print(' ')

# 미국판 369 게임 - buzz
# https://www.wikihow.com/Play-Buzz