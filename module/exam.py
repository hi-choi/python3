#시험 통과 여부

def exampass(one,two,three):
    tot = one+two+three
    avg = tot/3
    isPass = '불합격'

    isAll60 = avg >= 60
    is40 = one < 40 or two <40 or three <40
    if isAll60 and not is40:
        isPass = '합격'

    # 파이썬에서는 함수의 리턴값으로 2개 이상 가능
    return tot, avg, isPass

    # if avg >= 60 and one >= 40 and two >= 40 and three >= 40 :
    #     isresult = 'Pass'
    # else :
    #     isresult = 'Fail'
    #
    # print(f'총점 : {tot}')
    # print(f'평균 : {avg}')
    # print(f'합격여부 : {isresult}')
