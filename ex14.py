# 출석부 관리
student = ['정우람','박으뜸','배힘찬','천영웅','신석기','배민규','전민수','박건우','박찬호','이승엽']

# 1 가나다순으로 정렬
student.sort(reverse=False) # 가나다순

# 2 학생 제거
student.remove('박찬호')

# 3 학생 출력
for i in student :
    print(i,end=' ')
else :
    print(f'\n전체 학생 수 : {len(student)}명')

# 4 학생 추가
student.append('이병규')
# 5 학생 순서 역순으로
student.reverse()

# 6 학생 이름 변경
student[2] = '정잘남'
student