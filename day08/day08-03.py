"""
argument_parameter
인수와 매개변수

"""

'''
함수로 전달되는 인수(argument) 를 저장하는 변수를 매개변수(parameter) 라고 한다!
이 둘은 다른 개념이지만 함수가 호출된 뒤에는 인수와 매개변수가 같은 값을 가지게 되므로
이를 구분하지 않고 부르는 경우가 있습니다.


def welcome (매개변수)
    print(매개변수)

인수 = 1    
welcome(인수)
'''

'''
1. 인수가 있는 함수

'''
"""
def introduce(name,age):
    print(f'내 이름은 {name}이고, 나이는{age}살 입니다.')

introduce('james',25)

"""

'''
점수를 입력하면 해당 점수가 출력되는 함수를 만드세요
함수명 show()
'''


"""
def show(score):
    score = int(input("점수를 입력해주시오:"))
    print(f"당신의 점수는{score} 입니다.")
show()
"""



'''
점수를 10개 입력하면 해당 점수들이 출력되는 함수를 만드세요

'''

"""
def show_ten() :
    score_li = []
    for i in range(10):
        score = int(input('점수를 입력하세요:'))

        score_li.append(score)
    print(f'당신의 점수는 {score_li} 입니다.')

show_ten()
"""
'''
2. 가변 매개변수
함수로 전달해야 하는 인수의 개수가 정해지지 않아도
매개변수를 선언할 수 있습니다.
이를 가변 매개변수라고 합니다.
가변 매개변수를 만드는 키워드는 애스터리스트(*) 입니다.
매개변수 앞에 * 을 붙이면
곧바로 가변 매개변수가 되면서 전달되는 모든 인수를 하나의 튜플로 만들어줍니다.


*show() 함수를 만든다
 - show()함수는 전달받은 모든 인수를 하나씩 출력하는 함수.
 '''



'''
예제 함수를 두개 만드는데 하나는 인수가 하나인 값만 받아서 출력
두번째 함수는 두개의 인수를 받아서 두개의 인수를 출력
함수명: one(인수), two(인수1,인수2)
호출 출력
one(1)
1

two(1,2)
1
2
'''
def one(x):
    print(x)

def two(x,y):
    print(x)
    print(y)

one(1)
two(3,4)

def three(*nums):
    for i in nums:
        print(i)

three(1,5,54,32,6)

def show(*args):
    print(args)
    for item in args:
        print(item)

show('python')
show('happy','birthday')

'''
디폴트 매개변수
매개변수 전달되는 인수가 없는 경우에 기본적으로 사용할 수 있도록
매개변수에 기본값을 설정할 수 있습니다.
이 것을 디폴트 매개변수(기본 매개변수) 라고 합니다.
- 사용자가 함수를 호출할 때 매개변수로 아무 값도 넣지 않는다면
'안녕하세요' 라는 인사말이 화면에 나타난다.

'''
# 매개변수에 아무 값이 들어오지 않을 때 안녕하세요 를 출력!
def greet(message='안녕하세요'):
    print(message)


# 매개변수
greet()
# 매개변수로 반갑습니다가 들어가서 반갑습니다가 출력.
"""
def greet(message='안녕하세요',name):
    print(f'{name}님, {message}')

greet('김철수')
매개변수 순서를 유의해야 한다!

항상 디폴트 값을 가지는 매개변수는 뒤에 있는게 좋다!
"""


'''
 non-default argument follows default argument
기본인수가 아닌 인수가 기본인수를 따르고 있다?
-> 기본 인수가 아닌 인수
'''



'''
다음은 전달된 모든 인수를 모두 더해서 합계를 출력하는 프로그램이디ㅏ!
(1,2)의 합은 3입니다.
.
.
.
'''
def adder(*nums):
    print(f'{nums}의 합은 {sum(nums)}입니다.')

adder(1,2)
adder(1,2,3)