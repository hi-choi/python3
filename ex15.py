# 혈액 보관 시스템
# 방법1
a = []
b = []
ab = []
o = []

for i in range(10):
    blood = input('헌혈해 주셔서 감사합니다. \n'
                  '혈액형을 선택하세요.(A,B,AB,O)')
    if blood == 'A' or blood =='a':
        a.append(blood)
    elif blood == 'B' or blood == 'b':
        b.append(blood)
    elif blood == 'AB' or blood == 'ab':
        ab.append(blood)
    elif blood == 'O' or blood == 'o':
        o.append(blood)
print(f'혈액형 수급 현황\n'
      f'A형 : {len(a)}\n'
      f'B형 : {len(b)}\n'
      f'AB형 : {len(ab)}\n'
      f'O형 : {len(o)}')


# 방법2
bloods = []
for i in range(10):
    blood = input('헌혈해주셔서 감사합니다.\n'
                  '혈액형을 선택하세요 (A,B,AB,O')
    bloods.append(blood)
print('-'*30)
print('혈액형 수급 현황')
print('-'*30)
print(f'A형 : {bloods.count("A")}')
print(f'B형 : {bloods.count("B")}')
print(f'AB형 : {bloods.count("AB")}')
print(f'O형 : {bloods.count("O")}')
print('-'*30)

blood = []
for i in range(10):
    print('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요.')
    blood.append(input('A, B, AB, O'))

print('-----------------------------')
print('혈액형 : 개수')
print('-----------------------------')

a=b=o=ab=0
for i in blood:
    if i == 'A': a +=1
    elif i == 'B': b +=1
    elif i == 'AB': ab +=1
    elif i == 'O': o +=1
print(f'A형 : {a}')
print(f'B형 : {b}')
print(f'AB형 : {ab}')
print(f'O형 : {o}')
print('-----------------------------')