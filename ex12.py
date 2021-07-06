# ex) 열차 교차 시간
# 방법 1
for i in range(1,541):
    if(i%30 == 0) :
        print(f'{9 + (i // 60)}시 {i % 60}분')
    elif(i%50 == 0) :
        print(f'{9 + (i // 60)}시 {i % 60}분')


# 방법 2
train1 = 10
train2 = 25
train3 = 30

for i in range(1, 540+1):
    hour = (i // 60) + 9
    min = i % 60

    if i % train1 == 0 and i % train2 == 0:
        print(f'A열차와 B열차 충돌! {hour}시 {min}분')
    elif i % train2 == 0 and i % train3 == 0:
        print(f'B열차와 C열차 충돌! {hour}시 {min}분')
    elif i % train3 == 0 and i % train1 == 0:
        print(f'C열차와 A열차 충돌! {hour}시 {min}분')
