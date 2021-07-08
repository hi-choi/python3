# 다국어 인삿말
def greet(nation) :
    if nation == '1' : print('안녕')
    elif nation == '2' : print('Hello')
    elif nation == '3' : print('こんにちは')
nation = input('where are you from? 1.한국, 2.USA, 3.Japan')
greet(nation)
