# ex) 할인된 상품 가격표
print('-'*30)
print('-- 한빛마트 오늘의 할인 가격표 출력 시스템 --')
print('-'*30)
discount = int(input('오늘의 할인율을 입력하세요. '))
item = {'쌀 ':9900,'상추':1900,'고추':2900,'마늘':8900,'통닭':5600,'햄 ':6900,'치즈':3900}

for i in item:
    print(f'{i}  : {item[i]} 원 {discount}%DC -> {item[i] - item[i]*discount*0.01 : .0f}원' )


def product():
    product = {'쌀':9900,'상추':1900,'고추':2900,'마늘':8900,'통닭':5600,'햄':6900,'치즈':3900}
    return product

def computeDiscount(dp):
    p = product()

    for k, v in p.items():
        price = v - v * dp/100
        print(f'{k}\t : {v:,d}원\t {dp}%DC ->{price:,.1f}원')

header = '-' * 30
header += '\n-- 한빛마트 오늘의 할인 가격표 출력 시스템 --\n'
header += '-' * 30

print(header)
dp = float(input('오늘의 할인율을 입력하세요 '))

computeDiscount(dp)