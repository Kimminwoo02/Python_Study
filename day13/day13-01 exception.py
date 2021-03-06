"""
1. 사용자 예외 클래스
예외 처리의 마지막 단계로 예외 클래스를 직접 만들어서 사용해본다.

직접예외 클래스를 만드는 방법은 exception 클래스를 상속받은 클래스를
새로 만드는 것.
예외 메세지는 exception 클래스의 생성자인 __init() 메소드에 전달하면 됩니다.


[사용법]
1. 직접 예외 메세지 출력
class 예외 클래스(exception):
    def __init__(self):
        super.__init__('예외 메세지')

2. 인자로 넘겨받는 예외 메세지 출력
class 예외 클래스(exception):
    def __init__(self,message):
        super().__init__(message)
"""

#0~23 사이의 시간이 입력되는게 아닌 경우 에러를 발생
class HourError(Exception):

    def __init__(self):
        super().__init__('올바른 시간이 아닙니다.')

try:
    hour = int(input('시간을 입력하세요'))
    # 0 ~23 이 아닌경우
    #1 ~ 24 x ? 0 ~ 23 인가? : 0 ~ 23
    if hour < 0 or hour > 23:
        raise HourError
except HourError as e:
    print(e)

'''
책 예제 ) 입력받은 이름이 2~6자 사이가 아니면 NameError 예외를 발생시키고
이름은 2~6자 사이로 입력해주세요 라는 예외메시지 출력 프로그램 만들기

[출력]
--[틀린입력]
이름을 입력하세요 >>> 나 
이름은 2~6 자 사이로 입력해주세요
--[옳은 입력]
이름을 입력하세요 >>> 홍길동
입력된 이름은 홍길동 입니다.


'''
class NameError(Exception):

    def __init__(self,msg):
        super.__init__(msg)

try:
    name = input('이름을 입력하세요:')
    if len(name) < 2 or len(name) > 6:
        raise NameError('이름은 2~6자 사이로 입력해주세요:')
except NameError as e:
    print(e)
else:
    print(f'입력된 이름은 {name}')


