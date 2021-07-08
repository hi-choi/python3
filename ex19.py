# 계산기
def compute(num1, num2, op) :

    if op == '1' :
        result = num1+num2
        print(f'덧셈 결과 : {result:.1f}')
    elif op == '2' :
        result = num1-num2
        print(f'뺄셈 결과 : {result:.1f}')
    elif op == '3' :
        result = num1*num2
        print(f'곱셈 결과 : {result:.1f}')
    elif op == '4' :
        result = num1/num2
        print(f'나눗셈 결과 : {result:.1f}')
    else:
        print(f'연산자를 잘못입력하셨습니다.')

def computer():
    num1 = int(input('첫번째 숫자를 입력하세요.'))
    op = input('연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈')
    num2 = int(input('두번째 숫자를 입력하세요.'))
    compute(num1,num2,op)

computer()