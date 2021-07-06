# ex) 로그인
count = 1
while(True):
    passwd = input('관리자 암호를 입력하세요.')
    if(passwd == 'hanbitac'):
        print('로그인 됐습니다.')
        break;
    if(count ==5 ):
        print('로그인 실패!! 횟수 초과!!')
        break;
    print('암호를 다시 확인하세요!!')
    count +=1

for i in range(5):
    userid = input('아이디를  입력해주세요.')
    passwd = input('비밀번호를  입력해주세요.')

    if userid == 'abc123' and passwd == '987xyz':
        print('로그인 되었습니다.')
        break;
    else:
        print('암호를 다시 확인해주세요.')
else :
    print('로그인 실패! 횟수 초과!')


cnt = 1
while True:
    if cnt > 5:
        print('로그인 실패! 횟수 초과!')
        break

    userid = input('아이디를  입력해주세요.')
    passwd = input('비밀번호를  입력해주세요.')

    if userid == 'abc123' and passwd == '987xyz':
        print('로그인 되었습니다.')
        break
    else:
        print('암호를 다시 확인해주세요.')
    cnt +=1