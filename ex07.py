# ex - 사용자로부터 숫자(1 - 9)를 하나 입력 받아,
# 구구단을 출력하는 프로그램을 작성해보세요
gugudan = int(input('숫자(1-9)를 입력해주세요.'))
for i in range(1,10):
      print(f'{gugudan}*{i}={gugudan*i}')


# ex - 키보드로 정수를 하나 입력받아 그 값이 정수, 음수, 0인지 구분하는
# 프로그램을 작성하시오. 각각의 경우에 따라 “정수입니다”, “음수입니다”,
# “0입니다”라고 출력하도록 한다.
import operator as op
num = int(input('정수를 입력해주세요.'))
result = '정수입니다.' if op.gt(num,0) else '0입니다.' if op.eq(num,0) else '음수입니다.'
print(result)

# ex - 지금 현재 수지의 통장잔액이 25,000원이다. 은행이자가 연 6%라
# 가정할 때, 몇 년이 지나야 통장잔액이 지금의 2배를 넘는지 알아보는
# 프로그램을 작성하세요

x= 0
sum = 0
while sum <= 50000:
      sum = 25000 * (1+0.06) ** x
      x=x+1

print(f'{x}년 후')