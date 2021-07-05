# 비밀번호 메일 발송
# 비밀번호
print('회원정보를 입력해주세요')
email = input('이메일을 입력해주세요.')
name = input('이름을 입력해주세요.')
userid = input('아이디를 입력해주세요.')
passwd = input('비밀번호를 입력해주세요.')
print('------------------------------------------')
print('To.' + email)
print('▶ 아이디 및 비밀번호 확인')
print(' '+ name +' 고객님 안녕하세요.')
print(' '+ name +' 고객님의 아이디와 비밀번호는 아래와 같습니다.')
print(' 아이디 : '+ userid)
print(' 비밀번호 : '+ passwd)
# print 추력시 변수와 문자열 사이에 , 사용 : 공백이 하나 더 추가
print('------------------------------------------')
print('To.' , email)
print('▶ 아이디 및 비밀번호 확인')
print(' ', name ,' 고객님 안녕하세요.')
print(' ', name ,' 고객님의 아이디와 비밀번호는 아래와 같습니다.')
print(' 아이디 : ', userid)
print(' 비밀번호 : ', passwd)
# format함수를 사용 : 문자열 템플릿으로 출력 : python3에서 제공하는 기능
print('------------------------------------------')
print('To. {0}'.format(email))
print('▶ 아이디 및 비밀번호 확인')
print('  {0}고객님 안녕하세요.'.format(name))
print('  {0}고객님의 아이디와 비밀번호는 아래와 같습니다.'.format(name))
print(' 아이디 : {0}'.format(userid))
print(' 비밀번호 : {0}'.format(passwd))
# format문자열 사용 : python2에서 제공하는 기능
print('------------------------------------------')
print('To. %s' % email)
print('▶ 아이디 및 비밀번호 확인')
print('  %s고객님 안녕하세요.' % name)
print('  %s고객님의 아이디와 비밀번호는 아래와 같습니다.' % name)
print(' 아이디 : %s' % userid)
print(' 비밀번호 : %s' % passwd)
# print문 하나로 출력
print('------------------------------------------')
print('To.' + email +'\n '+
        '▶ 아이디 및 비밀번호 확인\n'+
        ' '+ name +' 고객님 안녕하세요.\n'+
        ' '+ name +' 고객님의 아이디와 비밀번호는 아래와 같습니다.\n'+
        ' 아이디 : '+ userid + '\n'+
        ' 비밀번호 : '+ passwd + '\n'
      )

print(f'To. {email}')
print(f'▶ 아이디 및 비밀번호 확인')
print(f'  {name}고객님 안녕하세요.')
print(f'  {name}고객님의 아이디와 비밀번호는 아래와 같습니다.')
print(f' 아이디 : {userid}')
print(f' 비밀번호 : {passwd}')