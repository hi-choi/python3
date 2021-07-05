# ex) 생존율 구하기
time = int(input('최초 장비를 사용하기까지 걸린 시간(초)를 입력하세요.'))
if time <= 60 : print('생존율 : 85%')
elif time <= 120 : print('생존율 : 76%')
elif time <= 180 : print('생존율 : 66%')
elif time <= 240 : print('생존율 : 57%')
elif time <= 300 : print('생존율 : 47%')
else : print('생존율 : 25% 미만')

