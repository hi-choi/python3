# ex - 근무시간에 필요한 컴퓨터 수량 파악
import operator as op
hour = int(input('근무시간을 입력하세요.'))
computer = 24//hour if op.eq(24 % hour, 0) else 24//hour + 1
print(f'필요한 컴퓨터 : {computer}')
