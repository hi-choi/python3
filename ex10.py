# ex) 전기 요금 계산기
qty = int(input('전기 사용량을 입력하세요.'))
if (qty<=200) :
    price = 99.3
    base_rate = 910
elif (qty<=400):
    price = 187.9
    base_rate = 1600
else:
    price = 280.6
    base_rate = 7300

print(f'사용량 : {qty:.1f} kwh')
print(f'기본요금 : {base_rate}원')
print(f'단가 : {price}원')
print(f'전기요금 : {base_rate + qty*price}원')