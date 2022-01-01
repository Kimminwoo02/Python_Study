"""
파일 출력!

"""

'''
1. 텍스트 파일 생성하기!

내용이 없는 텍스트 파일이 아닌
내용이 있는 텍스트 파일을 생성해보자!

[파일 내용]
안녕하세요
반갑습니다.

'''
file = open('hello.py','wt')

file.write('안녕하세요.\n')
file.write('반갑습니다.\n')

print('hello.py 파일이 생성되었습니다!')

file.close()

'''
정상적으로 실행되면 hello.py파일이 생성되었습니다. 가 출력되고,
hello.py파일이 생성됩니다

** 화면에 출력할 때는 print() 함수를 이용
파일에 내용을 출력할 때는 write() 메소드를 사용합니다!

**write() 메소드는 자동 줄 바꿈 처리를 하지 않습니다!
'''

'''
2. 텍스트 파일에 내용 추가!

이미 만든 hello.py 새로운 내용을 추가한다!

기본적으로 wt를 사용하면 덮어쓰기가 되기 때문에 
원하는 내용을 추가하고 싶다면 a모드를 사용해야 한다!
'''
'''
file = open('hello.py','at')

file.write('hello\n')
file.write('Nice to meet you \n')

print('hello.py 파일에 새로운 내용이 추가되었습니다!')
file.close()
'''

'''
오늘의 스케줄을 입력하면 그 내용을 파일에 보관하는 프로그램입니다.
스케줄을 입력하지 않고 enter을 누르면 프로그램이 종료됩니다

[조건]
생성되는 파일이름 :현재 날짜
확장자 txt

예시
2021-07-25
오늘 스케줄 입력하세요>>> 커피 마시기
오늘 스케줄 입력하세요>>> 밥먹기
오늘 스케줄 입력하세요>>> 놀기


'''

# from time import strftime
#
# file = open(strftime('%Y-%m-%d')+'.txt','wt')
# while True:
#     schedule = input('오늘 스케줄을 입력하세요!:')
#
#     if not schedule:
#         break
#     file.write(schedule +'\n' )
#
# file.close()

'''
문제) 코인을 던저서 50%의 확률로 당첨, 꽝이 나오고
이 결과를 answer.txt 파일을 저장되게 하세요.

[조건]
파일명:answer
확장자: txt

[출력]
코인의 결과가 answer에 파일에 저장되었습니다
 
[내부]
꽝 or 당첨
'''

from random import random

with open('answer.txt','wt') as file:

    if random() < 0.5:
        file.write('당첨')
    else:
        file.write('꽝!')
file.close()