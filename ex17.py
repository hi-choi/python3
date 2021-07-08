# ex) 회원가입
members = {}
flag = True

menu =  '='*30
menu += '   회원가입 프로그램   \n'
menu += '-'*30
menu += '\n 1. 회원가입   \n'
menu += ' 2. 프로그램 종료   \n'
menu += '-'*30

while flag :
    print(menu)
    choice = input('작업을 선택하세요 : ')

    if choice == '1':
        userid = input('아이디는?')
        passwd = input('비밀번호는?')
        members[userid] = passwd

    elif choice == '2':
        print('프로그램을 종료합니다.')
        print('가입한 회원들은 다음과 같습니다...')

        for u, p in members.items():
           print(f'{u}:{p}')

        flag = False



# ex)회원가입 2
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
